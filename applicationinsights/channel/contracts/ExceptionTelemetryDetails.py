import json

class ExceptionTelemetryDetails(object):
    """Data contract class for type ExceptionTelemetryDetails."""
    def __init__(self):
        """Initializes a new instance of the ExceptionTelemetryDetails class."""
        self.__instanceVersion = 0
        self.__id = None
        self.__outerId = None
        self.__typeName = None
        self.__message = None
        self.__hasFullStack = True
        self.__stack = None
        self.__parsedStack = []
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
    def outerId(self):
        """Gets or sets the 'outerId' property."""
        return self.__outerId
        
    @outerId.setter
    def outerId(self, value):
        self.__outerId = value
        self.__instanceVersion += 1
        
    @property
    def typeName(self):
        """Gets or sets the 'typeName' property."""
        return self.__typeName
        
    @typeName.setter
    def typeName(self, value):
        self.__typeName = value
        self.__instanceVersion += 1
        
    @property
    def message(self):
        """Gets or sets the 'message' property."""
        return self.__message
        
    @message.setter
    def message(self, value):
        self.__message = value
        self.__instanceVersion += 1
        
    @property
    def hasFullStack(self):
        """Gets or sets the 'hasFullStack' property."""
        return self.__hasFullStack
        
    @hasFullStack.setter
    def hasFullStack(self, value):
        self.__hasFullStack = value
        self.__instanceVersion += 1
        
    @property
    def stack(self):
        """Gets or sets the 'stack' property."""
        return self.__stack
        
    @stack.setter
    def stack(self, value):
        self.__stack = value
        self.__instanceVersion += 1
        
    @property
    def parsedStack(self):
        """Gets or sets the 'parsedStack' property."""
        return self.__parsedStack
        
    @parsedStack.setter
    def parsedStack(self, value):
        self.__parsedStack = value
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
        if self.__outerId != None:
            output += prefix + "\"outerId\":"
            output += json.dumps(self.__outerId)
        output += prefix + "\"typeName\":"
        output += json.dumps(self.__typeName)
        output += prefix + "\"message\":"
        output += json.dumps(self.__message)
        output += prefix + "\"hasFullStack\":"
        output += json.dumps(self.__hasFullStack)
        if self.__stack != None:
            output += prefix + "\"stack\":"
            output += json.dumps(self.__stack)
        if self.__parsedStack != None:
            arrayPrefix = ""
            output += prefix + "\"parsedStack\":["
            for item in self.__parsedStack:
                output += arrayPrefix + item.serialize()
                arrayPrefix = ","
            output += "]"
        output += "}"
        return output

