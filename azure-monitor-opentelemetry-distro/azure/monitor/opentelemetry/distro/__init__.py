# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------
from logging import NOTSET, getLogger

from azure.monitor.opentelemetry.distro.util import get_configurations
from azure.monitor.opentelemetry.exporter import (
    ApplicationInsightsSampler,
    AzureMonitorLogExporter,
    AzureMonitorTraceExporter,
)
from opentelemetry.sdk._logs import (
    LoggerProvider,
    LoggingHandler,
    get_logger_provider,
    set_logger_provider,
)
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.semconv.resource import ResourceAttributes
from opentelemetry.trace import get_tracer_provider, set_tracer_provider


def configure_azure_monitor(**kwargs):
    """
    This function works as a configuration layer that allows the
    end user to configure OpenTelemetry and Azure monitor components. The
    configuration can be done via arguments passed to this function.
    """

    configurations = get_configurations(**kwargs)
    service_name = configurations.get("service_name", "")
    service_namespace = configurations.get("service_namespace", "")
    service_instance_id = configurations.get("service_instance_id", "")
    disable_logging = configurations.get("disable_logging", False)
    logging_level = configurations.get("logging_level", NOTSET)
    logging_export_interval_millis = configurations.get(
        "logging_export_interval_millis", 30000
    )
    disable_tracing = configurations.get("disable_tracing", False)
    sampling_ratio = configurations.get("sampling_ratio", 1.0)
    tracing_export_interval_millis = configurations.get(
        "tracing_export_interval_millis", 30000
    )

    resource = None
    if not disable_logging or not disable_tracing:
        resource = Resource.create(
            {
                ResourceAttributes.SERVICE_NAME: service_name,
                ResourceAttributes.SERVICE_NAMESPACE: service_namespace,
                ResourceAttributes.SERVICE_INSTANCE_ID: service_instance_id,
            }
        )
    if not disable_logging:
        logger_provider = LoggerProvider(resource=resource)
        set_logger_provider(logger_provider)
        log_exporter = AzureMonitorLogExporter(**kwargs)
        log_record_processor = BatchLogRecordProcessor(
            log_exporter,
            export_timeout_millis=logging_export_interval_millis,
        )
        get_logger_provider().add_log_record_processor(log_record_processor)
        handler = LoggingHandler(
            level=logging_level, logger_provider=get_logger_provider()
        )
        getLogger().addHandler(handler)
    if not disable_tracing:
        tracer_provider = TracerProvider(
            sampler=ApplicationInsightsSampler(sampling_ratio=sampling_ratio),
            resource=resource,
        )
        set_tracer_provider(tracer_provider)
        trace_exporter = AzureMonitorTraceExporter(**kwargs)
        span_processor = BatchSpanProcessor(
            trace_exporter,
            export_timeout_millis=tracing_export_interval_millis,
        )
        get_tracer_provider().add_span_processor(span_processor)
