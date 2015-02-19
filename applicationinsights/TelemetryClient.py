import datetime
import traceback
import sys
import uuid
from applicationinsights import channel

NULL_CONSTANT_STRING = 'Null'

class TelemetryClient(object):
    """The telemetry client used for sending all types of telemetry. It serves as the main entry point for
    interacting with the Application Insights service.
    """
    def __init__(self, instrumentation_key, telemetry_channel=None):
        """Initializes a new instance of the class.

        Args:
            instrumentation_key (str). the instrumentation key to use for this telemetry client.\n
            telemetry_channel (:class:`channel.TelemetryChannel`). the optional telemetry channel to be used instead of
                constructing a default one.
        """
        if instrumentation_key:
            if isinstance(instrumentation_key, channel.TelemetryChannel):
                telemetry_channel = instrumentation_key
                instrumentation_key = None
        else:
            raise Exception('Instrumentation key was required but not provided')
        self._context = channel.TelemetryContext()
        self._context.instrumentation_key = instrumentation_key
        self._channel = telemetry_channel or channel.TelemetryChannel()

    @property
    def context(self):
        """The context associated with this client. All data objects created by this client will be accompanied by
        this value.

        Returns:
            :class:`channel.TelemetryChannel`. the context instance.
        """
        return self._context

    @property
    def channel(self):
        """The channel associated with this telemetry client. All data created by this client will be passed along with
        the :func:`context` object to :class:`channel.TelemetryChannel`'s :func:`write`.

        Returns:
            :class:`channel.TelemetryChannel`. the channel instance.
        """
        return self._channel

    def flush(self):
        """Flushes data in the queue. Data in the queue will be sent either immediately irrespective of what sender is
        being used.
        """
        self._channel.flush()

    def track_pageview(self, name, url, duration=0, properties=None, measurements=None):
        """Send information about the page viewed in the application (a web page for instance).

        Args:
            name (str). the name of the page that was viewed.\n
            url (str). the URL of the page that was viewed.\n
            duration (int). the duration of the page view in milliseconds. (defaults to: 0)\n
            properties (dict). the set of custom properties the client wants attached to this data item. (defaults to: None)\n
            measurements (dict). the set of custom measurements the client wants to attach to this data item. (defaults to: None)
        """
        data = channel.contracts.PageViewData()
        data.name = name or NULL_CONSTANT_STRING
        data.url = url
        data.duration = duration
        if properties:
            data.properties = properties
        if measurements:
            data.measurements = measurements

        self._channel.write(data, self._context)

    def track_exception(self, type=None, value=None, tb=None, properties=None, measurements=None):
        """ Send information about a single exception that occurred in the application.

        Args:
            type (Type). the type of the exception that was thrown.\n
            value (:class:`Exception`). the exception that the client wants to send.\n
            tb (:class:`Traceback`). the traceback information as returned by :func:`sys.exc_info`.\n
            properties (dict). the set of custom properties the client wants attached to this data item. (defaults to: None)\n
            measurements (dict). the set of custom measurements the client wants to attach to this data item. (defaults to: None)
        """
        if not type or not value or not tb:
            type, value, tb = sys.exc_info()

        if not type or not value or not tb:
            try:
                raise Exception(NULL_CONSTANT_STRING)
            except:
                type, value, tb = sys.exc_info()

        details = channel.contracts.ExceptionDetails()
        details.id = 1
        details.outer_id = 0
        details.type_name = type.__name__
        details.message = str(value)
        details.has_full_stack = True
        counter = 0
        for tb_frame_file, tb_frame_line, tb_frame_function, tb_frame_text in traceback.extract_tb(tb):
            frame = channel.contracts.StackFrame()
            frame.assembly = 'Unknown'
            frame.file_name = tb_frame_file
            frame.level = counter
            frame.line = tb_frame_line
            frame.method = tb_frame_function
            details.parsed_stack.append(frame)
            counter += 1
        details.parsed_stack.reverse()

        data = channel.contracts.ExceptionData()
        data.handled_at = 'UserCode'
        data.exceptions.append(details)
        if properties:
            data.properties = properties
        if measurements:
            data.measurements = measurements

        self._channel.write(data, self._context)

    def track_event(self, name, properties=None, measurements=None):
        """ Send information about a single event that has occurred in the context of the application.

        Args:
            name (str). the data to associate to this event.\n
            properties (dict). the set of custom properties the client wants attached to this data item. (defaults to: None)\n
            measurements (dict). the set of custom measurements the client wants to attach to this data item. (defaults to: None)
        """
        data = channel.contracts.EventData()
        data.name = name or NULL_CONSTANT_STRING
        if properties:
            data.properties = properties
        if measurements:
            data.measurements = measurements

        self._channel.write(data, self._context)

    def track_metric(self, name, value, type=None, count=None, min=None, max=None, std_dev=None, properties=None):
        """Send information about a single metric data point that was captured for the application.

        Args:
            name (str). the name of the metric that was captured.\n
            value (float). the value of the metric that was captured.\n
            type (:class:`channel.contracts.DataPointType`). the type of the metric. (defaults to: :func:`channel.contracts.DataPointType.aggregation`)\n
            count (int). the number of metrics that were aggregated into this data point. (defaults to: None)\n
            min (float). the minimum of all metrics collected that were aggregated into this data point. (defaults to: None)\n
            max (float). the maximum of all metrics collected that were aggregated into this data point. (defaults to: None)\n
            std_dev (float). the standard deviation of all metrics collected that were aggregated into this data point. (defaults to: None)\n
            properties (dict). the set of custom properties the client wants attached to this data item. (defaults to: None)
        """
        dataPoint = channel.contracts.DataPoint()
        dataPoint.name = name or NULL_CONSTANT_STRING
        dataPoint.value = value or 0
        dataPoint.kind = type or channel.contracts.DataPointType.aggregation
        dataPoint.count = count
        dataPoint.min = min
        dataPoint.max = max
        dataPoint.std_dev = std_dev
        
        data = channel.contracts.MetricData()
        data.metrics.append(dataPoint)
        if properties:
            data.properties = properties

        self._channel.write(data, self._context)

    def track_trace(self, name, properties=None):
        """Sends a single trace statement.

        Args:
            name (str). the trace statement.\n
            properties (dict). the set of custom properties the client wants attached to this data item. (defaults to: None)
        """
        data = channel.contracts.MessageData()
        data.message = name or NULL_CONSTANT_STRING
        if properties:
            data.properties = properties

        self._channel.write(data, self._context)

    def track_request(self, name, url, success, start_time=None, duration=None, response_code=None, http_method=None, properties=None, measurements=None):
        """Sends a single request that was captured for the application.

        Args:
            name (str). the name for this request. All requests with the same name will be grouped together.\n
            url (str). the actual URL for this request (to show in individual request instances).\n
            success (bool). true if the request ended in success, false otherwise.\n
            start_time (str). the start time of the request. The value should look the same as the one returned by :func:`datetime.isoformat()` (defaults to: None)\n
            duration (int). the number of milliseconds that this request lasted. (defaults to: None)\n
            response_code (string). the response code that this request returned. (defaults to: None)\n
            http_method (string). the HTTP method that triggered this request. (defaults to: None)\n
            properties (dict). the set of custom properties the client wants attached to this data item. (defaults to: None)\n
            measurements (dict). the set of custom measurements the client wants to attach to this data item. (defaults to: None)
        """
        data = channel.contracts.RequestData()
        data.id = str(uuid.uuid4())
        data.name = name
        data.start_time = start_time or datetime.datetime.utcnow().isoformat() + 'Z'

        local_duration = duration or 0
        duration_parts = []
        for multiplier in [1000, 60, 60, 24]:
            duration_parts.append(local_duration % multiplier)
            local_duration //= multiplier

        duration_parts.reverse()
        data.duration = '%02d:%02d:%02d.%03d' % tuple(duration_parts)
        if local_duration:
            data.duration = '%d.%s' % (local_duration, data.duration)

        data.response_code = response_code or '200'
        data.success = success
        data.http_method = http_method or 'GET'
        data.url = url
        if properties:
            data.properties = properties
        if measurements:
            data.measurements = measurements

        self.channel.write(data, self._context)

