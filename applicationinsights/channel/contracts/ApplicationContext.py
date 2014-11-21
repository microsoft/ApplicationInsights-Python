import json

class ApplicationContext(object):
    """Data contract class for type ApplicationContext."""
    def __init__(self):
        """Initializes a new instance of the ApplicationContext class."""
        self.__instanceVersion = 0
        self.__id = "Unknown"
        self.__ver = "Unknown"
        if hasattr(self.__class__, 'initialize') and callable(getattr(self.__class__, 'initialize')):
            self.initialize()
        
    @property
    def id(self):
        """Gets or sets the 'id' property."""
        return self.__id
        
    @id.setter
    def id(self, value):
        self.__id = value
        self.__instanceVersion += 1
        
    @property
    def ver(self):
        """Gets or sets the 'ver' property."""
        return self.__ver
        
    @ver.setter
    def ver(self, value):
        self.__ver = value
        self.__instanceVersion += 1
        
    def hasChanges(self):
        """Checks if the current instance has changes since its initalization."""
        return self.__instanceVersion != 0
    
    def serialize(self):
        """Serializes the contents of this object and returns the content as a JSON encoded string."""
        output = "{"
        prefix = ""
        if self.__id != None:
            output += prefix + "\"id\":"
            output += json.dumps(self.__id)
            prefix = ","
        if self.__ver != None:
            output += prefix + "\"ver\":"
            output += json.dumps(self.__ver)
        output += "}"
        return output

