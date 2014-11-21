import json

class ExceptionTelemetryStackFrame(object):
    """Data contract class for type ExceptionTelemetryStackFrame."""
    def __init__(self):
        """Initializes a new instance of the ExceptionTelemetryStackFrame class."""
        self.__instanceVersion = 0
        self.__level = None
        self.__method = None
        self.__assembly = None
        self.__fileName = None
        self.__line = None
        if hasattr(self.__class__, 'initialize') and callable(getattr(self.__class__, 'initialize')):
            self.initialize()
        
    @property
    def level(self):
        """Gets or sets the 'level' property."""
        return self.__level
        
    @level.setter
    def level(self, value):
        self.__level = value
        self.__instanceVersion += 1
        
    @property
    def method(self):
        """Gets or sets the 'method' property."""
        return self.__method
        
    @method.setter
    def method(self, value):
        self.__method = value
        self.__instanceVersion += 1
        
    @property
    def assembly(self):
        """Gets or sets the 'assembly' property."""
        return self.__assembly
        
    @assembly.setter
    def assembly(self, value):
        self.__assembly = value
        self.__instanceVersion += 1
        
    @property
    def fileName(self):
        """Gets or sets the 'fileName' property."""
        return self.__fileName
        
    @fileName.setter
    def fileName(self, value):
        self.__fileName = value
        self.__instanceVersion += 1
        
    @property
    def line(self):
        """Gets or sets the 'line' property."""
        return self.__line
        
    @line.setter
    def line(self, value):
        self.__line = value
        self.__instanceVersion += 1
        
    def hasChanges(self):
        """Checks if the current instance has changes since its initalization."""
        return self.__instanceVersion != 0
    
    def serialize(self):
        """Serializes the contents of this object and returns the content as a JSON encoded string."""
        output = "{"
        prefix = ""
        if self.__level != None:
            output += prefix + "\"level\":"
            output += json.dumps(self.__level)
            prefix = ","
        output += prefix + "\"method\":"
        output += json.dumps(self.__method)
        prefix = ","
        if self.__assembly != None:
            output += prefix + "\"assembly\":"
            output += json.dumps(self.__assembly)
        if self.__fileName != None:
            output += prefix + "\"fileName\":"
            output += json.dumps(self.__fileName)
        if self.__line != None:
            output += prefix + "\"line\":"
            output += json.dumps(self.__line)
        output += "}"
        return output

