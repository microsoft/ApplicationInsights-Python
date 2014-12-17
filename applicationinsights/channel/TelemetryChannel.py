import datetime
import json
import locale
import platform
import threading

try:
    import urllib2 as HTTPClient
    from urllib2 import HTTPError
    platform_moniker = 'py2'
except ImportError:
    import urllib.request as HTTPClient
    from urllib.error import HTTPError
    platform_moniker = 'py3'

from applicationinsights.channel import contracts

# set up internal context
internal_context = contracts.Internal()
internal_context.sdk_version = platform_moniker + ':0.2.0'

class TelemetrySender(object):
    """The TelemetrySender is responsible for sending buffered telemetry to the server on a timer"""
    def __init__(self, service_endpoint_uri = 'https://dc.services.visualstudio.com/v2/track'):
        """Initializes a new instance of the TelemetrySender class."""
        if not service_endpoint_uri:
            raise Exception('Service endpoint URI was required but not provided')

        self._service_endpoint_uri = service_endpoint_uri
        self._send_interval_in_milliseconds = 6000
        self._max_queue_item_count = 100
        self._queue = []
        self._timers = []

    @property
    def service_endpoint_uri(self):
        """Gets the serivce endpoint URI property. This is where we send data to."""
        return self._service_endpoint_uri

    @property
    def send_interval_in_milliseconds(self):
        """Gets or sets the send interval after which we will send data to the server. This value is expressed in milliseconds."""
        return self._send_interval_in_milliseconds

    @send_interval_in_milliseconds.setter
    def send_interval_in_milliseconds(self, value):
        """Gets or sets the send interval after which we will send data to the server. This value is expressed in milliseconds."""
        if value < 1000:
            value = 1000
        self._send_interval_in_milliseconds = value

    @property
    def max_queue_item_count(self):
        """Gets or sets the maximum number of items that will be held by the queue before we force a send."""
        return self._max_queue_item_count

    @max_queue_item_count.setter
    def max_queue_item_count(self, value):
        """Gets or sets the maximum number of items that will be held by the queue before we force a send."""
        if value < 1:
            value = 1
        self._max_queue_item_count = value

    def send(self, envelope):
        """Enqueues the specified envelope into our queue. If the queue is full, this function will also trigger a send."""
        self._queue.append(envelope)   
        self._maybe_create_timer() 
         
    def _maybe_create_timer(self):
        if len(self._timers) == 0 or len(self._queue) >= self.max_queue_item_count:
            due_time = self._send_interval_in_milliseconds / 1000.0
            if len(self._queue) >= self.max_queue_item_count:
                due_time = 1 / 1000.0

            timer = threading.Timer(self._send_interval_in_milliseconds / 1000.0, self._schedule_send)
            timer.args.append(timer)
            self._timers.append(timer)
            timer.start()   
                            
    def _schedule_send(self, timer):
        self._send()
        self._timers.remove(timer)
        if len(self._queue) > 0:
            self._maybe_create_timer()

    def _send(self):
        data_to_send = []
        for i in range(len(self._queue)):
            try:
                data_to_send.append(self._queue.pop())
            except IndexError:
                break

        if len(data_to_send) == 0:
            return

        data_to_send.reverse()
        data_to_send = [ a.write() for a in data_to_send ]
        request_payload = json.dumps(data_to_send)
        
        request = HTTPClient.Request(self._service_endpoint_uri, bytearray(request_payload, 'utf-8'), { 'Accept': 'application/json', 'Content-Type' : 'application/json; charset=utf-8' })
        try:
            response = HTTPClient.urlopen(request)
            status_code = response.getcode()
            response_payload = response.read()
            if 200 <= status_code < 300:
                return
        except HTTPError as e:
            if e.getcode() == 400:
                return
        except Exception as e:
            pass

        if len(data_to_send) + len(self._queue) < self._max_queue_item_count:
            # If the unsent amount will put us over the top of the max queue length, drop the data to prevent infinate loops
            # Otherwise, add our unsent data back on to the queue
            for data in data_to_send:
                self._queue.append(data)


class TelemetryChannel(object):
    """The telemetry channel is responsible for constructing an envelope an sending it."""
    def __init__(self, context=None, sender=None):
        """Initializes a new instance of the telemetry channel class."""
        self._context = context
        self._sender = sender or TelemetrySender()

    @property
    def context(self):
        """Gets the global TelemetryContext associated with this client."""
        return self._context

    @property
    def sender(self):
        """Gets the TelemetrySender associated with this client."""
        return self._sender
    
    def write(self, data, context=None):
        """writes the passed in data to the sending queue."""
        local_context = context or self._context
        if not local_context:
            raise Exception('Context was required but not provided')
                 
        if not data:
            raise Exception('Data was required but not provided')

        envelope = contracts.Envelope()
        envelope.name = data.ENVELOPE_TYPE_NAME
        envelope.time = datetime.datetime.utcnow().isoformat() + 'Z'
        envelope.ikey = local_context.instrumentation_key
        tags = envelope.tags
        for key, value in self._write_tags(local_context):
            tags[key] = value
        envelope.data = contracts.Data()
        envelope.data.base_type = data.DATA_TYPE_NAME
        if hasattr(data, 'properties') and local_context.properties:
            properties = data.properties
            if not properties:
                properties = {}
                data.properties = properties
            for key, value in local_context.properties:
                if key not in properties:
                    properties[key] = value
        envelope.data.base_data = data

        self._sender.send(envelope)

    def _write_tags(self, context):
        for item in [ internal_context, context.device, context.application, context.user, context.session, context.location, context.operation ]:
            if not item:
                continue
            for pair in item.write().items():
                yield pair






