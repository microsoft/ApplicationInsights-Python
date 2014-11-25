import platform
import locale
import socket
import uuid

from applicationinsights.channel import contracts

# save off whatever is currently there
existing_device_initialize = contracts.Device._initialize
def device_initialize(self):
    """ The device initializer used to assign special properties to all device context objects"""
    existing_device_initialize(self)
    self.type = 'Other'
    self.id = platform.node()
    self.os_version = platform.version()
    self.locale = locale.getdefaultlocale()[0]

# assign the device context initializer
contracts.Device._initialize = device_initialize

class TelemetryContext(object):
    """Represents a context for sending telemetry to the Application Insights service."""
    def __init__(self):
        """Initializes a new instance of the TelemetryContext class."""
        self.instrumentation_key = None
        self.device = contracts.Device()
        self.application = contracts.Application()
        self.user = contracts.User()
        self.session = contracts.Session()
        self.operation = contracts.Operation()
        self.location = contracts.Location()
        self._properties = {}

    @property
    def properties(self):
        """Gets a dictionary of application-defined property values.."""
        return self._properties
