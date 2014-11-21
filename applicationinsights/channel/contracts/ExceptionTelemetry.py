import json

class ExceptionTelemetry(object):
    """Data contract class for type ExceptionTelemetry."""
    def __init__(self):
        """Initializes a new instance of the ExceptionTelemetry class."""
        self.__instanceVersion = 0
        self.__ver = 1
        self.__handledAt = "UserCode"
        self.__exceptions = []
        self.__properties = {}
        self.__measurements = {}
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
    def handledAt(self):
        """Gets or sets the 'handledAt' property."""
        return self.__handledAt
        
    @handledAt.setter
    def handledAt(self, value):
        self.__handledAt = value
        self.__instanceVersion += 1
        
    @property
    def exceptions(self):
        """Gets or sets the 'exceptions' property."""
        return self.__exceptions
        
    @exceptions.setter
    def exceptions(self, value):
        self.__exceptions = value
        self.__instanceVersion += 1
        
    @property
    def properties(self):
        """Gets or sets the 'properties' property."""
        return self.__properties
        
    @properties.setter
    def properties(self, value):
        self.__properties = value
        self.__instanceVersion += 1
        
    @property
    def measurements(self):
        """Gets or sets the 'measurements' property."""
        return self.__measurements
        
    @measurements.setter
    def measurements(self, value):
        self.__measurements = value
        self.__instanceVersion += 1
        
    def hasChanges(self):
        """Checks if the current instance has changes since its initalization."""
        return self.__instanceVersion != 0
    
    def serialize(self):
        """Serializes the contents of this object and returns the content as a JSON encoded string."""
        output = "{"
        prefix = ""
        output += prefix + "\"ver\":"
        output += json.dumps(self.__ver)
        prefix = ","
        output += prefix + "\"handledAt\":"
        output += json.dumps(self.__handledAt)
        arrayPrefix = ""
        output += prefix + "\"exceptions\":["
        for item in self.__exceptions:
            output += arrayPrefix + item.serialize()
            arrayPrefix = ","
        output += "]"
        if self.__properties != None:
            output += prefix + "\"properties\":"
            output += json.dumps(self.__properties)
        if self.__measurements != None:
            output += prefix + "\"measurements\":"
            output += json.dumps(self.__measurements)
        output += "}"
        return output

