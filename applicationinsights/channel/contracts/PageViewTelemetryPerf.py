import json

class PageViewTelemetryPerf(object):
    """Data contract class for type PageViewTelemetryPerf."""
    def __init__(self):
        """Initializes a new instance of the PageViewTelemetryPerf class."""
        self.__instanceVersion = 0
        self.__perfTotal = None
        self.__networkConnect = None
        self.__sentRequest = None
        self.__receivedResponse = None
        self.__domProcessing = None
        if hasattr(self.__class__, 'initialize') and callable(getattr(self.__class__, 'initialize')):
            self.initialize()
        
    @property
    def perfTotal(self):
        """Gets or sets the 'perfTotal' property."""
        return self.__perfTotal
        
    @perfTotal.setter
    def perfTotal(self, value):
        self.__perfTotal = value
        self.__instanceVersion += 1
        
    @property
    def networkConnect(self):
        """Gets or sets the 'networkConnect' property."""
        return self.__networkConnect
        
    @networkConnect.setter
    def networkConnect(self, value):
        self.__networkConnect = value
        self.__instanceVersion += 1
        
    @property
    def sentRequest(self):
        """Gets or sets the 'sentRequest' property."""
        return self.__sentRequest
        
    @sentRequest.setter
    def sentRequest(self, value):
        self.__sentRequest = value
        self.__instanceVersion += 1
        
    @property
    def receivedResponse(self):
        """Gets or sets the 'receivedResponse' property."""
        return self.__receivedResponse
        
    @receivedResponse.setter
    def receivedResponse(self, value):
        self.__receivedResponse = value
        self.__instanceVersion += 1
        
    @property
    def domProcessing(self):
        """Gets or sets the 'domProcessing' property."""
        return self.__domProcessing
        
    @domProcessing.setter
    def domProcessing(self, value):
        self.__domProcessing = value
        self.__instanceVersion += 1
        
    def hasChanges(self):
        """Checks if the current instance has changes since its initalization."""
        return self.__instanceVersion != 0
    
    def serialize(self):
        """Serializes the contents of this object and returns the content as a JSON encoded string."""
        output = "{"
        prefix = ""
        if self.__perfTotal != None:
            output += prefix + "\"perfTotal\":"
            output += json.dumps(self.__perfTotal)
            prefix = ","
        if self.__networkConnect != None:
            output += prefix + "\"networkConnect\":"
            output += json.dumps(self.__networkConnect)
            prefix = ","
        if self.__sentRequest != None:
            output += prefix + "\"sentRequest\":"
            output += json.dumps(self.__sentRequest)
            prefix = ","
        if self.__receivedResponse != None:
            output += prefix + "\"receivedResponse\":"
            output += json.dumps(self.__receivedResponse)
            prefix = ","
        if self.__domProcessing != None:
            output += prefix + "\"domProcessing\":"
            output += json.dumps(self.__domProcessing)
        output += "}"
        return output

