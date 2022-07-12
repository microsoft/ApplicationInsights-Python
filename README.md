# Azure Monitor Opentelemetry Distro

Azure Monitor Distro of [Opentelemetry Python][opentelemetry-python] provides multiple installable components available for an Opentelemetry Azure Monitor monitoring solution. It allows you to instrument your Python applications to capture and report telemetry to Azure Monitor via the Azure monitor exporters.

This distro automatically installs the following libraries:

* [Azure Monitor OpenTelemetry exporters][azure_monitor_opentelemetry_exporters]

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
[python]: https://www.python.org/downloads/
