from .QueueBase import QueueBase
from threading import Event

class AsynchronousMultiQueue():
    """A queue which uses a round-robin array of AsynchronousQueue objects to increase telemetry throughput
    """
    def __init__(self, num_queues = 8):
        self._queues = []
        self._num_queues = num_queues
        self._next_queue = 0
        for c in range(self._num_queues):
            queue = AsynchronousQueue(sender = AsynchronousSender())
            self._queues.append(queue)
        self._flush_notification = Event()

    @property
    def flush_notification(self):
        """The flush notification :class:`Event` that the :func:`sender` will use to get notified
        that a flush is needed.

        Returns:
            :class:`Event`. object that the :func:`sender` can wait on.
        """
        return self._flush_notification

    def put(self, item):
        """Adds the passed in item object to the queue and notifies the :func:`sender` to start an asynchronous
        send operation by calling :func:`start`.

        Args:
            item (:class:`contracts.Envelope`) the telemetry envelope object to send to the service.
        """
        # rotate which queue we send the event to
        self._queues[self._next_queue].put(item)
        self._next_queue = (self._next_queue + 1) % self._num_queues

    def flush(self):
        """Flushes the current queue by notifying the :func:`sender` via the :func:`flush_notification` event.
        """
        self._flush_notification.set()
        # flush all subqueues
        for c in range(self._num_queues):
            self._queues[c].flush()