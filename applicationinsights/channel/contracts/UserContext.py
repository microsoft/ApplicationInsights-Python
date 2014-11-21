import json

class UserContext(object):
    """Data contract class for type UserContext."""
    def __init__(self):
        """Initializes a new instance of the UserContext class."""
        self.__instanceVersion = 0
        self.__id = None
        self.__accountId = None
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
    def accountId(self):
        """Gets or sets the 'accountId' property."""
        return self.__accountId
        
    @accountId.setter
    def accountId(self, value):
        self.__accountId = value
        self.__instanceVersion += 1
        
    def hasChanges(self):
        """Checks if the current instance has changes since its initalization."""
        return self.__instanceVersion != 0
    
    def serialize(self):
        """Serializes the contents of this object and returns the content as a JSON encoded string."""
        output = "{"
        prefix = ""
        output += prefix + "\"id\":"
        output += json.dumps(self.__id)
        prefix = ","
        if self.__accountId != None:
            output += prefix + "\"accountId\":"
            output += json.dumps(self.__accountId)
        output += "}"
        return output

