.. Application Insights SDK for Python documentation master file, created by
   sphinx-quickstart on Mon Dec 22 23:32:45 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :hidden:

   applicationinsights
   applicationinsights.channel

Application Insights SDK for Python
===================================

    | Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python's elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.
    | -- \ `The Python Tutorial - Introduction <https://docs.python.org/3/tutorial/>`__\ 

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

**Sending a simple event telemetry item**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient()
    tc.context.instrumentation_key = '<YOUR INSTRUMENTATION KEY GOES HERE>'
    tc.track_event("Test event")
    tc.flush()

**Sending an event telemetry item with custom properties and measurements**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient()
    tc.context.instrumentation_key = '<YOUR INSTRUMENTATION KEY GOES HERE>'
    tc.track_event('Test event', { 'foo': 'bar' }, { 'baz': 42 })
    tc.flush()

**Sending a trace telemetry item with custom properties**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient()
    tc.context.instrumentation_key = '<YOUR INSTRUMENTATION KEY GOES HERE>'
    tc.track_trace('Test trace', { 'foo': 'bar' })
    tc.flush()

**Sending a metric telemetry item**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient()
    tc.context.instrumentation_key = '<YOUR INSTRUMENTATION KEY GOES HERE>'
    tc.track_metric('My Metric', 42)
    tc.flush()

**Sending an exception telemetry item with custom properties and measurements**

.. code:: python

    import sys
    from applicationinsights import TelemetryClient
    tc = TelemetryClient()
    tc.context.instrumentation_key = '<YOUR INSTRUMENTATION KEY GOES HERE>'
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
    tc = TelemetryClient()
    tc.context.instrumentation_key = '<YOUR INSTRUMENTATION KEY GOES HERE>'
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
    tc = TelemetryClient()
    # flush telemetry every 30 seconds (assuming we don't hit max_queue_item_count first)
    tc.channel.sender.send_interval_in_milliseconds = 30 * 1000
    # flush telemetry if we have 10 or more telemetry items in our queue
    tc.channel.sender.max_queue_item_count = 10

**Configuring synchronous (default) channel properties**

.. code:: python

    from applicationinsights import TelemetryClient
    tc = TelemetryClient()
    # flush telemetry if we have 10 or more telemetry items in our queue
    tc.channel.queue.max_queue_length = 10
    # send telemetry to the service in batches of 5
    tc.channel.sender.send_buffer_size = 5

**Configuring an asynchronous channel instead of the synchronous default**

.. code:: python

    from applicationinsights import TelemetryClient, channel
    sender = channel.AsynchronousSender()
    queue = channel.AsynchronousQueue(sender)
    channel = channel::TelemetryChannel(None, queue)
    tc = TelemetryClient(channel)
    # Note: the event will be sent on a separate thread; if the app finishes before
    #       the thread finishes, the data is lost
    tc.track_event('My event')

**Configuring asynchronous channel properties**

.. code:: python

    from applicationinsights import TelemetryClient, channel
    sender = channel.AsynchronousSender()
    queue = channel.AsynchronousQueue(sender)
    channel = channel::TelemetryChannel(None, queue)
    tc = TelemetryClient(channel)
    # flush telemetry if we have 10 or more telemetry items in our queue
    tc.channel.queue.max_queue_length = 10
    # send telemetry to the service in batches of 5
    tc.channel.sender.send_buffer_size = 5
    # the background worker thread will be active for 5 seconds before it shuts down. if
    # during this time items are picked up from the queue, the timer is reset.
    tc.channel.sender.send_time = 5
    # the background worker thread will poll the queue every 0.5 seconds for new items
    tc.channel.sender.send_interval = 0.5


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

