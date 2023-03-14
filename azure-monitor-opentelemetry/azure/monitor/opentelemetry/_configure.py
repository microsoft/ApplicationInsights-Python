# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------
from logging import NOTSET, getLogger
from typing import Any, Dict, Sequence

from azure.monitor.opentelemetry._types import ConfigurationValue
from azure.monitor.opentelemetry.exporter import (
    ApplicationInsightsSampler,
    AzureMonitorLogExporter,
    AzureMonitorMetricExporter,
    AzureMonitorTraceExporter,
)
from azure.monitor.opentelemetry.util.configurations import _get_configurations
from opentelemetry._logs import get_logger_provider, set_logger_provider
from opentelemetry.instrumentation.dependencies import (
    get_dist_dependency_conflicts,
)
from opentelemetry.instrumentation.instrumentor import BaseInstrumentor
from opentelemetry.metrics import set_meter_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import get_tracer_provider, set_tracer_provider
from pkg_resources import iter_entry_points

_logger = getLogger(__name__)


_SUPPORTED_INSTRUMENTED_LIBRARIES = (
    "django",
    "fastapi",
    "flask",
    "psycopg2",
    "requests",
    "urllib",
    "urllib3",
)


InstrumentationConfig = Dict[str, Dict[str, Any]]


def configure_azure_monitor(**kwargs) -> None:
    """
    This function works as a configuration layer that allows the
    end user to configure OpenTelemetry and Azure monitor components. The
    configuration can be done via arguments passed to this function.
    :keyword str connection_string: Connection string for your Application Insights resource.
    :keyword Sequence[str] exclude_instrumentations: Specifies instrumentations you do not want to enable.
    :keyword Resource resource: Specified the OpenTelemetry [resource][opentelemetry_spec_resource] associated with your application.
    :keyword bool disable_logging: If set to `True`, disables collection and export of logging telemetry. Defaults to `False`.
    :keyword bool disable_metrics: If set to `True`, disables collection and export of metric telemetry. Defaults to `False`.
    :keyword bool disable_tracing: If set to `True`, disables collection and export of distributed tracing telemetry. Defaults to `False`.
    :keyword int logging_level: Specifies the logging of the logs you would like to collect for your logging pipeline.
    :keyword str logger_name: Specifies the logger name under which logging will be instrumented. Defaults to "" which corresponds to the root logger.
    :keyword int logging_export_interval_ms: Specifies the logging export interval in milliseconds. Defaults to 5000.
    :keyword Sequence[MetricReader] metric_readers: Specifies the metric readers that you would like to use for your metric pipeline.
    :keyword Sequence[View] views: Specifies the list of views to configure for the metric pipeline.
    :keyword float sampling_ratio: Specifies the ratio of distributed tracing telemetry to be sampled. Accepted values are in the range [0,1]. Defaults to 1.0, meaning no telemetry is sampled out.
    :keyword int tracing_export_interval_ms: Specifies the distributed tracing export interval in milliseconds. Defaults to 5000.
    :keyword InstrumentationConfig instrumentation_config: Specifies a dictionary of kwargs that will be applied to instrumentation configuration. You can specify which instrumentation you want to
        configure by name in the key field and value as a dictionary representing `kwargs` for the corresponding instrumentation.
        Refer to the `Supported Library` section of https://github.com/microsoft/ApplicationInsights-Python/tree/main/azure-monitor-opentelemetry#officially-supported-instrumentations for the list of suppoprted library names.
    :keyword bool disable_offline_storage: Boolean value to determine whether to disable storing failed telemetry records for retry. Defaults to `False`.
    :keyword str storage_directory: Storage directory in which to store retry files. Defaults to `<tempfile.gettempdir()>/Microsoft/AzureMonitor/opentelemetry-python-<your-instrumentation-key>`.
    :rtype: None
    """

    configurations = _get_configurations(**kwargs)
    _validate_configurations(configurations)

    disable_tracing = configurations.get("disable_tracing", False)
    disable_logging = configurations.get("disable_logging", False)
    disable_metrics = configurations.get("disable_metrics", False)

    resource = None
    if not disable_logging or not disable_tracing or not disable_metrics:
        resource = _get_resource(configurations)

    # Setup tracing pipeline
    if not disable_tracing:
        _setup_tracing(resource, configurations)

    # Setup logging pipeline
    if not disable_logging:
        _setup_logging(resource, configurations)

    # Setup metrics pipeline
    if not disable_metrics:
        _setup_metrics(resource, configurations)

    # Setup instrumentations
    # Instrumentations need to be setup last so to use the global providers
    # instanstiated in the other setup steps
    _setup_instrumentations(configurations)


def _get_resource(configurations: Dict[str, ConfigurationValue]) -> Resource:
    return configurations.get("resource", Resource.create())


def _setup_tracing(
    resource: Resource, configurations: Dict[str, ConfigurationValue]
):
    sampling_ratio = configurations.get("sampling_ratio", 1.0)
    tracing_export_interval_ms = configurations.get(
        "tracing_export_interval_ms", 5000
    )
    tracer_provider = TracerProvider(
        sampler=ApplicationInsightsSampler(sampling_ratio=sampling_ratio),
        resource=resource,
    )
    set_tracer_provider(tracer_provider)
    trace_exporter = AzureMonitorTraceExporter(**configurations)
    span_processor = BatchSpanProcessor(
        trace_exporter,
        schedule_delay_millis=tracing_export_interval_ms,
    )
    get_tracer_provider().add_span_processor(span_processor)


def _setup_logging(
    resource: Resource, configurations: Dict[str, ConfigurationValue]
):
    logger_name = configurations.get("logger_name", "")
    logging_level = configurations.get("logging_level", NOTSET)
    logging_export_interval_ms = configurations.get(
        "logging_export_interval_ms", 5000
    )
    logger_provider = LoggerProvider(resource=resource)
    set_logger_provider(logger_provider)
    log_exporter = AzureMonitorLogExporter(**configurations)
    log_record_processor = BatchLogRecordProcessor(
        log_exporter,
        schedule_delay_millis=logging_export_interval_ms,
    )
    get_logger_provider().add_log_record_processor(log_record_processor)
    handler = LoggingHandler(
        level=logging_level, logger_provider=get_logger_provider()
    )
    getLogger(logger_name).addHandler(handler)


def _setup_metrics(
    resource: Resource, configurations: Dict[str, ConfigurationValue]
):
    views = configurations.get("views", ())
    metric_readers = configurations.get("metric_readers", [])
    metric_exporter = AzureMonitorMetricExporter(**configurations)
    reader = PeriodicExportingMetricReader(metric_exporter)
    meter_provider = MeterProvider(
        metric_readers=[reader] + metric_readers,
        resource=resource,
        views=views,
    )
    set_meter_provider(meter_provider)


def _setup_instrumentations(configurations: Dict[str, ConfigurationValue]):
    exclude_instrumentations = configurations.get(
        "exclude_instrumentations", []
    )
    instrumentation_configs = configurations.get("instrumentation_config", {})

    # use pkg_resources for now until https://github.com/open-telemetry/opentelemetry-python/pull/3168 is merged
    for entry_point in iter_entry_points("opentelemetry_instrumentor"):
        lib_name = entry_point.name
        if lib_name not in _SUPPORTED_INSTRUMENTED_LIBRARIES:
            continue
        if lib_name in exclude_instrumentations:
            _logger.debug("Instrumentation excluded for library %s", lib_name)
            continue
        try:
            # Check if dependent libraries/version are installed
            conflict = get_dist_dependency_conflicts(entry_point.dist)
            if conflict:
                _logger.debug(
                    "Skipping instrumentation %s: %s",
                    entry_point.name,
                    conflict,
                )
                continue
            # Load the instrumentor via entrypoint
            instrumentor: BaseInstrumentor = entry_point.load()
            # Call instrument() with configuration
            config = instrumentation_configs.get(lib_name, {})
            # tell instrumentation to not run dep checks again as we already did it above
            config["skip_dep_check"] = True
            instrumentor().instrument(**config)
        except Exception as ex:
            _logger.warning(
                "Exception occured when instrumenting: %s.",
                lib_name,
                exc_info=ex,
            )

def _is_instance_or_none(var, type):
    return isinstance(var, type) or var is None

def _validate_configurations(configurations):
    assert(_is_instance_or_none(configurations.get("connection_string"), str))
    assert(_is_instance_or_none(configurations.get("exclude_instrumentations"), Sequence))
    assert(_is_instance_or_none(configurations.get("resource"), Resource))
    assert(_is_instance_or_none(configurations.get("disable_logging"), bool))
    assert(_is_instance_or_none(configurations.get("disable_metrics"), bool))
    assert(_is_instance_or_none(configurations.get("disable_tracing"), bool))
    assert(_is_instance_or_none(configurations.get("logging_level"), int))
    assert(_is_instance_or_none(configurations.get("logger_name"), str))
    assert(_is_instance_or_none(configurations.get("logging_export_interval_millis"), int))
    assert(_is_instance_or_none(configurations.get("metric_readers"), Sequence))
    assert(_is_instance_or_none(configurations.get("views"), Sequence))
    assert(_is_instance_or_none(configurations.get("sampling_ratio"), float))
    assert(_is_instance_or_none(configurations.get("tracing_export_interval_millis"), int))
    for library in _SUPPORTED_INSTRUMENTED_LIBRARIES:
        assert(_is_instance_or_none(configurations.get(library + "_config"), Dict))
    assert(_is_instance_or_none(configurations.get("disable_offline_storage"), bool))
    assert(_is_instance_or_none(configurations.get("storage_directory"), str))
    
