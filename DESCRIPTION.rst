Application Insights for Python
===============================

This project extends the Application Insights API surface to support Python. `Application Insights <http://azure.microsoft.com/en-us/services/application-insights/>`_ is a service that allows developers to keep their application available, performing and succeeding. This Python module will allow you to send telemetry of various kinds (event, trace, exception, etc.) to the Application Insights service where they can be visualized in the Azure Portal.

Requirements
------------

Python >=2.7 and Python >=3.4 are currently supported by this module.

For opening the project in Microsoft Visual Studio you will need `Python Tools for Visual Studio <http://pytools.codeplex.com/>`_.

Installation
------------

To install the latest release you can use `pip <http://www.pip-installer.org/>`_.

::

    $ pip install applicationinsights

Usage
-----

Once installed, you can send telemetry to Application Insights. Here are a few samples.

    **Note**: before you can send data to you will need an instrumentation key. Please see the `Getting an Application Insights Instrumentation Key <https://github.com/Microsoft/AppInsights-Home/wiki#getting-an-application-insights-instrumentation-key>`_ section for more information.

**Sending a simple event telemetry item**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
    tc.track_event("Test event")
    tc.flush()

**Sending an event telemetry item with custom properties and measurements**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
    tc.track_event('Test event', { 'foo': 'bar' }, { 'baz': 42 })
    tc.flush()

**Sending a trace telemetry item with custom properties**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
    tc.track_trace('Test trace', { 'foo': 'bar' })
    tc.flush()

**Sending a metric telemetry item**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
    tc.track_metric('My Metric', 42)
    tc.flush()

**Sending an exception telemetry item with custom properties and measurements**

.. code:: python

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

**Configuring context for a telemetry client instance**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
    tc.context.application.id = 'My application'
    tc.context.application.ver = '1.2.3'
    tc.context.device.id = 'My current device'
    tc.context.device.oem_name = 'Asus'
    tc.context.device.model = 'X31A'
    tc.context.device.type = "Other"
    tc.context.user.id = 'santa@northpole.net'
    tc.track_trace('My trace with context')
    tc.flush()

**Configuring channel related properties**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
    # flush telemetry every 30 seconds (assuming we don't hit max_queue_item_count first)
    tc.channel.sender.send_interval_in_milliseconds = 30 * 1000
    # flush telemetry if we have 10 or more telemetry items in our queue
    tc.channel.sender.max_queue_item_count = 10

**Basic logging configuration (first option)**

.. code:: python

    import logging
    from applicationinsights.logging import enable

    # set up logging
    enable('<YOUR INSTRUMENTATION KEY GOES HERE>')

    # log something (this will be sent to the Application Insights service as a trace)
    logging.info('This is a message')

    # logging shutdown will cause a flush of all un-sent telemetry items
    # alternatively flush manually via handler.flush()

**Basic logging configuration (second option)**

.. code:: python

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

**Advanced logging configuration**

.. code:: python

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

**Logging unhandled exceptions**

.. code:: python

    from applicationinsights.exceptions import enable

    # set up exception capture
    enable('<YOUR INSTRUMENTATION KEY GOES HERE>')

    # raise an exception (this will be sent to the Application Insights service as an exception telemetry object)
    raise Exception('Boom!')

**Logging requests**

.. code:: python

    from flask import Flask
    from applicationinsights.requests import WSGIApplication

    # instantiate the Flask application and wrap its WSGI application
    app = Flask(__name__)
    app.wsgi_app = WSGIApplication('<YOUR INSTRUMENTATION KEY GOES HERE>', app.wsgi_app)

    # define a simple route
    @app.route('/')
    def hello_world():
        return 'Hello World!'

    # run the application
    if __name__ == '__main__':
        app.run()
