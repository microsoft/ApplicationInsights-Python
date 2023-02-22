# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------
import importlib
from logging import NOTSET, getLogger
from typing import Dict

from azure.monitor.opentelemetry._types import ConfigurationValue
from azure.monitor.opentelemetry.exporter import (
    ApplicationInsightsSampler,
    AzureMonitorLogExporter,
    AzureMonitorMetricExporter,
    AzureMonitorTraceExporter,
)
from azure.monitor.opentelemetry.util import _get_configurations
from opentelemetry._logs import get_logger_provider, set_logger_provider
from opentelemetry.metrics import set_meter_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import get_tracer_provider, set_tracer_provider

_logger = getLogger(__name__)


_INSTRUMENTATION_CONFIG_SUFFIX = "_config"
_SUPPORTED_INSTRUMENTED_LIBRARIES = (
    "django",
    "flask",
    "psycopg2",
    "requests",
)


def configure_azure_monitor(**kwargs) -> None:
    """
    This function works as a configuration layer that allows the
    end user to configure OpenTelemetry and Azure monitor components. The
    configuration can be done via arguments passed to this function.
    :keyword str connection_string: Connection string for your Application Insights resource.
    :keyword Sequence[str] connection_string: Specifies the libraries with instrumentations to be enabled.
    :keyword Resource resource: Specified the OpenTelemetry [resource][opentelemetry_spec_resource] associated with your application.
    :keyword bool disable_logging: If set to `True`, disables collection and export of logging telemetry. Defaults to `False`.
    :keyword bool disable_metrics: If set to `True`, disables collection and export of metric telemetry. Defaults to `False`.
    :keyword bool disable_tracing: If set to `True`, disables collection and export of distributed tracing telemetry. Defaults to `False`.
    :keyword int logging_level: Specifies the logging of the logs you would like to collect for your logging pipeline.
    :keyword str logger_name: Specifies the logger name under which logging will be instrumented. Defaults to "" which corresponds to the root logger.
    :keyword int logging_export_interval_millis: Specifies the logging export interval in milliseconds. Defaults to 5000.
    :keyword Sequence[MetricReader] metric_readers: Specifies the metric readers that you would like to use for your metric pipeline.
    :keyword Sequence[View] views: Specifies the list of views to configure for the metric pipeline.
    :keyword float sampling_ratio: Specifies the ratio of distributed tracing telemetry to be sampled. Accepted values are in the range [0,1]. Defaults to 1.0, meaning no telemetry is sampled out.
    :keyword int tracing_export_interval_millis: Specifies the distributed tracing export interval in milliseconds. Defaults to 5000.
    :keyword Dict[str, Any] <instrumentation>_config: Specifies a dictionary of kwargs that will be applied to configuration for instrumentation <instrumentation>.
    :keyword bool disable_offline_storage: Boolean value to determine whether to disable storing failed telemetry records for retry. Defaults to `False`.
    :keyword str storage_directory: Storage directory in which to store retry files. Defaults to `<tempfile.gettempdir()>/Microsoft/AzureMonitor/opentelemetry-python-<your-instrumentation-key>`.
    :rtype: None
    """

    configurations = _get_configurations(**kwargs)

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
    tracing_export_interval_millis = configurations.get(
        "tracing_export_interval_millis", 5000
    )
    tracer_provider = TracerProvider(
        sampler=ApplicationInsightsSampler(sampling_ratio=sampling_ratio),
        resource=resource,
    )
    set_tracer_provider(tracer_provider)
    trace_exporter = AzureMonitorTraceExporter(**configurations)
    span_processor = BatchSpanProcessor(
        trace_exporter,
        schedule_delay_millis=tracing_export_interval_millis,
    )
    get_tracer_provider().add_span_processor(span_processor)


def _setup_logging(
    resource: Resource, configurations: Dict[str, ConfigurationValue]
):
    logger_name = configurations.get("logger_name", "")
    logging_level = configurations.get("logging_level", NOTSET)
    logging_export_interval_millis = configurations.get(
        "logging_export_interval_millis", 5000
    )
    logger_provider = LoggerProvider(resource=resource)
    set_logger_provider(logger_provider)
    log_exporter = AzureMonitorLogExporter(**configurations)
    log_record_processor = BatchLogRecordProcessor(
        log_exporter,
        schedule_delay_millis=logging_export_interval_millis,
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
    instrumentations = configurations.get("instrumentations", [])
    instrumentation_configs = {}

    # Instrumentation specific configs
    # Format is {"<library_name>": {"<config>":<value>}}
    for k, v in configurations.items():
        if k.endswith(_INSTRUMENTATION_CONFIG_SUFFIX):
            lib_name = k.partition(_INSTRUMENTATION_CONFIG_SUFFIX)[0]
            instrumentation_configs[lib_name] = v

    for lib_name in instrumentations:
        if lib_name in _SUPPORTED_INSTRUMENTED_LIBRARIES:
            try:
                importlib.import_module(lib_name)
            except ImportError:
                _logger.warning(
                    "Unable to import %s. Please make sure it is installed.",
                    lib_name,
                )
                continue
            instr_lib_name = "opentelemetry.instrumentation." + lib_name
            try:
                module = importlib.import_module(instr_lib_name)
                instrumentor_name = "{}Instrumentor".format(
                    lib_name.capitalize()
                )
                class_ = getattr(module, instrumentor_name)
                config = instrumentation_configs.get(lib_name, {})
                class_().instrument(**config)
            except ImportError:
                _logger.warning(
                    "Unable to import %s. Please make sure it is installed.",
                    instr_lib_name,
                )
            except Exception as ex:
                _logger.warning(
                    "Exception occured when instrumenting: %s.",
                    lib_name,
                    exc_info=ex,
                )
        else:
            _logger.warning(
                "Instrumentation not supported for library: %s.", lib_name
            )
