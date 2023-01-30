# Azure Monitor Opentelemetry Distro

Azure Monitor Distro of [Opentelemetry Python][ot_sdk_python] provides multiple installable components available for an Opentelemetry Azure Monitor monitoring solution. It allows you to instrument your Python applications to capture and report telemetry to Azure Monitor via the Azure monitor exporters.

This distro automatically installs the following libraries:

* [Azure Monitor OpenTelemetry exporters][azure_monitor_opentelemetry_exporters]
* [OpenTelemetry Requests Instrumentation][opentelemetry_instrumentation_requests]
* [OpenTelemetry Django Instrumentation][opentelemetry_instrumentation_django]
* [OpenTelemetry Flask Instrumentation][opentelemetry_instrumentation_flask]
* [OpenTelemetry Psycopg2 Instrumentation][opentelemetry_instrumentation_psycopg2]

## Getting started

### Key Concepts

This package bundles a series of OpenTelemetry and Azure Monitor components to enable the collection and sending of telemetry to Azure Monitor. For MANUAL instrumentation, use the `configure_azure_monitor` function. AUTOMATIC instrumentation is not yet supported.

The [Azure Monitor OpenTelemetry exporters][azure_monitor_opentelemetry_exporters] are the main components in accomplishing this. You will be able to use the exporters and their APIs directly through this package. Please go the exporter documentation to understand how OpenTelemetry and Azure Monitor components work in enabling telemetry collection and exporting.

Currently, all instrumentations available in OpenTelemetry are in a beta state, meaning they are not stable and may have breaking changes in the future. Efforts are being made in pushing these to a more stable state.

### Install the package

Install the Azure Monitor Opentelemetry Distro with [pip][pip]:

```Bash
pip install azure-monitor-opentelemetry-distro --pre
```

### Usage

You can use `configure_azure_monitor` to set up instrumentation for your app to Azure Monitor. `configure_azure_monitor` supports the following optional arguments:

* connection_string - The [connection string][connection_string_doc] for your Application Insights resource. The connection string will be automatically populated from the `APPLICATIONINSIGHTS_CONNECTION_STRING` environment variable if not explicitly passed in.
* instrumentations - Specifies the libraries with [instrumentations][ot_instrumentations] that you would like to use. Accepts a comma separated list. e.g. `["requests", "flask"]`
* service_name - Specifies the [service][service_semantic_convention_doc] name.
* service_namespace - Specifies the [service][service_semantic_convention_doc] namespace.
* service_instance_id - Specifies the [service][service_semantic_convention_doc] instance id.
* disable_logging - If set to `True`, disables collection and export of logging telemetry.
* disable_metrics - If set to `True`, disables collection and export of metric telemetry.
* disable_tracing - If set to `True`, disables collection and export of distributed tracing telemetry.
* logging_level - Specifies the [logging level][logging_level] of the Opentelemetry Logging Handler. Ex: logging.WARNING.
* logger_name = Specifies the [logger name][logger_name_hierarchy_doc] under which all logging will be instrumented. Defaults to "" which corresponds to the root logger.
* logging_export_interval_millis - Specifies the logging export interval in milliseconds. Defaults to 30,000.
* views - Specifies the list of [views][opentelemetry_specification_view] to configure for the metric pipeline. See [here][ot_sdk_python_view_examples] for example usage.
* sampling_ratio - Specifies the ratio of distributed tracing telemetry to be [sampled][application_insights_sampling]. Accepted values are in the range [0,1]. Defaults to 1.0, meaning no telemetry is sampled out.
* tracing_export_interval_millis - Specifies the distributed tracing export interval in milliseconds. Defaults to 30,000.

See additional [configuration related to exporting here][exporter_configuration_docs].

### Prerequisites:

To use this package, you must have:

* Azure subscription - [Create a free account][azure_sub]
* Azure Monitor - [How to use application insights][application_insights_namespace]
* Opentelemetry SDK - [Opentelemetry SDK for Python][ot_sdk_python]
* Python 3.7 or later - [Install Python][python]

### Additional documentation

[Azure Portal][azure_portal]
[OpenTelemetry Python Official Docs][ot_python_docs]

<!-- LINKS -->
[azure_monitor_opentelemetry_exporters]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/monitor/azure-monitor-opentelemetry-exporter#microsoft-opentelemetry-exporter-for-azure-monitor
[azure_portal]: https://portal.azure.com
[azure_sub]: https://azure.microsoft.com/free/
[application_insights_namespace]: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview
[application_insights_sampling]: https://learn.microsoft.com/en-us/azure/azure-monitor/app/sampling
[connection_string_doc]: https://learn.microsoft.com/en-us/azure/azure-monitor/app/sdk-connection-string
[exporter_configuration_docs]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/monitor/azure-monitor-opentelemetry-exporter#configuration
[logging_level]: https://docs.python.org/3/library/logging.html#levels
[logger_name_hierarchy_doc]: https://docs.python.org/3/library/logging.html#logger-objects
[ot_instrumentations]: https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation
[ot_python_docs]: https://opentelemetry.io/docs/instrumentation/python/
[ot_sdk_python]: https://github.com/open-telemetry/opentelemetry-python
[ot_sdk_python_view_examples]: https://github.com/open-telemetry/opentelemetry-python/tree/main/docs/examples/metrics/views
[opentelemetry_instrumentation_requests]: https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-requests
[opentelemetry_instrumentation_django]: https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-django
[opentelemetry_instrumentation_flask]: https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-flask
[opentelemetry_instrumentation_psycopg2]: https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-psycopg2
[opentelemetry_specification_view]: https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/sdk.md#view
[python]: https://www.python.org/downloads/
[pip]: https://pypi.org/project/pip/
[service_semantic_convention_doc]: https://github.com/open-telemetry/opentelemetry-specification/tree/main/specification/resource/semantic_conventions#service