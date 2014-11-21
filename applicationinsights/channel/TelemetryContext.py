import platform
import locale
import socket
import uuid

from applicationinsights.channel import contracts

def deviceInitializer(self):
    """ The device initializer used to assign special properties to all device context objects"""
    self.type = "Other"
    self.id = platform.node()
    self.osVersion = platform.version()
    self.locale = locale.getdefaultlocale()[0]

# assign the device context initializer
contracts.DeviceContext.initialize = deviceInitializer

class TelemetryContext(object):
    """Represents a context for sending telemetry to the Application Insights service."""
    def __init__(self):
        """Initializes a new instance of the TelemetryContext class."""
        self.__instrumentationKey = None
        self.__device = contracts.DeviceContext()
        self.__application = contracts.ApplicationContext()
        self.__user = contracts.UserContext()
        self.__session = contracts.SessionContext()
        self.__operation = contracts.OperationContext()
        self.__location = contracts.LocationContext()
        self.__properties = {}

    @property
    def instrumentationKey(self):
        """Gets or sets the instrumentation key for this TelemetryContext."""
        return self.__instrumentationKey

    @instrumentationKey.setter
    def instrumentationKey(self, value):
        self.__instrumentationKey = value

    @property
    def device(self):
        """Gets or sets the object describing the device tracked by this TelemetryContext."""
        return self.__device

    @device.setter
    def device(self, value):
        if isinstance(value, contracts.DeviceContext) or not value:
            self.__device = value

    @property
    def application(self):
        """Gets or sets the object describing the component tracked by this TelemetryContext."""
        return self.__application

    @application.setter
    def application(self, value):
        if isinstance(value, contracts.ApplicationContext) or not value:
            self.__application = value

    @property
    def user(self):
        """Gets or sets the object describing a user tracked by this TelemetryContext."""
        return self.__user

    @user.setter
    def user(self, value):
        if isinstance(value, contracts.UserContext) or not value:
            self.__user = value

    @property
    def session(self):
        """Gets or sets the object describing a user session tracked by this TelemetryContext."""
        return self.__session

    @session.setter
    def session(self, value):
        if isinstance(value, contracts.SessionContext) or not value:
            self.__session = value

    @property
    def location(self):
        """Gets or sets the object describing a location tracked by this TelemetryContext."""
        return self.__location

    @location.setter
    def location(self, value):
        if isinstance(value, contracts.LocationContext) or not value:
            self.__location = value

    @property
    def operation(self):
        """Gets or sets the object describing a operation tracked by this TelemetryContext."""
        return self.__operation

    @operation.setter
    def operation(self, value):
        if isinstance(value, contracts.OperationContext) or not value:
            self.__operation = value

    @property
    def properties(self):
        """Gets a dictionary of application-defined property values.."""
        return self.__properties
