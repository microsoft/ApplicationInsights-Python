# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry import metrics
from opentelemetry.sdk.metrics import Counter
from opentelemetry.sdk.metrics.view import View

# Create a view matching the counter instrument `my.counter`
# and configure the new name `my.counter.total` for the result metrics stream
change_metric_name_view = View(
    connection_string="<your-connection-string>",
    instrument_type=Counter,
    instrument_name="my.counter",
    name="my.counter.total",
)

# Configure Azure monitor collection telemetry pipeline
configure_azure_monitor(
    connection_string="<your-connection-string>",
    disable_logging=True,
    disable_tracing=True,
    metrics_export_interval_millis=30000,
    views=[change_metric_name_view],
)

meter = metrics.get_meter_provider().get_meter("view-name-change")
my_counter = meter.create_counter("my.counter")
my_counter.add(100)

input()
