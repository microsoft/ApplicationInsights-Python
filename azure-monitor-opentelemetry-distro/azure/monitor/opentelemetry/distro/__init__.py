# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------
import importlib
import logging

from typing import Any, Dict
from azure.monitor.opentelemetry.distro.util import get_configurations
from azure.monitor.opentelemetry.exporter import (
    ApplicationInsightsSampler,
    AzureMonitorTraceExporter,
)
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.semconv.resource import ResourceAttributes

_logger = logging.getLogger(__name__)


_SUPPORTED_INSTRUMENTED_LIBRARIES = {
    "django",
    "flask",
    "psycopg2",
    "requests",
}


def configure_azure_monitor(**kwargs):
    """
    This function works as a configuration layer that allows the
    end user to configure OpenTelemetry and Azure monitor components. The
    configuration can be done via arguments passed to this function.
    """

    configurations = get_configurations(**kwargs)

    # Setup tracing pipeline
    _setup_tracing(configurations, **kwargs)

    # Setup instrumentations
    # Instrumentations need to be setup last so to use the global providers
    # instanstiated in the other setup steps
    _setup_instrumentations(configurations.get("instrumentations", []))


def _setup_instrumentations(instrumentations: Dict[str, str]):
    for lib_name in instrumentations:
        if lib_name in _SUPPORTED_INSTRUMENTED_LIBRARIES:
                try:
                    importlib.import_module(lib_name)
                except ImportError as ex:
                    _logger.warning(
                        "Unable to import %s. Please make sure it is installed.",
                        lib_name
                    )
                    continue
                instr_lib_name = "opentelemetry.instrumentation." + lib_name
                try:
                    module = importlib.import_module(instr_lib_name)
                    instrumentor_name = "{}Instrumentor".format(
                        lib_name.capitalize()
                    )
                    class_ = getattr(module, instrumentor_name)
                    class_().instrument()
                except ImportError:
                    _logger.warning(
                        "Unable to import %s. Please make sure it is installed.",
                        instr_lib_name
                    )
                except Exception as ex:
                    _logger.warning(
                        "Exception occured when instrumenting: %s.", lib_name, exc_info=ex)
                finally:
                    continue
        else:
            _logger.warning("Instrumentation not supported for library: %s.", lib_name)


def _setup_tracing(configurations: Dict[str, Any], **kwargs: Dict[Any, Any]):
    disable_tracing = configurations.get("disable_tracing", False)

    if not disable_tracing:
        service_name = configurations.get("service_name", "")
        service_namespace = configurations.get("service_namespace", "")
        service_instance_id = configurations.get("service_instance_id", "")
        sampling_ratio = configurations.get("sampling_ratio", 1.0)
        tracing_export_interval_millis = configurations.get(
            "tracing_export_interval_millis", 30000
        )
        resource = Resource.create(
            {
                ResourceAttributes.SERVICE_NAME: service_name,
                ResourceAttributes.SERVICE_NAMESPACE: service_namespace,
                ResourceAttributes.SERVICE_INSTANCE_ID: service_instance_id,
            }
        )
        tracer_provider = TracerProvider(
            sampler=ApplicationInsightsSampler(sampling_ratio=sampling_ratio),
            resource=resource,
        )
        trace.set_tracer_provider(tracer_provider)
        exporter = AzureMonitorTraceExporter(**kwargs)
        span_processor = BatchSpanProcessor(
            exporter,
            export_timeout_millis=tracing_export_interval_millis,
        )
        trace.get_tracer_provider().add_span_processor(span_processor)
