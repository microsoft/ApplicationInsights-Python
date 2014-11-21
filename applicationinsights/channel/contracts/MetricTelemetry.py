import json

class MetricTelemetry(object):
    """Data contract class for type MetricTelemetry."""
    def __init__(self):
        """Initializes a new instance of the MetricTelemetry class."""
        self.__instanceVersion = 0
        self.__ver = 1
        self.__metrics = []
        self.__properties = {}
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
    def metrics(self):
        """Gets or sets the 'metrics' property."""
        return self.__metrics
        
    @metrics.setter
    def metrics(self, value):
        self.__metrics = value
        self.__instanceVersion += 1
        
    @property
    def properties(self):
        """Gets or sets the 'properties' property."""
        return self.__properties
        
    @properties.setter
    def properties(self, value):
        self.__properties = value
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
        arrayPrefix = ""
        output += prefix + "\"metrics\":["
        for item in self.__metrics:
            output += arrayPrefix + item.serialize()
            arrayPrefix = ","
        output += "]"
        if self.__properties != None:
            output += prefix + "\"properties\":"
            output += json.dumps(self.__properties)
        output += "}"
        return output

