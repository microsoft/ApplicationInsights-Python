# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from os import environ

from azure.monitor.opentelemetry.distro._diagnostic_logging import (
    AzureDiagnosticLogging,
)
from opentelemetry.environment_variables import (
    OTEL_METRICS_EXPORTER,
    OTEL_TRACES_EXPORTER,
)
from opentelemetry.instrumentation.distro import BaseDistro

_logger = logging.getLogger(__name__)
_opentelemetry_logger = logging.getLogger("opentelemetry")
# TODO: Enabled when duplicate logging issue is solved
# _exporter_logger = logging.getLogger("azure.monitor.opentelemetry.exporter")


class AzureMonitorDistro(BaseDistro):
    def _configure(self, **kwargs) -> None:
        try:
            _configure_auto_instrumentation()
        except Exception as ex:
            _logger.exception(
                ("Error occured auto-instrumenting AzureMonitorDistro")
            )
            raise ex


def _configure_auto_instrumentation() -> None:
    try:
        AzureDiagnosticLogging.enable(_logger)
        AzureDiagnosticLogging.enable(_opentelemetry_logger)
        # TODO: Enabled when duplicate logging issue is solved
        # if _EXPORTER_DIAGNOSTICS_ENABLED:
        #     exporter_logger = logging.getLogger(
        #         "azure.monitor.opentelemetry.exporter"
        #     )
        #     AzureDiagnosticLogging.enable(_exporter_logger)
        # TODO: Uncomment when logging is out of preview
        # environ.setdefault(OTEL_LOGS_EXPORTER,
        #     "azure_monitor_opentelemetry_exporter")
        environ.setdefault(
            OTEL_METRICS_EXPORTER, "azure_monitor_opentelemetry_exporter"
        )
        environ.setdefault(
            OTEL_TRACES_EXPORTER, "azure_monitor_opentelemetry_exporter"
        )
        _logger.info(
            "Azure Monitor OpenTelemetry Distro configured successfully."
        )
    except Exception as exc:
        _logger.error(
            "Azure Monitor OpenTelemetry Distro failed during "
            + f"configuration: {exc}"
        )
        raise exc
