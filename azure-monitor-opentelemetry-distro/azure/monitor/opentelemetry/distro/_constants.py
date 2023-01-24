# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

import platform
from os import environ
from pathlib import Path

from azure.monitor.opentelemetry.exporter._connection_string_parser import (
    ConnectionStringParser,
)

_LOG_PATH_LINUX = "/var/log/applicationinsights"
_LOG_PATH_WINDOWS = "\\LogFiles\\ApplicationInsights"
_IS_ON_APP_SERVICE = "WEBSITE_SITE_NAME" in environ
# TODO: Add environment variable to enabled diagnostics off of App Service
_IS_DIAGNOSTICS_ENABLED = _IS_ON_APP_SERVICE
# TODO: Enabled when duplciate logging issue is solved
# _EXPORTER_DIAGNOSTICS_ENABLED_ENV_VAR = (
#     "AZURE_MONITOR_OPENTELEMETRY_DISTRO_ENABLE_EXPORTER_DIAGNOSTICS"
# )


def _get_log_path(status_log_path=False):
    system = platform.system()
    if system == "Linux":
        return _LOG_PATH_LINUX
    elif system == "Windows":
        log_path = str(Path.home()) + _LOG_PATH_WINDOWS
        if status_log_path:
            return log_path + "\\status"
        else:
            return log_path
    else:
        return None


def _env_var_or_default(var_name, default_val=""):
    try:
        return environ[var_name]
    except KeyError:
        return default_val


# TODO: Enabled when duplciate logging issue is solved
# def _is_exporter_diagnostics_enabled():
#     return (
#         _EXPORTER_DIAGNOSTICS_ENABLED_ENV_VAR in environ
#         and environ[_EXPORTER_DIAGNOSTICS_ENABLED_ENV_VAR] == "True"
#     )


_EXTENSION_VERSION = _env_var_or_default(
    "ApplicationInsightsAgent_EXTENSION_VERSION", "disabled"
)
# TODO: Enabled when duplciate logging issue is solved
# _EXPORTER_DIAGNOSTICS_ENABLED = _is_exporter_diagnostics_enabled()


class ConnectionStringConstants:
    _conn_str_parser = None

    def set_conn_str_from_env_var():
        ConnectionStringConstants._conn_str_parser = ConnectionStringParser()

    def set_conn_str(conn_str):
        ConnectionStringConstants._conn_str_parser = ConnectionStringParser(
            conn_str
        )

    def get_conn_str():
        if ConnectionStringConstants._conn_str_parser is None:
            return None
        return ConnectionStringConstants._conn_str_parser._conn_str

    def get_customer_ikey():
        if ConnectionStringConstants._conn_str_parser is None:
            return None
        return ConnectionStringConstants._conn_str_parser.instrumentation_key
