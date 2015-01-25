import datetime
import re
import applicationinsights

class Closure(object):
    """A simple closure object used to transfer context between different scopes.
    """
    def __init__(self):
        self.status = None

class WSGIApplication(object):
    """ This class represents a WSGI wrapper that enables request telemetry for existing WSGI applications. The request
    telemetry will be sent to Application Insights service using the supplied instrumentation key.

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
    """
    def __init__(self, instrumentation_key, wsgi_application, *args, **kwargs):
        """
        Initialize a new instance of the class.

        Args:
            instrumentation_key (str). the instrumentation key to use while sending telemetry to the service.\n
            wsgi_application (func). the WSGI application that we're wrapping.
        """
        if not instrumentation_key:
            raise Exception('Instrumentation key was required but not provided')
        if not wsgi_application:
            raise Exception('WSGI application was required but not provided')
        telemetry_channel = kwargs.get('telemetry_channel')
        if 'telemetry_channel' in kwargs:
            del kwargs['telemetry_channel']
        self.client = applicationinsights.TelemetryClient(instrumentation_key, telemetry_channel)
        self._wsgi_application = wsgi_application

    def flush(self):
        """Flushes the queued up telemetry to the service.
        """
        self.client.flush()

    def __call__(self, environ, start_response):
        """Callable implementation for WSGI middleware.

        Args:
            environ (dict). a dictionary containing all WSGI environment properties for this request.\n
            start_response (func). a function used to store the status, HTTP headers to be sent to the client and optional exception information.

        Returns:
            (obj). the response to send back to the client.
        """
        start_time = datetime.datetime.utcnow()
        name = '/'
        if 'PATH_INFO' in environ:
            name = environ['PATH_INFO']
        closure = Closure()
        closure.status = '200 OK'

        def status_interceptor(status_string, headers_array):
            closure.status = status_string
            start_response(status_string, headers_array)

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
