
from . import common
from applicationinsights import logging

import sys

class LoggingHandler(logging.LoggingHandler):
    def __init__(self, *args, **kwargs):
        client = common.create_client()
        new_kwargs = {}
        new_kwargs.update(kwargs)
        new_kwargs['telemetry_channel'] = client.channel
        super(LoggingHandler, self).__init__(client.context.instrumentation_key, *args, **new_kwargs)
