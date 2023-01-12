# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from azure.monitor.opentelemetry.distro import configure_azure_monitor
from opentelemetry import trace

configure_azure_monitor(
    connection_string="<your-connection-string>",
    service_name="foo_service",
    tracing_export_interval=15,
)

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("hello"):
    print("Hello, World!")

input()
