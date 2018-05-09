.. toctree::
    :maxdepth: 2
    :hidden:

    applicationinsights

Application Insights SDK for Python
===================================

.. sidebar:: Usage

    Once installed, you can send telemetry to Application Insights. Here are a few samples.

    * :ref:`Sending a simple event telemetry item <usage-sample-01>`
    * :ref:`Sending an event telemetry item with custom properties and measurements <usage-sample-02>`
    * :ref:`Sending a trace telemetry item with custom properties <usage-sample-03>`
    * :ref:`Sending a metric telemetry item <usage-sample-04>`
    * :ref:`Sending an exception telemetry item with custom properties and measurements <usage-sample-05>`
    * :ref:`Configuring context for a telemetry client instance <usage-sample-06>`
    * :ref:`Configuring channel related properties <usage-sample-07>`
    * :ref:`Configuring synchronous (default) channel properties <usage-sample-08>`
    * :ref:`Configuring an asynchronous channel instead of the synchronous default <usage-sample-09>`
    * :ref:`Configuring asynchronous channel properties <usage-sample-10>`
    * :ref:`Basic logging configuration (first option) <usage-sample-11>`
    * :ref:`Basic logging configuration (second option) <usage-sample-12>`
    * :ref:`Advanced logging configuration <usage-sample-13>`
    * :ref:`Logging unhandled exceptions <usage-sample-14>`
    * :ref:`Logging requests <usage-sample-15>`
    * :ref:`Integrating with Django <usage-sample-16>`

This project extends the Application Insights API surface to support Python. `Application
Insights <http://azure.microsoft.com/en-us/services/application-insights/>`__ is a service that allows developers to keep their application available, performing and succeeding. This Python module will allow you to send telemetry of various kinds (event, trace, exception, etc.) to the Application Insights service where they can be visualized in the Azure Portal.

Requirements
------------

Python 2.7 and Python 3.4 are currently supported by this module.

For opening the project in Microsoft Visual Studio you will need `Python Tools for Visual Studio <http://pytools.codeplex.com/>`__.

Installation
------------

To install the latest release you can use `pip <http://www.pip-installer.org/>`__.

::

    $ pip install applicationinsights

Usage
-----

Once installed, you can send telemetry to Application Insights. Here are a few samples.

    **Note**: before you can send data to you will need an instrumentation key. Please see the `Getting an Application Insights
    Instrumentation Key <https://github.com/Microsoft/AppInsights-Home/wiki#getting-an-application-insights-instrumentation-key>`__
    section for more information.

.. _usage-sample-01:

**Sending a simple event telemetry item**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
    tc.track_event("Test event")
    tc.flush()

.. _usage-sample-02:

**Sending an event telemetry item with custom properties and measurements**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
    tc.track_event('Test event', { 'foo': 'bar' }, { 'baz': 42 })
    tc.flush()

.. _usage-sample-03:

**Sending a trace telemetry item with custom properties**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
    tc.track_trace('Test trace', { 'foo': 'bar' })
    tc.flush()

.. _usage-sample-04:

**Sending a metric telemetry item**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
    tc.track_metric('My Metric', 42)
    tc.flush()

.. _usage-sample-05:

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

.. _usage-sample-06:

**Configuring context for a telemetry client instance**

.. code:: python

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

.. _usage-sample-07:

**Configuring channel related properties**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
    # flush telemetry every 30 seconds (assuming we don't hit max_queue_item_count first)
    tc.channel.sender.send_interval_in_milliseconds = 30 * 1000
    # flush telemetry if we have 10 or more telemetry items in our queue
    tc.channel.sender.max_queue_item_count = 10

.. _usage-sample-08:

**Configuring synchronous (default) channel properties**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>')
    # flush telemetry if we have 10 or more telemetry items in our queue
    tc.channel.queue.max_queue_length = 10
    # send telemetry to the service in batches of 5
    tc.channel.sender.send_buffer_size = 5

.. _usage-sample-09:

**Configuring an asynchronous channel instead of the synchronous default**

.. code:: python

    from applicationinsights import TelemetryClient, channel
    sender = channel.AsynchronousSender()
    queue = channel.AsynchronousQueue(sender)
    channel = channel::TelemetryChannel(None, queue)
    tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>', channel)
    # Note: the event will be sent on a separate thread; if the app finishes before
    #       the thread finishes, the data is lost
    tc.track_event('My event')

.. _usage-sample-10:

**Configuring asynchronous channel properties**

.. code:: python

    from applicationinsights import TelemetryClient, channel
    sender = channel.AsynchronousSender()
    queue = channel.AsynchronousQueue(sender)
    channel = channel::TelemetryChannel(None, queue)
    tc = TelemetryClient('<YOUR INSTRUMENTATION KEY GOES HERE>', channel)
    # flush telemetry if we have 10 or more telemetry items in our queue
    tc.channel.queue.max_queue_length = 10
    # send telemetry to the service in batches of 5
    tc.channel.sender.send_buffer_size = 5
    # the background worker thread will be active for 5 seconds before it shuts down. if
    # during this time items are picked up from the queue, the timer is reset.
    tc.channel.sender.send_time = 5
    # the background worker thread will poll the queue every 0.5 seconds for new items
    tc.channel.sender.send_interval = 0.5

.. _usage-sample-11:

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

.. _usage-sample-12:

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

.. _usage-sample-13:

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

.. _usage-sample-14:

**Logging unhandled exceptions**

.. code:: python

    from applicationinsights.exceptions import enable

    # set up exception capture
    enable('<YOUR INSTRUMENTATION KEY GOES HERE>')

    # raise an exception (this will be sent to the Application Insights service as an exception telemetry object)
    raise Exception('Boom!')

.. _usage-sample-15:

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

.. _usage-sample-16:

**Integrating with Django**

Place the following in your `settings.py` file:

.. code:: python

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
        
        # (optional) By default, request names are logged as the fully-qualified
        # name of the view.  To disable this behavior, specify:
        'use_operation_url': True,
        
        # (optional) By default, arguments to views are tracked as custom
        # properties.  To disable this, specify:
        'record_view_arguments': False,
        
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

This will log all requests and exceptions to the instrumentation key
specified in the `APPLICATION_INSIGHTS` setting.  In addition, an
`appinsights` property will be placed on each incoming `request` object in
your views.  This will have the following properties:

* `client`: This is an instance of the :class:`applicationinsights.TelemetryClient` type, which will
  submit telemetry to the same instrumentation key, and will parent each telemetry item to the current
  request.
* `request`: This is the :class:`applicationinsights.channel.contracts.RequestData` instance for the
  current request.  You can modify properties on this object during the handling of the current request.
  It will be submitted when the request has finished.
* `context`: This is the :class:`applicationinsights.channel.TelemetryContext` object for the current
  ApplicationInsights sender.

You can also hook up logging to Django.  For example, to log all builtin
Django warnings and errors, use the following logging configuration in
`settings.py`:

.. code:: python

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

See Django's logging documentation for more information:
https://docs.djangoproject.com/en/1.11/topics/logging/
