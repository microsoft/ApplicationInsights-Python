# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from logging import WARNING, getLogger

import flask
from azure.monitor.opentelemetry import configure_azure_monitor

configure_azure_monitor(
    connection_string="<your-connection-string>",
    logger_name=__name__,
    logging_level=WARNING,
    disable_metrics=True,
    instrumentations=["flask"],
    tracing_export_interval_millis=15000,
)

logger = getLogger(__name__)

app = flask.Flask(__name__)


@app.route("/info_log")
def info_log():
    message = "Correlated info log"
    logger.info(message)
    return message


@app.route("/error_log")
def error_log():
    message = "Correlated error log"
    logger.error(message)
    return message


@app.route("/error_log")
def error_log():
    message = "Correlated error log"
    logger.error(message)
    return message


if __name__ == "__main__":
    app.run(host="localhost", port=8080)

    logger.info("Correlated info log")
    logger.warning("Correlated warning log")
    logger.error("Correlated error log")
