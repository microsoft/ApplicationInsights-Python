# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from json import dumps
from os import getpid, makedirs
from os.path import exists, join
from platform import node

from azure.monitor.opentelemetry.distro._constants import (
    ConnectionStringConstants,
    _EXTENSION_VERSION,
    _IS_DIAGNOSTICS_ENABLED,
    _get_log_path,
)
from azure.monitor.opentelemetry.distro._version import VERSION
import logging

_MACHINE_NAME = node()
_STATUS_LOG_PATH = _get_log_path(status_log_path=True)
_logger = logging.getLogger(__name__)


class AzureStatusLogger:
    def _get_status_json(agent_initialized_successfully, pid, reason=None):
        customer_ikey = ConnectionStringConstants.get_customer_ikey()
        if customer_ikey is None:
            try:
                ConnectionStringConstants.set_conn_str_from_env_var()
                customer_ikey = ConnectionStringConstants.get_customer_ikey()
            except ValueError as e:
                _logger.error("Failed to parse Instrumentation Key: %s" % e)
                customer_ikey = "unknown"
        status_json = {
            "AgentInitializedSuccessfully": agent_initialized_successfully,
            "AppType": "python",
            "MachineName": _MACHINE_NAME,
            "PID": pid,
            "SdkVersion": VERSION,
            "Ikey": customer_ikey,
            "ExtensionVersion": _EXTENSION_VERSION,
        }
        if reason:
            status_json["Reason"] = reason
        return status_json

    def log_status(agent_initialized_successfully, reason=None):
        if _IS_DIAGNOSTICS_ENABLED and _STATUS_LOG_PATH:
            pid = getpid()
            status_json = AzureStatusLogger._get_status_json(
                agent_initialized_successfully, pid, reason
            )
            if not exists(_STATUS_LOG_PATH):
                makedirs(_STATUS_LOG_PATH)
            # Change to be hostname and pid
            status_logger_file_name = f"status_{_MACHINE_NAME}_{pid}.json"
            with open(
                join(_STATUS_LOG_PATH, status_logger_file_name), "w"
            ) as f:
                f.seek(0)
                f.write(dumps(status_json))
                f.truncate()
