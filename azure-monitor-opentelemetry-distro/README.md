# Azure Monitor Opentelemetry Distro

Azure Monitor Distro of [Opentelemetry Python][ot_sdk_python] provides multiple installable components available for an Opentelemetry Azure Monitor monitoring solution. It allows you to instrument your Python applications to capture and report telemetry to Azure Monitor via the Azure monitor exporters.

This distro automatically installs the following libraries:

* [Azure Monitor OpenTelemetry exporters][azure_monitor_opentelemetry_exporters]
* [OpenTelemetry Requests Instrumentation][opentelemetry_instrumentation_requests]
* [OpenTelemetry Flask Instrumentation][opentelemetry_instrumentation_flask]
* [OpenTelemetry Psycopg2 Instrumentation][opentelemetry_instrumentation_psycopg2]

## Getting started

### Install the package

Install the Azure Monitor Opentelemetry Distro with [pip][pip]:

```Bash
pip install azure-monitor-opentelemetry-distro --pre
```

### Prerequisites:
To use this package, you must have:
* Azure subscription - [Create a free account][azure_sub]
* Azure Monitor - [How to use application insights][application_insights_namespace]
* Opentelemetry SDK - [Opentelemtry SDK for Python][ot_sdk_python]
* Python 3.6 or later - [Install Python][python]

### Additional documentation

[Azure Portal][azure_portal]

<!-- LINKS -->
[azure_monitor_opentelemetry_exporters]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/monitor/azure-monitor-opentelemetry-exporter#microsoft-opentelemetry-exporter-for-azure-monitor
[azure_portal]: https://portal.azure.com
[azure_sub]: https://azure.microsoft.com/free/
[application_insights_namespace]: https://docs.microsoft.com/azure/azure-monitor/app/
[pip]: https://pypi.org/project/pip/
[ot_sdk_python]: https://github.com/open-telemetry/opentelemetry-python
[opentelemetry_instrumentation_requests]: https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-requests
[opentelemetry_instrumentation_flask]: https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-flask
[opentelemetry_instrumentation_psycopg2]: https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-psycopg2
[python]: https://www.python.org/downloads/
