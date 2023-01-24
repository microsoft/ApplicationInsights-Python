# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

import logging
import threading
from os import makedirs
from os.path import exists, join

from azure.monitor.opentelemetry.distro._constants import (
    _EXTENSION_VERSION,
    _IS_DIAGNOSTICS_ENABLED,
    ConnectionStringConstants,
    _env_var_or_default,
    _get_log_path,
)
from azure.monitor.opentelemetry.distro._version import VERSION

_DIAGNOSTIC_LOGGER_FILE_NAME = "applicationinsights-extension.log"
_SITE_NAME = _env_var_or_default("WEBSITE_SITE_NAME")
_SUBSCRIPTION_ID_ENV_VAR = _env_var_or_default("WEBSITE_OWNER_NAME")
_SUBSCRIPTION_ID = (
    _SUBSCRIPTION_ID_ENV_VAR.split("+")[0]
    if _SUBSCRIPTION_ID_ENV_VAR
    else None
)
_logger = logging.getLogger(__name__)
_DIAGNOSTIC_LOG_PATH = _get_log_path()


class AzureDiagnosticLogging:
    _initialized = False
    _lock = threading.Lock()
    _f_handler = None

    def _initialize():
        with AzureDiagnosticLogging._lock:
            if not AzureDiagnosticLogging._initialized:
                if _IS_DIAGNOSTICS_ENABLED and _DIAGNOSTIC_LOG_PATH:
                    customer_ikey = (
                        ConnectionStringConstants.get_customer_ikey()
                    )
                    if customer_ikey is None:
                        try:
                            ConnectionStringConstants.set_conn_str_from_env_var()
                            customer_ikey = (
                                ConnectionStringConstants.get_customer_ikey()
                            )
                        except ValueError as e:
                            _logger.error(
                                "Failed to parse Instrumentation Key: %s" % e
                            )
                            customer_ikey = "unknown"
                    format = (
                        "{"
                        + '"time":"%(asctime)s.%(msecs)03d", '
                        + '"level":"%(levelname)s", '
                        + '"logger":"%(name)s", '
                        + '"message":"%(message)s", '
                        + '"properties":{'
                        + '"operation":"Startup", '
                        + f'"sitename":"{_SITE_NAME}", '
                        + f'"ikey":"{customer_ikey}", '
                        + f'"extensionVersion":"{_EXTENSION_VERSION}", '
                        + f'"sdkVersion":"{VERSION}", '
                        + f'"subscriptionId":"{_SUBSCRIPTION_ID}", '
                        + '"language":"python"'
                        + "}"
                        + "}"
                    )
                    if not exists(_DIAGNOSTIC_LOG_PATH):
                        makedirs(_DIAGNOSTIC_LOG_PATH)
                    AzureDiagnosticLogging._f_handler = logging.FileHandler(
                        join(
                            _DIAGNOSTIC_LOG_PATH, _DIAGNOSTIC_LOGGER_FILE_NAME
                        )
                    )
                    formatter = logging.Formatter(
                        fmt=format, datefmt="%Y-%m-%dT%H:%M:%S"
                    )
                    AzureDiagnosticLogging._f_handler.setFormatter(formatter)
                    AzureDiagnosticLogging._initialized = True
                    _logger.info("Initialized Azure Diagnostic Logger.")

    def enable(logger: logging.Logger):
        AzureDiagnosticLogging._initialize()
        if AzureDiagnosticLogging._initialized:
            if AzureDiagnosticLogging._f_handler in logger.handlers:
                _logger.info(
                    "Azure diagnostics already enabled for %s logger."
                    % logger.name
                )
            else:
                logger.addHandler(AzureDiagnosticLogging._f_handler)
                _logger.info(
                    "Added Azure diagnostics logging to %s." % logger.name
                )
