# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------


from azure.monitor.opentelemetry.distro._diagnostic_logging import (
    AzureDiagnosticLogging,
)
from opentelemetry.sdk._configuration import _OTelSDKConfigurator


class AzureMonitorConfigurator(_OTelSDKConfigurator):
    def _configure(self, **kwargs):
        try:
            super()._configure(**kwargs)
        except ValueError as e:
            AzureDiagnosticLogging.log_diagnostic_error(
                f"The components failed to initialize due to a ValueError: {e}"
            )
            raise e
        except Exception as e:
            AzureDiagnosticLogging.log_diagnostic_error(
                f"The components failed to initialize: {e}"
            )
            raise e
