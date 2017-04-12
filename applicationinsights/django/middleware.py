
import datetime
import inspect
import sys
import time
import traceback
import uuid

from django.http import Http404

import applicationinsights
from applicationinsights.channel import contracts
from . import common

# Pick a function to measure time; starting with 3.3, time.monotonic is available.
if sys.version_info >= (3, 3):
    TIME_FUNC = time.monotonic
else:
    TIME_FUNC = time.time

class ApplicationInsightsMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response

        # Get configuration
        self._settings = common.ApplicationInsightsSettings()
        self._client = common.create_client(self._settings)

    # Pre-1.10 handler
    def process_request(self, request):
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
        context.operation.id = data.id
        context.location.ip = request.META.get('REMOTE_ADDR', '')
        context.user.user_agent = request.META.get('HTTP_USER_AGENT', '')

        # User
        if request.user is not None and not request.user.is_anonymous and request.user.is_authenticated:
            context.user.account_id = request.user.get_short_name()

        # Run and time the request
        addon.start_stopwatch()
        return None

    # Pre-1.10 handler
    def process_response(self, request, response):
        addon = request.appinsights
        duration = addon.measure_duration()

        data = addon.request
        context = addon.context

        # Fill in data from the response
        data.duration = addon.measure_duration()
        data.response_code = response.status_code
        data.success = response.status_code < 400

        # Submit and return
        self._client.channel.write(data, context)
        return response

    # 1.10 and up...
    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        self.process_response(request, response)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not hasattr(request, "appinsights"):
            return None

        data = request.appinsights.request
        context = request.appinsights.context

        # Operation name is the method + url by default (set in __call__),
        # so if that's not set, then we'll use the view name.
        if not self._settings.use_operation_url:
            mod = inspect.getmodule(view_func)
            name = view_func.__name__
            if mod:
                opname = "%s %s.%s" % (data.http_method, mod.__name__, name)
            else:
                opname = "%s %s" % (data.http_method, name)
            data.name = opname
            context.operation.name = opname

        # Populate the properties with view arguments
        if self._settings.record_view_arguments:
            for i, arg in enumerate(view_args):
                data.properties['view_arg_' + str(i)] = arg_to_str(arg)

            for k, v in view_kwargs.items():
                data.properties['view_arg_' + k] = arg_to_str(v)

        return None

    def process_exception(self, request, exception):
        if type(exception) is Http404:
            return None

        client = applicationinsights.TelemetryClient(self._client.context.instrumentation_key, self._client.channel)
        if hasattr(request, 'appinsights'):
            client.context.operation.parent_id = request.appinsights.request.id

        client.track_exception(type(exception), exception, sys.exc_info()[2])

        return None

    def process_template_response(self, request, response):
        if hasattr(request, 'appinsights') and hasattr(response, 'template_name'):
            data = request.appinsights.request
            data.properties['template_name'] = response.template_name

        return None

class RequestAddon(object):
    def __init__(self, client):
        self._baseclient = client
        self._client = None
        self.request = contracts.RequestData()
        self.request.id = str(uuid.uuid4())
        self.context = applicationinsights.channel.TelemetryContext()
        self.context.instrumentation_key = client.context.instrumentation_key
        self.context.operation.id = self.request.id
        self._process_start_time = None

    @property
    def client(self):
        if self._client is None:
            # Create a client that submits telemetry parented to the request.
            self._client = applicationinsights.TelemetryClient(self.context.instrumentation_key, self._baseclient.channel)
            self._client.context.operation.parent_id = self.context.operation.id

        return self._client

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

def arg_to_str(arg):
    if isinstance(arg, str):
        return arg
    if isinstance(arg, int):
        return str(arg)
    return repr(arg)
