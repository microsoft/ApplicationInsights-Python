# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------
from azure.monitor.opentelemetry.distro.util import get_configurations
from azure.monitor.opentelemetry.exporter import (
    ApplicationInsightsSampler,
    AzureMonitorTraceExporter,
)
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.semconv.resource import ResourceAttributes


def configure_azure_monitor(**kwargs):
    """
    This function works as a configuration layer that allows the
    end user to configure OpenTelemetry and Azure monitor components. The
    configuration can be done via arguments passed to this function.
    """

    configurations = get_configurations(**kwargs)
    disable_tracing = configurations.get("disable_tracing", False)
    service_name = configurations.get("service_name", "")
    service_namespace = configurations.get("service_namespace", "")
    service_instance_id = configurations.get("service_instance_id", "")
    sampling_ratio = configurations.get("sampling_ratio", 1.0)
    tracing_export_interval = configurations.get("tracing_export_interval", 30000)

    if not disable_tracing:
        resource = Resource.create(
            {
                ResourceAttributes.SERVICE_NAME: service_name,
                ResourceAttributes.SERVICE_NAMESPACE: service_namespace,
                ResourceAttributes.SERVICE_INSTANCE_ID: service_instance_id,
            }
        )
        tracer_provider = TracerProvider(
            sampler=ApplicationInsightsSampler(
                sampling_ratio=sampling_ratio
            ),
            resource=resource,
        )
        trace.set_tracer_provider(tracer_provider)
        exporter = AzureMonitorTraceExporter(**kwargs)
        span_processor = BatchSpanProcessor(
            exporter,
            export_timeout_millis=tracing_export_interval,
        )
        trace.get_tracer_provider().add_span_processor(span_processor)
