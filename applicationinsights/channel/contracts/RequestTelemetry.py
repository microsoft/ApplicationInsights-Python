import json

class RequestTelemetry(object):
    """Data contract class for type RequestTelemetry."""
    def __init__(self):
        """Initializes a new instance of the RequestTelemetry class."""
        self.__instanceVersion = 0
        self.__ver = 1
        self.__name = ""
        self.__id = None
        self.__startTime = None
        self.__duration = None
        self.__responseCode = None
        self.__success = None
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
    def name(self):
        """Gets or sets the 'name' property."""
        return self.__name
        
    @name.setter
    def name(self, value):
        self.__name = value
        self.__instanceVersion += 1
        
    @property
    def id(self):
        """Gets or sets the 'id' property."""
        return self.__id
        
    @id.setter
    def id(self, value):
        self.__id = value
        self.__instanceVersion += 1
        
    @property
    def startTime(self):
        """Gets or sets the 'startTime' property."""
        return self.__startTime
        
    @startTime.setter
    def startTime(self, value):
        self.__startTime = value
        self.__instanceVersion += 1
        
    @property
    def duration(self):
        """Gets or sets the 'duration' property."""
        return self.__duration
        
    @duration.setter
    def duration(self, value):
        self.__duration = value
        self.__instanceVersion += 1
        
    @property
    def responseCode(self):
        """Gets or sets the 'responseCode' property."""
        return self.__responseCode
        
    @responseCode.setter
    def responseCode(self, value):
        self.__responseCode = value
        self.__instanceVersion += 1
        
    @property
    def success(self):
        """Gets or sets the 'success' property."""
        return self.__success
        
    @success.setter
    def success(self, value):
        self.__success = value
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
        output += prefix + "\"name\":"
        output += json.dumps(self.__name)
        if self.__id != None:
            output += prefix + "\"id\":"
            output += json.dumps(self.__id)
        if self.__startTime != None:
            output += prefix + "\"startTime\":"
            output += json.dumps(self.__startTime)
        if self.__duration != None:
            output += prefix + "\"duration\":"
            output += json.dumps(self.__duration)
        if self.__responseCode != None:
            output += prefix + "\"responseCode\":"
            output += json.dumps(self.__responseCode)
        if self.__success != None:
            output += prefix + "\"success\":"
            output += json.dumps(self.__success)
        if self.__properties != None:
            output += prefix + "\"properties\":"
            output += json.dumps(self.__properties)
        if self.__measurements != None:
            output += prefix + "\"measurements\":"
            output += json.dumps(self.__measurements)
        output += "}"
        return output

