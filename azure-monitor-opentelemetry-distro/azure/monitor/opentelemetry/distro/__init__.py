# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------
import importlib
from logging import NOTSET, getLogger
from typing import Any, Dict

from azure.monitor.opentelemetry.distro.util import get_configurations
from azure.monitor.opentelemetry.exporter import (
    ApplicationInsightsSampler,
    AzureMonitorLogExporter,
    AzureMonitorMetricExporter,
    AzureMonitorTraceExporter,
)
from opentelemetry.metrics import get_meter_provider, set_meter_provider
from opentelemetry.sdk._logs import (
    LoggerProvider,
    LoggingHandler,
    get_logger_provider,
    set_logger_provider,
)
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.semconv.resource import ResourceAttributes
from opentelemetry.trace import get_tracer_provider, set_tracer_provider

_logger = getLogger(__name__)


_SUPPORTED_INSTRUMENTED_LIBRARIES = {
    "django",
    "flask",
    "psycopg2",
    "requests",
}


def configure_azure_monitor(**kwargs):
    """
    This function works as a configuration layer that allows the
    end user to configure OpenTelemetry and Azure monitor components. The
    configuration can be done via arguments passed to this function.
    """

    configurations = get_configurations(**kwargs)

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


def _get_resource(configurations: Dict[str, Any]) -> Resource:
    service_name = configurations.get("service_name", "")
    service_namespace = configurations.get("service_namespace", "")
    service_instance_id = configurations.get("service_instance_id", "")
    return Resource.create(
        {
            ResourceAttributes.SERVICE_NAME: service_name,
            ResourceAttributes.SERVICE_NAMESPACE: service_namespace,
            ResourceAttributes.SERVICE_INSTANCE_ID: service_instance_id,
        }
    )


def _setup_tracing(resource: Resource, configurations: Dict[str, Any]):
    sampling_ratio = configurations.get("sampling_ratio", 1.0)
    tracing_export_interval_millis = configurations.get(
        "tracing_export_interval_millis", 30000
    )
    tracer_provider = TracerProvider(
        sampler=ApplicationInsightsSampler(sampling_ratio=sampling_ratio),
        resource=resource,
    )
    set_tracer_provider(tracer_provider)
    trace_exporter = AzureMonitorTraceExporter(**configurations)
    span_processor = BatchSpanProcessor(
        trace_exporter,
        export_timeout_millis=tracing_export_interval_millis,
    )
    get_tracer_provider().add_span_processor(span_processor)


def _setup_logging(resource: Resource, configurations: Dict[str, Any]):
    logger_name = configurations.get("logger_name", "")
    logging_level = configurations.get("logging_level", NOTSET)
    logging_export_interval_millis = configurations.get(
        "logging_export_interval_millis", 30000
    )
    logger_provider = LoggerProvider(resource=resource)
    set_logger_provider(logger_provider)
    log_exporter = AzureMonitorLogExporter(**configurations)
    log_record_processor = BatchLogRecordProcessor(
        log_exporter,
        export_timeout_millis=logging_export_interval_millis,
    )
    get_logger_provider().add_log_record_processor(log_record_processor)
    handler = LoggingHandler(
        level=logging_level, logger_provider=get_logger_provider()
    )
    getLogger(logger_name).addHandler(handler)


def _setup_metrics(resource: Resource, configurations: Dict[str, Any]):
    metrics_export_interval_millis = configurations.get(
        "metrics_export_interval_millis", 60000
    )
    views = configurations.get("views", ())
    metric_exporter = AzureMonitorMetricExporter(**configurations)
    reader = PeriodicExportingMetricReader(
        metric_exporter,
        export_interval_millis=metrics_export_interval_millis,
    )
    meter_provider = MeterProvider(
        metric_readers=[reader],
        resource=resource,
        views=views,
    )
    set_meter_provider(meter_provider)


def _setup_instrumentations(configurations: Dict[str, Any]):
    instrumentations = configurations.get("instrumentations", [])
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
                class_().instrument()
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
