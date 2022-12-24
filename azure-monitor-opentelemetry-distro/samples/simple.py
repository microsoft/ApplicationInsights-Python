# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from opentelemetry import trace
from azure.monitor.opentelemetry.distro import configure_opentelemetry

configure_opentelemetry()

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("hello"):
    print("Hello, World!")
