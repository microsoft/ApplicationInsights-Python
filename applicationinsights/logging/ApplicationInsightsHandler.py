import logging
import applicationinsights

class ApplicationInsightsHandler(logging.Handler):
    """This class represents an integration point between Python's logging framework and the Application Insights
    service.

    Logging records are sent to the service either as simple Trace telemetry or as Exception telemetry (in the case
    of exception information being available).
    """
    def __init__(self, instrumentation_key, *args, **kwargs):
        """
        Initialize a new instance of the class.

        Args:
            instrumentation_key (str). the instrumentation key to use while sending telemetry to the service.
        """
        if not instrumentation_key:
            raise Exception('Instrumentation key was required but not provided')
        self.client = applicationinsights.TelemetryClient()
        self.client.context.instrumentation_key = instrumentation_key
        logging.Handler.__init__(self, *args, **kwargs)

    def flush(self):
        """Flushes the queued up telemetry to the service.
        """
        self.client.flush()
        return super().flush()

    def emit(self, record):
        """Emit a record.

        If a formatter is specified, it is used to format the record. If exception information is present, an Exception
        telemetry object is sent instead of a Trace telemetry object.

        Args:
            record (:class:`logging.LogRecord`). the record to format and send.
        """
        # the set of properties that will ride with the record
        properties = {
            'process': record.processName,
            'module': record.module,
            'fileName': record.filename,
            'lineNumber': record.lineno,
            'level': record.levelname,
        }

        # if we have exec_info, we will use it as an exception
        if record.exc_info:
            self.client.track_exception(*record.exc_info, properties=properties)
            return

        # if we don't simply format the message and send the trace
        formatted_message = self.format(record)
        self.client.track_trace(formatted_message, properties=properties)
