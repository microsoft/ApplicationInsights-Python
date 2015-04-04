import datetime
import re
import applicationinsights

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
        telemetry_channel = kwargs.pop('telemetry_channel', None)
        if not telemetry_channel:
            sender = applicationinsights.channel.AsynchronousSender()
            queue = applicationinsights.channel.AsynchronousQueue(sender)
            telemetry_channel = applicationinsights.channel.TelemetryChannel(None, queue)
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
        name = environ.get('PATH_INFO') or '/'
        closure = {'status': '200 OK'}

        def status_interceptor(status_string, headers_array, exc_info=None):
            closure['status'] = status_string
            start_response(status_string, headers_array, exc_info)

        for part in self._wsgi_application(environ, status_interceptor):
            yield part

        success = True
        response_match = re.match(r'\s*(?P<code>\d+)', closure['status'])
        if response_match:
            response_code = response_match.group('code')
            if int(response_code) >= 400:
                success = False
        else:
            response_code = closure['status']
            success = False
            
        http_method = environ.get('REQUEST_METHOD', 'GET')
        url = name
        query_string = environ.get('QUERY_STRING')
        if query_string:
            url += '?' + query_string

        scheme = environ.get('wsgi.url_scheme', 'http')
        host =  environ.get('HTTP_HOST', environ.get('SERVER_NAME', 'unknown'))

        url = scheme + '://' + host + url

        end_time = datetime.datetime.utcnow()
        duration = int((end_time - start_time).total_seconds() * 1000)

        self.client.track_request(name, url, success, start_time.isoformat() + 'Z', duration, response_code, http_method)
