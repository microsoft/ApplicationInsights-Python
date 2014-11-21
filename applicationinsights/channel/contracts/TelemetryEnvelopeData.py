import json

class TelemetryEnvelopeData(object):
    """Data contract class for type TelemetryEnvelopeData."""
    def __init__(self):
        """Initializes a new instance of the TelemetryEnvelopeData class."""
        self.__instanceVersion = 0
        self.__type = None
        self.__item = None
        if hasattr(self.__class__, 'initialize') and callable(getattr(self.__class__, 'initialize')):
            self.initialize()
        
    @property
    def type(self):
        """Gets or sets the 'type' property."""
        return self.__type
        
    @type.setter
    def type(self, value):
        self.__type = value
        self.__instanceVersion += 1
        
    @property
    def item(self):
        """Gets or sets the 'item' property."""
        return self.__item
        
    @item.setter
    def item(self, value):
        self.__item = value
        self.__instanceVersion += 1
        
    def hasChanges(self):
        """Checks if the current instance has changes since its initalization."""
        return self.__instanceVersion != 0
    
    def serialize(self):
        """Serializes the contents of this object and returns the content as a JSON encoded string."""
        output = "{"
        prefix = ""
        if self.__type != None:
            output += prefix + "\"type\":"
            output += json.dumps(self.__type)
            prefix = ","
        if self.__item != None and self.__item.hasChanges():
            output += prefix + "\"item\":"
            output += self.__item.serialize()
        output += "}"
        return output

