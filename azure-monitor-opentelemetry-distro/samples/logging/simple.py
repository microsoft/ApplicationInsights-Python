# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from logging import WARN, getLogger

from azure.monitor.opentelemetry.distro import configure_azure_monitor
from opentelemetry import trace

configure_azure_monitor(
    connection_string="<your-connection-string>",
    service_name="foo_service",
    logging_level=WARN,
    disable_metrics=True,
    disable_tracing=True,
)

logger = getLogger(__name__)
tracer = trace.get_tracer(__name__)

logger.info("info log")
logger.warning("warning log")
logger.error("error log")

with tracer.start_as_current_span("hello"):
    print("Hello, World!")
    logger.info("Correlated info log")
    logger.warning("Correlated warning log")
    logger.error("Correlated error log")
