import threading

from .SenderBase import SenderBase
from threading import Thread


class JoinableAsynchronousSender(SenderBase):
    """An asynchronous sender that works in conjunction with the :class:`AsynchronousQueue`. The sender object will
    start a worker thread that will pull items from the :func:`queue`. The thread will be created immediately and
    started when the client calls :func:`start` and will check for queue items every :func:`send_interval` seconds.
    The worker thread can also be forced to check the queue by flushing the queue.

    - If no items are found, the thread will go back to sleep.
    - If items are found, the worker thread will send items to the specified service in batches of :func:`send_buffer_size`.
    """
    def __init__(self, service_endpoint_uri='https://dc.services.visualstudio.com/v2/track'):
        """Initializes a new instance of the class.

        Args:
            sender (String) service_endpoint_uri the address of the service to send telemetry data to.
        """
        self._send_interval = 1.0
        self._send_time = 3
        self._termination_requested = threading.Event()
        self._thread = None

        SenderBase.__init__(self, service_endpoint_uri)

    @property
    def send_interval(self):
        """The time span in seconds at which the the worker thread will check the :func:`queue` for items (defaults to: 1.0).
        Args:
            value (int) the interval in seconds.
        Returns:
            int. the interval in seconds.
        """
        return self._send_interval

    @send_interval.setter
    def send_interval(self, value):
        """The time span in seconds at which the the worker thread will check the :func:`queue` for items (defaults to: 1.0).
        Args:
            value (int) the interval in seconds.
        Returns:
            int. the interval in seconds.
        """

        if self._thread and self._thread.isAlive():
            raise Exception('Sender thread already started')

        if value < 0.1:
            raise Exception("Interval can't be lower than 100ms")

        self._send_interval = value

    @property
    def send_time(self):
        """The time span in seconds at which the the worker thread will check the :func:`queue` for items (defaults to: 1.0).
        Args:
            value (int) the interval in seconds.
        Returns:
            int. the interval in seconds.
        """
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        """The time span in seconds at which the the worker thread will check the :func:`queue` for items (defaults to: 1.0).
        Args:
            value (int) the interval in seconds.
        Returns:
            int. the interval in seconds.
        """

        if self._thread and self._thread.isAlive():
            raise Exception('Sender thread already started')

        self._send_time = value

    def start(self):
        """Starts a new sender thread if none is not already there
        """
        if self._thread and self._thread.isAlive():
            raise Exception('Sender thread already started')

        self._thread = Thread(target=self._run)
        self._thread.daemon = True
        self._thread.start()

    def stop(self):
        """Gracefully stops the sender thread if one is there.
        Raises runtime error in case sender thread cannot be joined
        """

        self._queue.flush_notification.set()
        self._termination_requested.set()

        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=2*self._send_time)
            self._termination_requested.clear()
            if self._thread.is_alive():
                raise Exception('Could not join sender thread')

    def _run(self):
        try:
            while not self._termination_requested.wait(self.send_interval):
                self.send_all_in_queue()

                # wait at most send_interval (or until we get signalled)
                if self._queue.flush_notification.wait(self._send_interval):
                    self._queue.flush_notification.clear()

            # clear the queue
            self.send_all_in_queue()

        except Exception as e:
            # thread can never die
            print(repr(e))

    def send_all_in_queue(self):
        while True:
            data_chunk = self.get_data_chunk()

            if len(data_chunk) == 0:
                return

            self.send(data_chunk)

    def get_data_chunk(self):
        # get at most send_buffer_size items from the queue
        counter = self._send_buffer_size
        data = []
        while counter > 0:
            item = self.queue.get()
            if not item:
                break
            data.append(item)
            counter -= 1

        return data
