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

This package is simply a collection of OpenTelemetry and Azure Monitor components bundled together to enable the collection and sending of telemetry to Azure Monitor. For MANUAL instrumentation, it is equivalent to installing the above packages individually. AUTOMATIC instrumentation is not yet supported.

The [Azure Monitor OpenTelemetry exporters][azure_monitor_opentelemetry_exporters] are the main components in accomplishing this. You will be able to use the exporters and their APIs directly through this package. Please go the exporter documentation to understand how OpenTelemetry and Azure Monitor components work in enabling telemetry collection and exporting.

Currently, all instrumentations available in OpenTelemetry are in a beta state, meaning they are not stable and may have breaking changes in the future. Efforts are being made in pushing these to a more stable state.

### Install the package

Install the Azure Monitor Opentelemetry Distro with [pip][pip]:

```Bash
pip install azure-monitor-opentelemetry-distro --pre
```

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
[application_insights_namespace]: https://docs.microsoft.com/azure/azure-monitor/app/
[pip]: https://pypi.org/project/pip/
[ot_python_docs]: https://opentelemetry.io/docs/instrumentation/python/
[ot_sdk_python]: https://github.com/open-telemetry/opentelemetry-python
[opentelemetry_instrumentation_requests]: https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-requests
[opentelemetry_instrumentation_django]: https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-django
[opentelemetry_instrumentation_flask]: https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-flask
[opentelemetry_instrumentation_psycopg2]: https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-psycopg2
[python]: https://www.python.org/downloads/
