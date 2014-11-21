import json

class DeviceContext(object):
    """Data contract class for type DeviceContext."""
    def __init__(self):
        """Initializes a new instance of the DeviceContext class."""
        self.__instanceVersion = 0
        self.__type = "Other"
        self.__id = "Unknown"
        self.__os = "Unknown OS"
        self.__osVersion = "Unknown"
        self.__oemName = None
        self.__model = None
        self.__network = None
        self.__resolution = None
        self.__locale = "Unknown"
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
    def id(self):
        """Gets or sets the 'id' property."""
        return self.__id
        
    @id.setter
    def id(self, value):
        self.__id = value
        self.__instanceVersion += 1
        
    @property
    def os(self):
        """Gets or sets the 'os' property."""
        return self.__os
        
    @os.setter
    def os(self, value):
        self.__os = value
        self.__instanceVersion += 1
        
    @property
    def osVersion(self):
        """Gets or sets the 'osVersion' property."""
        return self.__osVersion
        
    @osVersion.setter
    def osVersion(self, value):
        self.__osVersion = value
        self.__instanceVersion += 1
        
    @property
    def oemName(self):
        """Gets or sets the 'oemName' property."""
        return self.__oemName
        
    @oemName.setter
    def oemName(self, value):
        self.__oemName = value
        self.__instanceVersion += 1
        
    @property
    def model(self):
        """Gets or sets the 'model' property."""
        return self.__model
        
    @model.setter
    def model(self, value):
        self.__model = value
        self.__instanceVersion += 1
        
    @property
    def network(self):
        """Gets or sets the 'network' property."""
        return self.__network
        
    @network.setter
    def network(self, value):
        self.__network = value
        self.__instanceVersion += 1
        
    @property
    def resolution(self):
        """Gets or sets the 'resolution' property."""
        return self.__resolution
        
    @resolution.setter
    def resolution(self, value):
        self.__resolution = value
        self.__instanceVersion += 1
        
    @property
    def locale(self):
        """Gets or sets the 'locale' property."""
        return self.__locale
        
    @locale.setter
    def locale(self, value):
        self.__locale = value
        self.__instanceVersion += 1
        
    def hasChanges(self):
        """Checks if the current instance has changes since its initalization."""
        return self.__instanceVersion != 0
    
    def serialize(self):
        """Serializes the contents of this object and returns the content as a JSON encoded string."""
        output = "{"
        prefix = ""
        output += prefix + "\"type\":"
        output += json.dumps(self.__type)
        prefix = ","
        output += prefix + "\"id\":"
        output += json.dumps(self.__id)
        output += prefix + "\"os\":"
        output += json.dumps(self.__os)
        output += prefix + "\"osVersion\":"
        output += json.dumps(self.__osVersion)
        if self.__oemName != None:
            output += prefix + "\"oemName\":"
            output += json.dumps(self.__oemName)
        if self.__model != None:
            output += prefix + "\"model\":"
            output += json.dumps(self.__model)
        if self.__network != None:
            output += prefix + "\"network\":"
            output += json.dumps(self.__network)
        if self.__resolution != None:
            output += prefix + "\"resolution\":"
            output += json.dumps(self.__resolution)
        output += prefix + "\"locale\":"
        output += json.dumps(self.__locale)
        output += "}"
        return output

