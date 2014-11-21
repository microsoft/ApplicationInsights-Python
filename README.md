# Application Insights for Python #

>Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python's elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.
> -- <cite>[The Python Tutorial - Introduction](https://docs.python.org/3/tutorial/)</cite>

This project extends the Application Insights API surface to support Python. [Application Insights](http://azure.microsoft.com/en-us/services/application-insights/) is a service that allows developers to keep their application available, performing and succeeding. This Python module will allow you to send telemetry of various kinds (event, trace, exception, etc.) to the Application Insights service where they can be visualized in the Azure Portal. 


## Requirements ##

Python 2.7 and Python 3.4 are currently supported by this module. 

For opening the project in Microsoft Visual Studio you will need [Python Tools for Visual Studio](http://pytools.codeplex.com/).

## Installation ##

To install the latest release you can use [pip](http://www.pip-installer.org/).

```
$ pip install applicationinsights
```

## Usage ##

Once installed, you can send telemetry to Application Insights. Here are a few samples.

>**Note**: before you can send data to you will need an instrumentation key. Please see the **Getting an Application Insights Instrumentation Key** section for more information.


**Sending a simple event telemetry item**
```python
from applicationinsights import TelemetryClient
tc = TelemetryClient()
tc.context.instrumentationKey = "<YOUR INSTRUMENTATION KEY GOES HERE>"
tc.trackEvent("Test event")
```

**Sending an event telemetry item with custom properties and measurements**
```python
from applicationinsights import TelemetryClient
tc = TelemetryClient()
tc.context.instrumentationKey = "<YOUR INSTRUMENTATION KEY GOES HERE>"
tc.trackEvent("Test event", { "foo": "bar" }, { "baz": 42 })
```

**Sending a trace telemetry item with custom properties**
```python
from applicationinsights import TelemetryClient
tc = TelemetryClient()
tc.context.instrumentationKey = "<YOUR INSTRUMENTATION KEY GOES HERE>"
tc.trackTrace("Test trace", { "foo": "bar" })
```  

**Sending a metric telemetry item**
```python
from applicationinsights import TelemetryClient
tc = TelemetryClient()
tc.context.instrumentationKey = "<YOUR INSTRUMENTATION KEY GOES HERE>"
tc.trackMetric("My Metric", 42)
``` 

**Sending an exception telemetry item with custom properties and measurements**
```python
from applicationinsights import TelemetryClient
tc = TelemetryClient()
tc.context.instrumentationKey = "<YOUR INSTRUMENTATION KEY GOES HERE>"
try:
    raise Exception("blah")
except Exception as e:
    tc.trackException(e, { "foo": "bar" }, { "x": 42 })
```  

**Configuring context for a telemetry client instance**
```python
from applicationinsights import TelemetryClient
tc = TelemetryClient()
tc.context.instrumentationKey = "<YOUR INSTRUMENTATION KEY GOES HERE>"
tc.context.application.id = "My application"
tc.context.application.ver = "1.2.3"
tc.context.device.id = "My current device"
tc.context.device.oemName = "Asus"
tc.context.device.model = "X31A"
tc.context.device.type = "Other"
tc.context.user.id = "santa@northpole.net"
tc.trackTrace("My trace with context")
```  

**Configuring channel related properties**
```python
from applicationinsights import TelemetryClient
tc = TelemetryClient()
# flush telemetry every 30 seconds (assuming we don't hit maxQueueItemCount first)
tc.channel.sender.sendIntervalInMilliseconds = 30 * 1000
# flush telemetry if we have 10 or more telemetry items in our queue
tc.channel.sender.maxQueueItemCount = 10
```

## Getting an Application Insights Instrumentation Key ##

To successfully send data to the Application Insights service, you will need an Application Insights resource's instrumentation key. Here is how you get a new one.

1. Log into the [Microsoft Azure portal](https://portal.azure.com/)

2. Create a new Application Insights resource in the by clicking `New -> Application Insights`.

<center><img src="http://i.imgur.com/jieq59h.png" width="300" /></center><br/><br/>
3. Enter a name for your new Application Insights resource and click create. A new tile will appear on your dashboard. 

<center><img src="http://i.imgur.com/XIMABul.png" width="600" /></center><br/><br/>
4. Expand your resource by clicking on the tile on your dashboard, then click on the Properties tile to open your resource's properties blade. You can copy the instrumentation key from here.

<center><img src="http://i.imgur.com/i1OzJVP.png" width="700" /></center><br/><br/>



