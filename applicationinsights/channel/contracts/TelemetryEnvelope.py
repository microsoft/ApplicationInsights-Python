import json

class TelemetryEnvelope(object):
    """Data contract class for type TelemetryEnvelope."""
    def __init__(self):
        """Initializes a new instance of the TelemetryEnvelope class."""
        self.__instanceVersion = 0
        self.__ver = 1
        self.__name = None
        self.__time = None
        self.__iKey = None
        self.__application = None
        self.__device = None
        self.__user = None
        self.__session = None
        self.__location = None
        self.__operation = None
        self.__data = None
        if hasattr(self.__class__, 'initialize') and callable(getattr(self.__class__, 'initialize')):
            self.initialize()
        
    @property
    def ver(self):
        """Gets or sets the 'ver' property."""
        return self.__ver
        
    @ver.setter
    def ver(self, value):
        self.__ver = value
        self.__instanceVersion += 1
        
    @property
    def name(self):
        """Gets or sets the 'name' property."""
        return self.__name
        
    @name.setter
    def name(self, value):
        self.__name = value
        self.__instanceVersion += 1
        
    @property
    def time(self):
        """Gets or sets the 'time' property."""
        return self.__time
        
    @time.setter
    def time(self, value):
        self.__time = value
        self.__instanceVersion += 1
        
    @property
    def iKey(self):
        """Gets or sets the 'iKey' property."""
        return self.__iKey
        
    @iKey.setter
    def iKey(self, value):
        self.__iKey = value
        self.__instanceVersion += 1
        
    @property
    def application(self):
        """Gets or sets the 'application' property."""
        return self.__application
        
    @application.setter
    def application(self, value):
        self.__application = value
        self.__instanceVersion += 1
        
    @property
    def device(self):
        """Gets or sets the 'device' property."""
        return self.__device
        
    @device.setter
    def device(self, value):
        self.__device = value
        self.__instanceVersion += 1
        
    @property
    def user(self):
        """Gets or sets the 'user' property."""
        return self.__user
        
    @user.setter
    def user(self, value):
        self.__user = value
        self.__instanceVersion += 1
        
    @property
    def session(self):
        """Gets or sets the 'session' property."""
        return self.__session
        
    @session.setter
    def session(self, value):
        self.__session = value
        self.__instanceVersion += 1
        
    @property
    def location(self):
        """Gets or sets the 'location' property."""
        return self.__location
        
    @location.setter
    def location(self, value):
        self.__location = value
        self.__instanceVersion += 1
        
    @property
    def operation(self):
        """Gets or sets the 'operation' property."""
        return self.__operation
        
    @operation.setter
    def operation(self, value):
        self.__operation = value
        self.__instanceVersion += 1
        
    @property
    def data(self):
        """Gets or sets the 'data' property."""
        return self.__data
        
    @data.setter
    def data(self, value):
        self.__data = value
        self.__instanceVersion += 1
        
    def hasChanges(self):
        """Checks if the current instance has changes since its initalization."""
        return self.__instanceVersion != 0
    
    def serialize(self):
        """Serializes the contents of this object and returns the content as a JSON encoded string."""
        output = "{"
        prefix = ""
        if self.__ver != None:
            output += prefix + "\"ver\":"
            output += json.dumps(self.__ver)
            prefix = ","
        if self.__name != None:
            output += prefix + "\"name\":"
            output += json.dumps(self.__name)
            prefix = ","
        output += prefix + "\"time\":"
        output += json.dumps(self.__time)
        prefix = ","
        output += prefix + "\"iKey\":"
        output += json.dumps(self.__iKey)
        if self.__application != None and self.__application.hasChanges():
            output += prefix + "\"application\":"
            output += self.__application.serialize()
        if self.__device != None and self.__device.hasChanges():
            output += prefix + "\"device\":"
            output += self.__device.serialize()
        if self.__user != None and self.__user.hasChanges():
            output += prefix + "\"user\":"
            output += self.__user.serialize()
        if self.__session != None and self.__session.hasChanges():
            output += prefix + "\"session\":"
            output += self.__session.serialize()
        if self.__location != None and self.__location.hasChanges():
            output += prefix + "\"location\":"
            output += self.__location.serialize()
        if self.__operation != None and self.__operation.hasChanges():
            output += prefix + "\"operation\":"
            output += self.__operation.serialize()
        if self.__data != None and self.__data.hasChanges():
            output += prefix + "\"data\":"
            output += self.__data.serialize()
        output += "}"
        return output

