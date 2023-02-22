# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from logging import WARNING, getLogger

from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry.sdk.resources import Resource, ResourceAttributes

configure_azure_monitor(
    connection_string="<your-connection-string>",
    logger_name=__name__,
    logging_level=WARNING,
    resource=Resource.create(
        {
            ResourceAttributes.SERVICE_NAME: "simple_service",
            ResourceAttributes.SERVICE_INSTANCE_ID: "simple_logging_instance",
        }
    ),
    disable_metrics=True,
    disable_tracing=True,
)

logger = getLogger(__name__)

logger.info("info log")
logger.warning("warning log")
logger.error("error log")
