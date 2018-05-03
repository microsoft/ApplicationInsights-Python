from os import getenv

from applicationinsights import TelemetryClient
from applicationinsights.channel import AsynchronousSender
from applicationinsights.channel import AsynchronousQueue
from applicationinsights.channel import TelemetryChannel
from applicationinsights.logging import LoggingHandler
from applicationinsights.requests import WSGIApplication

CONF_PREFIX = "APPINSIGHTS"

CONF_KEY = CONF_PREFIX + "_INSTRUMENTATIONKEY"
CONF_ENDPOINT_URI = CONF_PREFIX + "_ENDPOINT_URI"
CONF_DISABLE_REQUEST_LOGGING = CONF_PREFIX + "_DISABLE_REQUEST_LOGGING"
CONF_DISABLE_TRACE_LOGGING = CONF_PREFIX + "_DISABLE_TRACE_LOGGING"
CONF_DISABLE_EXCEPTION_LOGGING = CONF_PREFIX + "_DISABLE_EXCEPTION_LOGGING"


class AppInsights(object):
    def __init__(self, app=None):
        self._key = None
        self._endpoint_uri = None
        self._channel = None
        self._requests_middleware = None
        self._trace_log_handler = None
        self._exception_telemetry_client = None

        if app:
            self.init_app(app)

    def init_app(self, app):
        self._key = app.config.get(CONF_KEY) or getenv(CONF_KEY)

        if not self._key:
            return

        self._endpoint_uri = app.config.get(CONF_ENDPOINT_URI)

        if self._endpoint_uri:
            sender = AsynchronousSender(self._endpoint_uri)
        else:
            sender = AsynchronousSender()

        queue = AsynchronousQueue(sender)
        self._channel = TelemetryChannel(None, queue)

        self._init_request_logging(app)
        self._init_trace_logging(app)
        self._init_exception_logging(app)

    def _init_request_logging(self, app):
        enabled = not app.config.get(CONF_DISABLE_REQUEST_LOGGING, False)

        if not enabled:
            return

        self._requests_middleware = WSGIApplication(
            self._key, app.wsgi_app, telemetry_channel=self._channel)

        app.wsgi_app = self._requests_middleware

    def _init_trace_logging(self, app):
        enabled = not app.config.get(CONF_DISABLE_TRACE_LOGGING, False)

        if not enabled:
            return

        self._trace_log_handler = LoggingHandler(
            self._key, telemetry_channel=self._channel)

        app.logger.addHandler(self._trace_log_handler)

    def _init_exception_logging(self, app):
        enabled = not app.config.get(CONF_DISABLE_EXCEPTION_LOGGING, False)

        if not enabled:
            return

        exception_telemetry_client = TelemetryClient(
            self._key, telemetry_channel=self._channel)

        @app.errorhandler(Exception)
        def exception_handler(exception):
            exception_telemetry_client.track_exception(
                type=type(exception),
                value=exception,
                tb=exception.__traceback__)

            raise exception

        self._exception_telemetry_client = exception_telemetry_client

    def flush(self):
        if self._requests_middleware:
            self._requests_middleware.flush()

        if self._trace_log_handler:
            self._trace_log_handler.flush()

        if self._exception_telemetry_client:
            self._exception_telemetry_client.flush()
