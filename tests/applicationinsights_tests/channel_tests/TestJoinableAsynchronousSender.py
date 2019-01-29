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
        sender = channel.JoinableAsynchronousSender()
        self.assertEqual(1.0, sender.send_interval)
        sender.send_interval = 10.0
        self.assertEqual(10.0, sender.send_interval)

    def test_send_time_works_as_expected(self):
        sender = channel.JoinableAsynchronousSender()
        self.assertEqual(3.0, sender.send_time)
        sender.send_time = 10.0
        self.assertEqual(10.0, sender.send_time)

    def test_start(self):
        sender = MockJoinableAsynchronousSender()
        sender.send_interval = 1.0
        sender.send_time = 3.0

        queue = MockJoinableAsynchronousQueue(sender)

        queue.put(1)
        queue.put(2)

        sender.start()
        time.sleep(2.0 * sender.send_time / 3.0)
        queue.put(3)
        time.sleep((1.0 * sender.send_time / 3.0) + 2.0)
        data = sender.data_to_send
        if [[1, 2], [3]] != data and [[1, 2]] != data:
            self.fail('Invalid result')
        get_calls = queue.get_calls
        if 7 != len(get_calls):
            print(get_calls)
            self.fail('Invalid count')

        sender.stop()


class MockJoinableAsynchronousQueue(channel.JoinableAsynchronousQueue):
    def __init__(self, sender):
        self.get_calls = []
        channel.JoinableAsynchronousQueue.__init__(self, sender)

    def get(self):
        output = channel.JoinableAsynchronousQueue.get(self)
        self.get_calls.append((time.gmtime(), output))
        return output


class MockJoinableAsynchronousSender(channel.JoinableAsynchronousSender):
    def __init__(self):
        self.data_to_send = []
        channel.JoinableAsynchronousSender.__init__(self)

    def send(self, data_to_send):
        self.data_to_send.append(data_to_send)
