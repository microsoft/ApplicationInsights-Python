import json

class SessionContext(object):
    """Data contract class for type SessionContext."""
    def __init__(self):
        """Initializes a new instance of the SessionContext class."""
        self.__instanceVersion = 0
        self.__id = None
        self.__firstSession = None
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
    def firstSession(self):
        """Gets or sets the 'firstSession' property."""
        return self.__firstSession
        
    @firstSession.setter
    def firstSession(self, value):
        self.__firstSession = value
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
        if self.__firstSession != None:
            output += prefix + "\"firstSession\":"
            output += json.dumps(self.__firstSession)
        output += "}"
        return output

