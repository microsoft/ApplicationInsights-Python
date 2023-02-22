# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------


import logging

from azure.monitor.opentelemetry.diagnostics._diagnostic_logging import (
    AzureDiagnosticLogging,
)
from opentelemetry.sdk._configuration import _OTelSDKConfigurator

_logger = logging.getLogger(__name__)


class AzureMonitorConfigurator(_OTelSDKConfigurator):
    def _configure(self, **kwargs):
        try:
            AzureDiagnosticLogging.enable(_logger)
            super()._configure(**kwargs)
        except ValueError as e:
            _logger.error(
                f"Azure Monitor Configurator failed during configuration due to a ValueError: {e}"
            )
            raise e
        except Exception as e:
            _logger.error(
                f"Azure Monitor Configurator failed during configuration: {e}"
            )
            raise e
