import json

class LocationContext(object):
    """Data contract class for type LocationContext."""
    def __init__(self):
        """Initializes a new instance of the LocationContext class."""
        self.__instanceVersion = 0
        self.__latitude = None
        self.__longitude = None
        self.__ip = None
        self.__continent = None
        self.__country = None
        self.__province = None
        self.__city = None
        if hasattr(self.__class__, 'initialize') and callable(getattr(self.__class__, 'initialize')):
            self.initialize()
        
    @property
    def latitude(self):
        """Gets or sets the 'latitude' property."""
        return self.__latitude
        
    @latitude.setter
    def latitude(self, value):
        self.__latitude = value
        self.__instanceVersion += 1
        
    @property
    def longitude(self):
        """Gets or sets the 'longitude' property."""
        return self.__longitude
        
    @longitude.setter
    def longitude(self, value):
        self.__longitude = value
        self.__instanceVersion += 1
        
    @property
    def ip(self):
        """Gets or sets the 'ip' property."""
        return self.__ip
        
    @ip.setter
    def ip(self, value):
        self.__ip = value
        self.__instanceVersion += 1
        
    @property
    def continent(self):
        """Gets or sets the 'continent' property."""
        return self.__continent
        
    @continent.setter
    def continent(self, value):
        self.__continent = value
        self.__instanceVersion += 1
        
    @property
    def country(self):
        """Gets or sets the 'country' property."""
        return self.__country
        
    @country.setter
    def country(self, value):
        self.__country = value
        self.__instanceVersion += 1
        
    @property
    def province(self):
        """Gets or sets the 'province' property."""
        return self.__province
        
    @province.setter
    def province(self, value):
        self.__province = value
        self.__instanceVersion += 1
        
    @property
    def city(self):
        """Gets or sets the 'city' property."""
        return self.__city
        
    @city.setter
    def city(self, value):
        self.__city = value
        self.__instanceVersion += 1
        
    def hasChanges(self):
        """Checks if the current instance has changes since its initalization."""
        return self.__instanceVersion != 0
    
    def serialize(self):
        """Serializes the contents of this object and returns the content as a JSON encoded string."""
        output = "{"
        prefix = ""
        if self.__latitude != None:
            output += prefix + "\"latitude\":"
            output += json.dumps(self.__latitude)
            prefix = ","
        if self.__longitude != None:
            output += prefix + "\"longitude\":"
            output += json.dumps(self.__longitude)
            prefix = ","
        if self.__ip != None:
            output += prefix + "\"ip\":"
            output += json.dumps(self.__ip)
            prefix = ","
        if self.__continent != None:
            output += prefix + "\"continent\":"
            output += json.dumps(self.__continent)
            prefix = ","
        if self.__country != None:
            output += prefix + "\"country\":"
            output += json.dumps(self.__country)
            prefix = ","
        if self.__province != None:
            output += prefix + "\"province\":"
            output += json.dumps(self.__province)
            prefix = ","
        if self.__city != None:
            output += prefix + "\"city\":"
            output += json.dumps(self.__city)
        output += "}"
        return output

