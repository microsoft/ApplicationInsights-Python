# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from azure.monitor.opentelemetry import configure_azure_monitor
from django.http import HttpResponse

# Configure Azure monitor collection telemetry pipeline
configure_azure_monitor(
    connection_string="<your-connection-string>",
    instrumentations=["django"],
    disable_logging=True,
    disable_metrics=True,
    tracing_export_interval_millis=15000,
)


# Requests sent to the django application will be automatically captured
def index(request):
    return HttpResponse("Hello, world.")


# Exceptions that are raised within the request are automatically captured
def exception(request):
    raise Exception("Exception was raised.")
