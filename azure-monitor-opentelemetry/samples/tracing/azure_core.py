from os import environ

from azure.core.settings import settings
from azure.core.tracing.ext.opentelemetry_span import OpenTelemetrySpan
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry.sdk import trace

# Declare OpenTelemetry as enabled tracing plugin for Azure SDKs
settings.tracing_implementation = OpenTelemetrySpan

# Set up exporting to Azure Monitor
configure_azure_monitor()

# Example with Storage SDKs

from azure.storage.blob import BlobServiceClient

tracer = trace.get_tracer(__name__)
with tracer.start_as_current_span(name="MyApplication"):
    client = BlobServiceClient.from_connection_string(
        environ["AZURE_STORAGE_ACCOUNT_CONNECTION_STRING"]
    )
    client.create_container("mycontainer")  # Call will be traced
