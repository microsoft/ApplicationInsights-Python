import unittest
import time

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import channel

class TestAsynchronousSender(unittest.TestCase):
    def test_construct(self):
        sender = channel.AsynchronousSender()
        self.assertEqual('https://dc.services.visualstudio.com/v2/track', sender.service_endpoint_uri)
        self.assertEqual(1.0, sender.send_interval)
        self.assertEqual(3.0, sender.send_time)

    def test_send_interval_works_as_expected(self):
        sender = channel.AsynchronousSender()
        self.assertEqual(1.0, sender.send_interval)
        sender.send_interval = 10.0
        self.assertEqual(10.0, sender.send_interval)

    def test_send_time_works_as_expected(self):
        sender = channel.AsynchronousSender()
        self.assertEqual(3.0, sender.send_time)
        sender.send_time = 10.0
        self.assertEqual(10.0, sender.send_time)

    def test_start(self):
        sender = InterceptableAsynchronousSender()
        sender.send_interval = 1.0
        sender.send_time = 3.0
        queue = InterceptableAsynchronousQueue(sender)
        sender.invoke_base_start = False
        queue.put(1)
        queue.put(2)
        sender.invoke_base_start = True
        sender.start()
        time.sleep(2.0 * sender.send_time / 3.0)
        queue.put(3)
        time.sleep((1.0 * sender.send_time / 3.0) + 2.0)
        data = sender.data_to_send
        if [[1, 2], [3]] != data and [[1, 2]] != data:
            self.fail('Invalid result')
        get_calls = queue.get_calls
        if 10 != len(get_calls) and 6 != len(get_calls):
            self.fail('Invalid count')


class InterceptableAsynchronousQueue(channel.AsynchronousQueue):
    def __init__(self, sender):
        self.get_calls = []
        channel.AsynchronousQueue.__init__(self, sender)

    def get(self):
        output = channel.AsynchronousQueue.get(self)
        self.get_calls.append((time.gmtime(), output))
        return output


class InterceptableAsynchronousSender(channel.AsynchronousSender):
    def __init__(self):
        self.data_to_send = []
        self.invoke_base_start = False
        channel.AsynchronousSender.__init__(self)

    def start(self):
        if self.invoke_base_start:
            channel.AsynchronousSender.start(self)

    def send(self, data_to_send):
        self.data_to_send.append(data_to_send)