import json

class RemoteDependencyTelemetry(object):
    """Data contract class for type RemoteDependencyTelemetry."""
    def __init__(self):
        """Initializes a new instance of the RemoteDependencyTelemetry class."""
        self.__instanceVersion = 0
        self.__name = None
        self.__dependencyKind = 0
        self.__value = None
        self.__resource = None
        self.__kind = None
        self.__count = None
        self.__min = None
        self.__max = None
        self.__stdDev = None
        self.__properties = {}
        self.__measurements = {}
        if hasattr(self.__class__, 'initialize') and callable(getattr(self.__class__, 'initialize')):
            self.initialize()
        
    @property
    def name(self):
        """Gets or sets the 'name' property."""
        return self.__name
        
    @name.setter
    def name(self, value):
        self.__name = value
        self.__instanceVersion += 1
        
    @property
    def dependencyKind(self):
        """Gets or sets the 'dependencyKind' property."""
        return self.__dependencyKind
        
    @dependencyKind.setter
    def dependencyKind(self, value):
        self.__dependencyKind = value
        self.__instanceVersion += 1
        
    @property
    def value(self):
        """Gets or sets the 'value' property."""
        return self.__value
        
    @value.setter
    def value(self, value):
        self.__value = value
        self.__instanceVersion += 1
        
    @property
    def resource(self):
        """Gets or sets the 'resource' property."""
        return self.__resource
        
    @resource.setter
    def resource(self, value):
        self.__resource = value
        self.__instanceVersion += 1
        
    @property
    def kind(self):
        """Gets or sets the 'kind' property."""
        return self.__kind
        
    @kind.setter
    def kind(self, value):
        self.__kind = value
        self.__instanceVersion += 1
        
    @property
    def count(self):
        """Gets or sets the 'count' property."""
        return self.__count
        
    @count.setter
    def count(self, value):
        self.__count = value
        self.__instanceVersion += 1
        
    @property
    def min(self):
        """Gets or sets the 'min' property."""
        return self.__min
        
    @min.setter
    def min(self, value):
        self.__min = value
        self.__instanceVersion += 1
        
    @property
    def max(self):
        """Gets or sets the 'max' property."""
        return self.__max
        
    @max.setter
    def max(self, value):
        self.__max = value
        self.__instanceVersion += 1
        
    @property
    def stdDev(self):
        """Gets or sets the 'stdDev' property."""
        return self.__stdDev
        
    @stdDev.setter
    def stdDev(self, value):
        self.__stdDev = value
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
        output += prefix + "\"name\":"
        output += json.dumps(self.__name)
        prefix = ","
        output += prefix + "\"dependencyKind\":"
        output += json.dumps(self.__dependencyKind)
        output += prefix + "\"value\":"
        output += json.dumps(self.__value)
        output += prefix + "\"resource\":"
        output += json.dumps(self.__resource)
        output += prefix + "\"kind\":"
        output += json.dumps(self.__kind)
        if self.__count != None:
            output += prefix + "\"count\":"
            output += json.dumps(self.__count)
        if self.__min != None:
            output += prefix + "\"min\":"
            output += json.dumps(self.__min)
        if self.__max != None:
            output += prefix + "\"max\":"
            output += json.dumps(self.__max)
        if self.__stdDev != None:
            output += prefix + "\"stdDev\":"
            output += json.dumps(self.__stdDev)
        if self.__properties != None:
            output += prefix + "\"properties\":"
            output += json.dumps(self.__properties)
        if self.__measurements != None:
            output += prefix + "\"measurements\":"
            output += json.dumps(self.__measurements)
        output += "}"
        return output

