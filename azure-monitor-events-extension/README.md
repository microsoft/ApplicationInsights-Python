# Azure Monitor Events Extension

The Azure Monitor Events Extension allows users to send custom events to Application Insights in conjunction with the [Azure Monitor OpenTelemetry Distro](https://learn.microsoft.com/azure/azure-monitor/app/opentelemetry-enable?tabs=python).

## Install the package

Install the `Azure Monitor OpenTelemetry Distro` and `Azure Monitor Events Extension`:

```Bash
pip install azure-monitor-opentelemetry
pip install azure-monitor-events-extension --pre
```

## Samples

Check out the [samples](https://github.com/microsoft/ApplicationInsights-Python/tree/main/azure-monitor-events-extension/samples) page to see how to use the events extention with the distro.

## Additional documentation

* [Azure Portal][azure_portal]
* [Official Azure monitor docs][azure_monitor_opentelemetry]
* [OpenTelemetry Python Official Docs][ot_python_docs]

<!-- LINKS -->
[azure_portal]: https://portal.azure.com
[azure_monitor_opentelemetry]: https://learn.microsoft.com/azure/azure-monitor/app/opentelemetry-enable?tabs=python
[ot_python_docs]: https://opentelemetry.io/docs/instrumentation/python/
