import json

class PageViewTelemetry(object):
    """Data contract class for type PageViewTelemetry."""
    def __init__(self):
        """Initializes a new instance of the PageViewTelemetry class."""
        self.__instanceVersion = 0
        self.__ver = 1
        self.__url = None
        self.__pageViewPerf = None
        self.__name = None
        self.__duration = None
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
    def url(self):
        """Gets or sets the 'url' property."""
        return self.__url
        
    @url.setter
    def url(self, value):
        self.__url = value
        self.__instanceVersion += 1
        
    @property
    def pageViewPerf(self):
        """Gets or sets the 'pageViewPerf' property."""
        return self.__pageViewPerf
        
    @pageViewPerf.setter
    def pageViewPerf(self, value):
        self.__pageViewPerf = value
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
    def duration(self):
        """Gets or sets the 'duration' property."""
        return self.__duration
        
    @duration.setter
    def duration(self, value):
        self.__duration = value
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
        output += prefix + "\"url\":"
        output += json.dumps(self.__url)
        if self.__pageViewPerf != None and self.__pageViewPerf.hasChanges():
            output += prefix + "\"pageViewPerf\":"
            output += self.__pageViewPerf.serialize()
        output += prefix + "\"name\":"
        output += json.dumps(self.__name)
        output += prefix + "\"duration\":"
        output += json.dumps(self.__duration)
        if self.__properties != None:
            output += prefix + "\"properties\":"
            output += json.dumps(self.__properties)
        if self.__measurements != None:
            output += prefix + "\"measurements\":"
            output += json.dumps(self.__measurements)
        output += "}"
        return output

