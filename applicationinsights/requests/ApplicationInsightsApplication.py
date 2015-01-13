import datetime
import re
import applicationinsights

class Closure(object):
    """A simple closure object used to transfer context between different scopes.
    """
    def __init__(self):
        self.status = None

class ApplicationInsightsApplication(object):
    def __init__(self, instrumentation_key, wsgi_application, *args, **kwargs):
        """
        Initialize a new instance of the class.

        Args:
            instrumentation_key (str). the instrumentation key to use while sending telemetry to the service.
        """
        if not instrumentation_key:
            raise Exception('Instrumentation key was required but not provided')
        telemetry_channel = kwargs.get('telemetry_channel')
        if 'telemetry_channel' in kwargs:
            del kwargs['telemetry_channel']
        self.client = applicationinsights.TelemetryClient(telemetry_channel)
        self.client.context.instrumentation_key = instrumentation_key
        self._wsgi_application = wsgi_application

    def flush(self):
        """Flushes the queued up telemetry to the service.
        """
        self.client.flush()

    def __call__(self, environ, start_response):
        """Callable implementation for WSGI middleware.

        Args:
            environ (dict). a dictionary containing all WSGI environment properties for this request.
            start_response (func). a function used to store the status, HTTP headers to be sent to the client and optional exception information.

        Returns:
            (str). the data to write back to the client.
        """
        start_time = datetime.datetime.utcnow()
        name = '/'
        if 'PATH_INFO' in environ:
            name = environ['PATH_INFO']
        closure = Closure()
        closure.status = '200 OK'

        def status_interceptor(status_string, headers_array, exc_info=None):
            closure.status = status_string
            start_response(status_string, headers_array, exc_info)

        response = self._wsgi_application(environ, status_interceptor)
        response_code = re.match('\s*(?P<code>\d+)', closure.status).group('code')
        success = True
        if int(response_code) >= 400:
            success = False
        http_method = 'GET'
        if 'REQUEST_METHOD' in environ:
            http_method = environ['REQUEST_METHOD']
        url = name
        if 'QUERY_STRING' in environ:
            query_string = environ['QUERY_STRING']
            if query_string:
                url += '?' + query_string
        end_time = datetime.datetime.utcnow()
        duration = int((end_time - start_time).total_seconds() * 1000)

        self.client.track_request(name, url, success, start_time.isoformat() + 'Z', duration, response_code, http_method)
        return response


