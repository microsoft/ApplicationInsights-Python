# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------
import logging

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.semconv.resource import ResourceAttributes

from azure.monitor.opentelemetry.distro.util import get_configurations
from azure.monitor.opentelemetry.exporter import (
    AzureMonitorTraceExporter
)


_logger = logging.getLogger(__name__)


def configure_opentelemetry(**kwargs):
    # pylint: disable=too-many-locals
    # pylint: disable=too-many-statements
    """
    Configures OpenTelemetry with Lightstep environment variables
    This function works as a configuration layer that allows the Lightstep end
    user to use current environment variables seamlessly with OpenTelemetry. In
    this way, it is not needed to make any configuration changes to the
    environment before using OpenTelemetry. The configuration can be done via
    environment variables (prefixed with `LS`) or via arguments passed to this
    function. Each argument has a 1:1 correspondence with an environment
    variable, their description follows:
    """

    configurations = get_configurations(**kwargs)
    connection_string = configurations["connection_string"]
    service_name = configurations["service_name"]
    service_namespace = configurations["service_namespace"]
    service_instance_id = configurations["service_instance_id"]
    service_version = configurations["service_version"]
    disable_tracing = configurations["disable_tracing"]

    if not disable_tracing:
        resource = Resource.create({
                ResourceAttributes.SERVICE_NAME: service_name,
                ResourceAttributes.SERVICE_NAMESPACE: service_namespace,
                ResourceAttributes.SERVICE_INSTANCE_ID: service_instance_id,
                ResourceAttributes.SERVICE_VERSION: service_version,
            }
        )
        trace.set_tracer_provider(TracerProvider(resource=resource))
        exporter = AzureMonitorTraceExporter(connection_string=connection_string)
        span_processor = BatchSpanProcessor(exporter)
        trace.get_tracer_provider().add_span_processor(span_processor)
