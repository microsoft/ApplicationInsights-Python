import traceback
from applicationinsights import channel

NULL_CONSTANT_STRING = "Null"

class TelemetryClient(object):
    def __init__(self, telemetryChannel=None):
        """Initializes a new instance of the TelemetryClient class."""
        self.__context = channel.TelemetryContext()
        self.__channel = telemetryChannel
        if not self.__channel or not isinstance(self.__channel, channel.TelemetryChannel):
            self.__channel = channel.TelemetryChannel()

    @property
    def context(self):
        """Gets the context associated with this telemetry client."""
        return self.__context

    @property
    def channel(self):
        """Gets the channel associated with this telemetry client."""
        return self.__channel

    def trackPageView(self, name, url, duration=0, properties=None, measurements=None):
        """Send information about the page viewed in the application."""
        pageViewData = channel.contracts.PageViewTelemetry()
        if not name:
            name = NULL_CONSTANT_STRING
        pageViewData.name = name
        pageViewData.url = url
        pageViewData.duration = duration
        pageViewData.properties = properties
        pageViewData.measurements = measurements

        self.__channel.write(pageViewData, self.__context)

    def trackException(self, exception, properties=None, measurements=None):
        """Send an ExceptionTelemetry object for display in Diagnostic Search."""
        exceptionData = channel.contracts.ExceptionTelemetry()
        if not exception or not isinstance(exception, Exception):
            try:
                Exception(NULL_CONSTANT_STRING)
            except Exception as e:
                exception = e
       
        exceptionDataDetail = channel.contracts.ExceptionTelemetryDetails()
        exceptionDataDetail.id = 1
        exceptionDataDetail.outerId = 0
        exceptionDataDetail.typeName = exception.__class__.__name__
        exceptionDataDetail.message = "".join(exception.args)
        exceptionDataDetail.hasFullStack = False
        
        if "__traceback__" in dir(exception):
            exceptionDataDetail.hasFullStack = True
            traceback = exception.__traceback__
            counter = 0
            while traceback:
                frame = channel.contracts.ExceptionTelemetryStackFrame()
                frame.assembly = "<module>"
                frame.fileName = traceback.tb_frame.f_code.co_filename
                frame.level = counter
                frame.line = traceback.tb_lineno
                frame.method = traceback.tb_frame.f_code.co_name + "(" + ', '.join(traceback.tb_frame.f_code.co_varnames[:traceback.tb_frame.f_code.co_argcount]) + ")"
                exceptionDataDetail.parsedStack.append(frame)
                traceback = traceback.tb_next
                counter += 1
            exceptionDataDetail.parsedStack.reverse()

        exceptionData.exceptions.append(exceptionDataDetail)
        exceptionData.properties = properties
        exceptionData.measurements = measurements

        self.__channel.write(exceptionData, self.__context)

    def trackEvent(self, name, properties=None, measurements=None):
        """Send an EventTelemetry object for display in Diagnostic Search and aggregation in Metrics Explorer."""
        eventData = channel.contracts.EventTelemetry()
        if not name:
            name = NULL_CONSTANT_STRING
        eventData.name = name
        eventData.properties = properties
        eventData.measurements = measurements

        self.__channel.write(eventData, self.__context)

    def trackMetric(self, name, value, type=None, count=None, min=None, max=None, properties=None):
        """Send a MetricTelemetry object for aggregation in Metric Explorer."""
        metricDataPoint = channel.contracts.MetricTelemetryDataPoint()
        if not name:
            name = NULL_CONSTANT_STRING
        if not value:
            value = 0
        if not type:
            type = "Aggregation"
        metricDataPoint.name = name
        metricDataPoint.value = value
        metricDataPoint.kind = type
        metricDataPoint.count = count
        metricDataPoint.min = min
        metricDataPoint.max = max
        
        metricData = channel.contracts.MetricTelemetry()
        metricData.metrics.append(metricDataPoint)
        metricData.properties = properties

        self.__channel.write(metricData, self.__context)

    def trackTrace(self, name, properties=None, measurements=None):
        """Send a trace message for display in Diagnostic Search."""
        traceData = channel.contracts.MessageTelemetry()
        if not name:
            name = NULL_CONSTANT_STRING
        traceData.message = name
        traceData.properties = properties
        traceData.measurements = measurements

        self.__channel.write(traceData, self.__context)
