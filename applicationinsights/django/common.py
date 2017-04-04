
from django.conf import settings
import applicationinsights

class ApplicationInsightsSettings(object):
    def __init__(self):
        self._settings = settings.APPLICATION_INSIGHTS or settings.APPLICATIONINSIGHTS
        if not self._settings:
            self._settings = {}

    @property
    def ikey(self):
        if settings.DEBUG:
            return self.debug_ikey
        return self._settings.get("ikey", None)

    @property
    def debug_ikey(self):
        return self._settings.get("debug_ikey", None)

    @property
    def endpoint(self):
        if settings.DEBUG and "debug_endpoint" in self._settings:
            return self._settings["debug_endpoint"]
        return self._settings.get("endpoint", None)

    @property
    def send_interval(self):
        return self._settings.get("send_interval", None)

    @property
    def send_time(self):
        return self._settings.get("send_time", None)

    @property
    def use_operation_url(self):
        return self._settings.get("use_operation_url", False)

    @property
    def record_view_arguments(self):
        return self._settings.get("record_view_args", True)

saved_client = None

def create_client(aisettings=None):
    global saved_client

    if saved_client is not None:
        return saved_client

    if aisettings = None:
        aisettings = ApplicationInsightsSettings()

    ikey = aisettings.ikey
    if ikey is None:
        if settings.DEBUG:
            return dummy_client("Running in debug mode, no 'debug_ikey' set")
        else:
            return dummy_client("No ikey specified")

    if aisettings.endpoint is not None:
        sender = applicationinsights.channel.AsynchronousSender(service_endpoint=aisettings.endpoint)
    else:
        sender = applicationinsights.channel.AsynchronousSender()

    if aisettings.send_time is not None:
        sender.send_time = aisettings.send_time
    if aisettings.send_interval is not None:
        sender.send_interval = aisettings.send_interval

    queue = applicationinsights.channel.AsynchronousQueue(sender)
    channel = applicationinsights.channel.TelemetryChannel(None, queue)

    saved_client = applicationinsights.TelemetryClient(aisettings.ikey, channel)
    return saved_client

def dummy_client(reason):
    """Creates a dummy channel so even if we're not logging telemetry, we can still send
    along the real object to things that depend on it to exist"""

    sender = applicationinsights.channel.NullSender()
    queue = applicationinsights.channel.SynchronousQueue(sender)
    channel = applicationinsights.channel.TelemetryChannel(None, queue)
    return applicationinsights.TelemetryClient("00000000-0000-0000-0000-000000000000", channel)
