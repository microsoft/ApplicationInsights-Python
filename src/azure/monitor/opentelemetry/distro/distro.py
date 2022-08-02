# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from os import environ
from opentelemetry.instrumentation.distro import BaseDistro
from opentelemetry.environment_variables import OTEL_LOGS_EXPORTER, OTEL_METRICS_EXPORTER, OTEL_TRACES_EXPORTER

class AzureMonitorDistro(BaseDistro):
    def _configure(self, **kwargs):
        environ.setdefault(OTEL_LOGS_EXPORTER, "otlp_proto_grpc")
        environ.setdefault(OTEL_METRICS_EXPORTER, "otlp_proto_grpc")
        environ.setdefault(OTEL_TRACES_EXPORTER, "otlp_proto_grpc")