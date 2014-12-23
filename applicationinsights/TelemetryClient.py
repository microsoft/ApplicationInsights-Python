import traceback
import sys
from applicationinsights import channel

NULL_CONSTANT_STRING = 'Null'

class TelemetryClient(object):
    def __init__(self, telemetry_channel=None):
        """Initializes a new instance of the TelemetryClient class."""
        self._context = channel.TelemetryContext()
        self._channel = telemetry_channel or channel.TelemetryChannel()

    @property
    def context(self):
        """Gets the context associated with this telemetry client."""
        return self._context

    @property
    def channel(self):
        """Gets the channel associated with this telemetry client."""
        return self._channel

    def flush(self):
        self._channel.flush()

    def track_pageview(self, name, url, duration=0, properties=None, measurements=None):
        """Send information about the page viewed in the application."""
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
        """Send an ExceptionTelemetry object for display in Diagnostic Search."""
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
        details.message = ''.join(value.args)
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
        """Send an EventTelemetry object for display in Diagnostic Search and aggregation in Metrics Explorer."""
        data = channel.contracts.EventData()
        data.name = name or NULL_CONSTANT_STRING
        if properties:
            data.properties = properties
        if measurements:
            data.measurements = measurements

        self._channel.write(data, self._context)

    def track_metric(self, name, value, type=None, count=None, min=None, max=None, std_dev=None, properties=None):
        """Send a MetricTelemetry object for aggregation in Metric Explorer."""
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
        """Send a trace message for display in Diagnostic Search."""
        data = channel.contracts.MessageData()
        data.message = name or NULL_CONSTANT_STRING
        if properties:
            data.properties = properties

        self._channel.write(data, self._context)
