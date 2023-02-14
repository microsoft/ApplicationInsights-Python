# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from logging import DEBUG, getLogger

from azure.monitor.opentelemetry import configure_azure_monitor

configure_azure_monitor(
    connection_string="<your-connection-string>",
    logger_name=__name__,
    logging_level=DEBUG,
    disable_metrics=True,
    disable_tracing=True,
)

logger = getLogger(__name__)
logger.setLevel(DEBUG)

# Pass custom properties in a dictionary with the extra argument
logger.debug("DEBUG: Debug with properties", extra={"debug": "true"})

input()
