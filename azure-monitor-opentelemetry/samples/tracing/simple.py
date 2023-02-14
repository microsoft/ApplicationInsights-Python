# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource, ResourceAttributes

configure_azure_monitor(
    connection_string="<your-connection-string>",
    resource=Resource.create(
        {
            ResourceAttributes.SERVICE_NAME: "simple_service",
            ResourceAttributes.SERVICE_INSTANCE_ID: "simple_tracing_instance",
        }
    ),
    tracing_export_interval_millis=15000,
    disable_logging=True,
    disable_metrics=True,
)

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("hello"):
    print("Hello, World!")

input()
