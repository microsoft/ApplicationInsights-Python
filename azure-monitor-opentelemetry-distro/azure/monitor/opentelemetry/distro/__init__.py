# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------
from azure.monitor.opentelemetry.distro.util import get_configurations
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.semconv.resource import ResourceAttributes


def configure_opentelemetry(**kwargs):
    """
    This function works as a configuration layer that allows the
    end user to configure OpenTelemetry and Azure monitor components. The
    configuration can be done via environment variables or
    via arguments passed to this function. Each argument has a 1:1
    correspondence with an environment variable.
    """

    configurations = get_configurations(**kwargs)
    connection_string = configurations["connection_string"]
    service_name = configurations["service_name"]
    service_namespace = configurations["service_namespace"]
    service_instance_id = configurations["service_instance_id"]
    disable_tracing = configurations["disable_tracing"]

    if not disable_tracing:
        resource = Resource.create(
            {
                ResourceAttributes.SERVICE_NAME: service_name,
                ResourceAttributes.SERVICE_NAMESPACE: service_namespace,
                ResourceAttributes.SERVICE_INSTANCE_ID: service_instance_id,
            }
        )
        trace.set_tracer_provider(TracerProvider(resource=resource))
        exporter = AzureMonitorTraceExporter(
            connection_string=connection_string
        )
        span_processor = BatchSpanProcessor(exporter)
        trace.get_tracer_provider().add_span_processor(span_processor)
