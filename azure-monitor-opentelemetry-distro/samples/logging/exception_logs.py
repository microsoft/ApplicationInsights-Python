# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from logging import WARNING, getLogger

from azure.monitor.opentelemetry.distro import configure_azure_monitor

configure_azure_monitor(
    connection_string="<your-connection-string>",
    service_name="foo_service",
    logging_level=WARNING,
    disable_metrics=True,
    disable_tracing=True,
)

logger = getLogger(__name__)

# The following code will generate two pieces of exception telemetry
# that are identical in nature
try:
    val = 1 / 0
    print(val)
except ZeroDivisionError:
    logger.exception("Error: Division by zero")

try:
    val = 1 / 0
    print(val)
except ZeroDivisionError:
    logger.error("Error: Division by zero", stack_info=True, exc_info=True)