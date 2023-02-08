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

logger.info("info log")
logger.warning("warning log")
logger.error("error log")
