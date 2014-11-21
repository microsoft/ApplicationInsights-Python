import datetime
import locale
import platform
import threading
try:
    import urllib2
    from urllib2 import HTTPError
except ImportError:
    import urllib.request as urllib2
    from urllib.error import HTTPError

from applicationinsights.channel import contracts

class TelemetrySender(object):
    """The TelemetrySender is responsible for sending buffered telemetry to the server on a timer"""

    def __init__(self, serviceEndpointUri="http://dc.services.visualstudio.com/v2/track"):
        """Initializes a new instance of the TelemetrySender class."""
        if serviceEndpointUri == None:
            raise Exception("Service endpoint URI was required but not provided")

        self.__serviceEndpointUri = serviceEndpointUri
        self.__sendIntervalInMilliseconds = 6000
        self.__maxQueueItemCount = 100
        self.__sendQueue = []
        self.__timers = []

    @property
    def serviceEndpointUri(self):
        """Gets the serivce endpoint URI property. This is where we send data to."""
        return self.__serviceEndpointUri

    @property
    def sendIntervalInMilliseconds(self):
        """Gets or sets the send interval after which we will send data to the server. This value is expressed in milliseconds."""
        return self.__sendIntervalInMilliseconds

    @sendIntervalInMilliseconds.setter
    def sendIntervalInMilliseconds(self, value):
        """Gets or sets the send interval after which we will send data to the server. This value is expressed in milliseconds."""
        if value < 1000:
            value = 1000
        self.__sendIntervalInMilliseconds = value

    @property
    def maxQueueItemCount(self):
        """Gets or sets the maximum number of items that will be held by the queue before we force a send."""
        return self.__maxQueueItemCount

    @maxQueueItemCount.setter
    def maxQueueItemCount(self, value):
        """Gets or sets the maximum number of items that will be held by the queue before we force a send."""
        if value < 1:
            value = 1
        self.__maxQueueItemCount = value

    def send(self, envelope):
        """Enqueues the specified envelope into our queue. If the queue is full, this function will also trigger a send."""
        self.__sendQueue.append(envelope)   
        self.__maybeCreateTimer() 
         
    def __maybeCreateTimer(self):
        if len(self.__timers) == 0 or len(self.__sendQueue) >= self.maxQueueItemCount:
            dueTime = self.__sendIntervalInMilliseconds / 1000.0
            if len(self.__sendQueue) >= self.maxQueueItemCount:
                dueTime = 1 / 1000.0

            timer = threading.Timer(self.__sendIntervalInMilliseconds / 1000.0, self.__scheduleSend)
            timer.args.append(timer)
            self.__timers.append(timer)
            timer.start()   
                            
    def __scheduleSend(self, timer):
        self.__send()
        self.__timers.remove(timer)
        if len(self.__sendQueue) > 0:
            self.__maybeCreateTimer()

    def __send(self):
        dataToSend = []
        for i in range(len(self.__sendQueue)):
            try:
                dataToSend.append(self.__sendQueue.pop())
            except IndexError:
                break

        if len(dataToSend) == 0:
            return

        dataToSend.reverse()
        first = True
        payload = "["
        for data in dataToSend:
            if not first:
                payload += ","
            first = False

            payload += data.serialize()

        payload += "]"
        
        request = urllib2.Request(self.__serviceEndpointUri, bytearray(payload, "utf-8"), { "Accept": "application/json", "Content-Type" : "application/json; charset=utf-8" })
        try:
            response = urllib2.urlopen(request)
            statusCode = response.getcode()
            responsePayload = response.read()
            if statusCode >= 200 and statusCode < 300:
                return
        except HTTPError as e:
            if e.getcode() == 400:
                return
        except Exception as e:
            pass

        if len(dataToSend) + len(self.__sendQueue) < self.__maxQueueItemCount:
            # If the unsent amount will put us over the top of the max queue length, drop the data to prevent infinate loops
            # Otherwise, add our unsent data back on to the queue
            for data in dataToSend:
                self.__sendQueue.append(data)


class TelemetryChannel(object):
    # The type moniker map. This will map a type of telemetry to metadata needed to construct the envelope.
    __typeMonikerMap = { "EventTelemetry": ("Microsoft.ApplicationInsights.Event", "Microsoft.ApplicationInsights.EventData"),
                         "MetricTelemetry": ("Microsoft.ApplicationInsights.Metric", "Microsoft.ApplicationInsights.MetricData"),
                         "MessageTelemetry": ("Microsoft.ApplicationInsights.Message", "Microsoft.ApplicationInsights.MessageData"),
                         "PageViewTelemetry": ("Microsoft.ApplicationInsights.Pageview", "Microsoft.ApplicationInsights.PageviewData"),
                         "ExceptionTelemetry": ("Microsoft.ApplicationInsights.Exception", "Microsoft.ApplicationInsights.ExceptionData")}
   
    def __init__(self, context=None, sender=None):
        """Initializes a new instance of the telemetry channel class."""
        self.__context = context
        self.__sender = sender
        if not sender or not isinstance(sender, TelemetrySender):
            self.__sender = TelemetrySender()

    @property
    def context(self):
        """Gets the global TelemetryContext associated with this client."""
        return self.__context

    @property
    def sender(self):
        """Gets the TelemetrySender associated with this client."""
        return self.__sender
    
    def write(self, data, context=None):
        """writes the passed in data to the sending queue."""
        localContext = context
        if not localContext:
            localContext = self.__context

        if not localContext:
            raise Exception("Context was required but not provided")
                 
        if not data:
            raise Exception("Data was required but not provided")

        dataType = ""
        if "__class__" in dir(data):
            dataType = data.__class__.__name__
        else:
            raise Exception("Data must be a class")

        typeMonikers = None
        if dataType in self.__typeMonikerMap:
            typeMonikers = self.__typeMonikerMap[dataType]
        else:
            raise Exception("Data is out or range")

        envelope = contracts.TelemetryEnvelope()
        envelope.name = typeMonikers[0]
        envelope.time = datetime.datetime.utcnow().isoformat() + "Z"
        envelope.iKey = localContext.instrumentationKey
        envelope.device = localContext.device
        envelope.application = localContext.application
        envelope.user = localContext.user
        envelope.session = localContext.session
        envelope.location = localContext.location
        envelope.operation = localContext.operation
        envelope.data = contracts.TelemetryEnvelopeData()
        envelope.data.type = typeMonikers[1]
        envelope.data.item = data

        self.__sender.send(envelope)

    





