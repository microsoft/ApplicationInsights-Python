
import datetime
import inspect
import sys
import time
import traceback
import uuid

import applicationinsights
from applicationinsights.channel import contracts
from . import common

# Pick a function to measure time; starting with 3.3, time.monotonic is available.
if sys.version >= (3, 3):
    TIME_FUNC = time.monotonic
else:
    TIME_FUNC = time.time

class ApplicationInsightsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

        # Get configuration
        self._settings = common.ApplicationInsightsSettings()
        self._client = common.create_client(self._settings)

    def __call__(self, request):
        # Populate context object onto request
        addon = RequestAddon(self._client)
        data = addon.request
        context = addon.context
        request.appinsights = addon

        # Basic request properties
        data.start_time = datetime.datetime.utcnow().isoformat() + "Z"
        data.http_method = request.method
        data.url = request.build_absolute_uri()
        data.name = "%s %s" % (request.method, data.url)
        context.client.ip = request.META.get('REMOTE_ADDR', '')
        context.user.user_agent = request.META.get('HTTP_USER_AGENT', '')

        # User
        if request.user is not None and request.user.is_authenticated:
            context.user.account_id = request.user.get_short_name()

        # Run and time the request
        addon.start_stopwatch()
        response = self.get_response(request)

        # Fill in data from the response
        data.duration = addon.measure_duration()
        data.response_code = response.status_code
        data.success = response.status_code < 400

        # Submit and return
        self._client.channel.write(data, context)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not hasattr(request, "appinsights"):
            return None

        data = request.appinsights.request

        # Operation name is the method + url by default (set in __call__),
        # so if that's not set, then we'll use the view name.
        if not self._settings.use_operation_url:
            mod = inspect.getmodule(view_func)
            name = view_func.__name__
            if mod:
                data.name = "%s %s.%s" % (data.http_method, mod, name)
            else:
                data.name = "%s %s" % (data.http_method, name)

        # Populate the properties with view arguments
        if self._settings.record_view_arguments:
            if data.properties is None:
                data.properties = {}

            for i, arg in enumerate(view_args):
                if isinstance(arg, str) or isinstance(arg, int):
                    data.properties['view_arg_' + str(i)] = str(arg)
                else:
                    data.properties['view_arg_' + str(i)] = repr(arg)

            for k, v in view_kwargs.items():
                if isinstance(arg, str) or isinstance(arg, int):
                    data.properties['view_arg_' + k] = str(v)
                else:
                    data.properties['view_arg_' + k] = repr(v)

        return None

    def process_exception(self, request, exception):
        client = applicationinsights.TelemetryClient(self._client.context.instrumentation_key, self._client.channel)
        if hasattr(request, 'appinsights'):
            client.context.operation.parent_id = request.appinsights.request.id

        client.track_exception(type(exception).__name__, exception, sys.exc_info()[2])

        return None

    def process_template_response(self, request, response):
        if hasattr(response, 'appinsights') and hasattr(response, 'template_name'):
            data = request.appinsights.request
            if data.properties is None:
                data.properties = {}
            data.properties['template_name'] = response.template_name

        return None

class RequestAddon(object):
    def __init__(self, client):
        self.client = client
        self.request = contracts.RequestData()
        self.context = applicationinsights.channel.TelemetryContext()
        self.context.instrumentation_key = client.context.instrumentation_key
        self._process_start_time = None

    def start_stopwatch(self):
        self._process_start_time = TIME_FUNC()

    def measure_duration(self):
        end_time = TIME_FUNC()
        return ms_to_duration(int((end_time - self._process_start_time) * 1000))

def ms_to_duration(n):
    duration_parts = []
    for multiplier in [1000, 60, 60, 24]:
        duration_parts.append(n % multiplier)
        n //= multiplier

    duration_parts.reverse()
    duration = "%02d:%02d:%02d.%03d" % tuple(duration_parts)
    if n:
        duration = "%d.%s" % (n, duration)

    return duration
