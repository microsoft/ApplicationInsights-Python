# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry import trace

configure_azure_monitor(
    connection_string="<your-connection-string>",
    # Sampling ratio of between 0 and 1 inclusive
    # 0.1 means approximately 10% of your traces are sent
    sampling_ratio=0.1,
    tracing_export_interval_ms=15000,
    disable_logging=True,
    disable_metrics=True,
)

tracer = trace.get_tracer(__name__)

for i in range(100):
    # Approximately 90% of these spans should be sampled out
    with tracer.start_as_current_span("hello"):
        print("Hello, World!")

input()
