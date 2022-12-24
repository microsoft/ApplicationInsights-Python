# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from os import environ

from opentelemetry.environment_variables import (OTEL_METRICS_EXPORTER,
                                                 OTEL_TRACES_EXPORTER)
from opentelemetry.instrumentation.distro import BaseDistro


class AzureMonitorDistro(BaseDistro):
    def _configure(self, **kwargs):
        # TODO: Uncomment when logging is out of preview
        # environ.setdefault(OTEL_LOGS_EXPORTER, "azure_monitor_opentelemetry_exporter")
        environ.setdefault(
            OTEL_METRICS_EXPORTER, "azure_monitor_opentelemetry_exporter"
        )
        environ.setdefault(OTEL_TRACES_EXPORTER, "azure_monitor_opentelemetry_exporter")
