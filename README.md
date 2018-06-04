# Application Insights for Python #

[![Build Status](https://travis-ci.org/Microsoft/ApplicationInsights-Python.svg?branch=master)](https://travis-ci.org/Microsoft/ApplicationInsights-Python) 
[![PyPI version](https://badge.fury.io/py/applicationinsights.svg)](http://badge.fury.io/py/applicationinsights)

This project extends the Application Insights API surface to support Python. [Application Insights](http://azure.microsoft.com/en-us/services/application-insights/) is a service that allows developers to keep their application available, performing and succeeding. This Python module will allow you to send telemetry of various kinds (event, trace, exception, etc.) to the Application Insights service where they can be visualized in the Azure Portal. 


## Requirements ##

Python >=2.7 and Python >=3.4 are currently supported by this module. 

## Installation ##

To install the latest release you can use [pip](http://www.pip-installer.org/).

```
$ pip install applicationinsights
```

## Usage ##

Once installed, you can send telemetry to Application Insights. Here are a few samples.

>**Note**: before you can send data to you will need an instrumentation key. Please see the [Getting an Application Insights Instrumentation Key](https://github.com/Microsoft/AppInsights-Home/wiki#getting-an-application-insights-instrumentation-key) section for more information.


**Sending a simple event telemetry item**
```python
from applicationinsights import TelemetryClient
tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
tc.track_event('Test event')
tc.flush()
```

**Sending an event telemetry item with custom properties and measurements**
```python
from applicationinsights import TelemetryClient
tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
tc.track_event('Test event', { 'foo': 'bar' }, { 'baz': 42 })
tc.flush()
```

**Sending a trace telemetry item with custom properties**
```python
from applicationinsights import TelemetryClient
tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
tc.track_trace('Test trace', { 'foo': 'bar' })
tc.flush()
```  

**Sending a metric telemetry item**
```python
from applicationinsights import TelemetryClient
tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
tc.track_metric('My Metric', 42)
tc.flush()
``` 

**Sending an exception telemetry item with custom properties and measurements**
```python
import sys
from applicationinsights import TelemetryClient
tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
try:
    raise Exception('blah')
except:
    tc.track_exception()

try:
    raise Exception("blah")
except:
    tc.track_exception(*sys.exc_info(), properties={ 'foo': 'bar' }, measurements={ 'x': 42 })
tc.flush()
```  

**Configuring context for a telemetry client instance**
```python
from applicationinsights import TelemetryClient
tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
tc.context.application.ver = '1.2.3'
tc.context.device.id = 'My current device'
tc.context.device.oem_name = 'Asus'
tc.context.device.model = 'X31A'
tc.context.device.type = "Other"
tc.context.user.id = 'santa@northpole.net'
tc.track_trace('My trace with context')
tc.flush()
```  

**Configuring channel related properties**
```python
from applicationinsights import TelemetryClient
tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
# flush telemetry every 30 seconds (assuming we don't hit max_queue_item_count first)
tc.channel.sender.send_interval_in_milliseconds = 30 * 1000
# flush telemetry if we have 10 or more telemetry items in our queue
tc.channel.sender.max_queue_item_count = 10
```

**Basic logging configuration (first option)**
```python
import logging
from applicationinsights.logging import enable

# set up logging
enable('<YOUR INSTRUMENTATION KEY GOES HERE>')

# log something (this will be sent to the Application Insights service as a trace)
logging.info('This is a message')

# logging shutdown will cause a flush of all un-sent telemetry items
# alternatively flush manually via handler.flush()
```

**Basic logging configuration (second option)**
```python
import logging
from applicationinsights.logging import LoggingHandler

# set up logging
handler = LoggingHandler('<YOUR INSTRUMENTATION KEY GOES HERE>')
logging.basicConfig(handlers=[ handler ], format='%(levelname)s: %(message)s', level=logging.DEBUG)

# log something (this will be sent to the Application Insights service as a trace)
logging.debug('This is a message')

try:
    raise Exception('Some exception')
except:
    # this will send an exception to the Application Insights service
    logging.exception('Code went boom!')

# logging shutdown will cause a flush of all un-sent telemetry items
# alternatively flush manually via handler.flush()
```

**Advanced logging configuration**
```python
import logging
from applicationinsights.logging import LoggingHandler

# set up logging
handler = LoggingHandler('<YOUR INSTRUMENTATION KEY GOES HERE>')
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
my_logger = logging.getLogger('simple_logger')
my_logger.setLevel(logging.DEBUG)
my_logger.addHandler(handler)

# log something (this will be sent to the Application Insights service as a trace)
my_logger.debug('This is a message')

# logging shutdown will cause a flush of all un-sent telemetry items
# alternatively flush manually via handler.flush()
```

**Logging unhandled exceptions**
```python
from applicationinsights.exceptions import enable

# set up exception capture
enable('<YOUR INSTRUMENTATION KEY GOES HERE>')

# raise an exception (this will be sent to the Application Insights service as an exception telemetry object)
raise Exception('Boom!')
```

**Integrating with Flask**
```python
from flask import Flask
from applicationinsights.flask.ext import AppInsights

# instantiate the Flask application
app = Flask(__name__)
app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = '<YOUR INSTRUMENTATION KEY GOES HERE>'

# log requests, traces and exceptions to the Application Insights service
appinsights = AppInsights(app)

# define a simple route
@app.route('/')
def hello_world():
    return 'Hello World!'

# run the application
if __name__ == '__main__':
    app.run()
```

**Integrating with Django**

Place the following in your `settings.py` file:

```python
# If on Django < 1.10
MIDDLEWARE_CLASSES = [
    # ... or whatever is below for you ...
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # ... or whatever is above for you ...
    'applicationinsights.django.ApplicationInsightsMiddleware',   # Add this middleware to the end
]

# If on Django >= 1.10
MIDDLEWARE = [
    # ... or whatever is below for you ...
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # ... or whatever is above for you ...
    'applicationinsights.django.ApplicationInsightsMiddleware',   # Add this middleware to the end
]

APPLICATION_INSIGHTS = {
    # (required) Your Application Insights instrumentation key
    'ikey': "00000000-0000-0000-0000-000000000000",
    
    # (optional) By default, request names are logged as the request method
    # and relative path of the URL.  To log the fully-qualified view names
    # instead, set this to True.  Defaults to False.
    'use_view_name': True,
    
    # (optional) To log arguments passed into the views as custom properties,
    # set this to True.  Defaults to False.
    'record_view_arguments': True,
    
    # (optional) Exceptions are logged by default, to disable, set this to False.
    'log_exceptions': False,
    
    # (optional) Events are submitted to Application Insights asynchronously.
    # send_interval specifies how often the queue is checked for items to submit.
    # send_time specifies how long the sender waits for new input before recycling
    # the background thread.
    'send_interval': 1.0, # Check every second
    'send_time': 3.0, # Wait up to 3 seconds for an event
    
    # (optional, uncommon) If you must send to an endpoint other than the
    # default endpoint, specify it here:
    'endpoint': "https://dc.services.visualstudio.com/v2/track",
}
```

This will log all requests and exceptions to the instrumentation key
specified in the `APPLICATION_INSIGHTS` setting.  In addition, an
`appinsights` property will be placed on each incoming `request` object in
your views.  This will have the following properties:

* `client`: This is an instance of the `applicationinsights.TelemetryClient`
  type, which will submit telemetry to the same instrumentation key, and
  will parent each telemetry item to the current request.
* `request`: This is the `applicationinsights.channel.contracts.RequestData`
  instance for the current request.  You can modify properties on this
  object during the handling of the current request.  It will be submitted
  when the request has finished.
* `context`: This is the `applicationinsights.channel.TelemetryContext`
  object for the current ApplicationInsights sender.

You can also hook up logging to Django.  For example, to log all builtin
Django warnings and errors, use the following logging configuration in
`settings.py`:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # The application insights handler is here
        'appinsights': {
            'class': 'applicationinsights.django.LoggingHandler',
            'level': 'WARNING'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['appinsights'],
            'level': 'WARNING',
            'propagate': True,
        }
    }
}
```

See Django's [logging documentation](https://docs.djangoproject.com/en/1.11/topics/logging/)
for more information.

**Integrating with other web frameworks**

For any other Python web framework that is [WSGI compliant](https://www.python.org/dev/peps/pep-0333/),
the [WSGIApplication](https://github.com/Microsoft/ApplicationInsights-Python/blob/master/applicationinsights/requests/WSGIApplication.py)
can be used as a middleware to log requests to Application Insights.

Add common properties to WSGIApplication request events by passing in a dictionary to the WSGIApplication constructor:
```
from flask import Flask
from applicationinsights.requests import WSGIApplication

# instantiate the Flask application and wrap its WSGI application
app = Flask(__name__)

# Construct dictionary which contains properties to be included with every request event
common_properties = {
    "service": "hello_world_flask_app",
    "environment": "production"
}

app.wsgi_app = WSGIApplication('<YOUR INSTRUMENTATION KEY GOES HERE>', app.wsgi_app, common_properties=common_properties)

# define a simple route
@app.route('/')
def hello_world():
    return 'Hello World!'

# run the application
if __name__ == '__main__':
    app.run()
```