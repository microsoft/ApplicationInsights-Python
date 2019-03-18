import unittest

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import channel

class TestAsynchronousQueue(unittest.TestCase):
    def test_construct(self):
        queue = channel.AsynchronousQueue(MockAsynchronousSender())
        self.assertIsNotNone(queue.flush_notification)

    def test_flush_notification_works_as_expected(self):
        queue = channel.AsynchronousQueue(MockAsynchronousSender())
        self.assertIsNotNone(queue.flush_notification)
        result = queue.flush_notification.wait(1)
        self.assertEqual(False, result)
        queue.flush_notification.set()
        result = queue.flush_notification.wait()
        self.assertEqual(True, result)
        queue.flush_notification.clear()
        result = queue.flush_notification.wait(1)
        self.assertEqual(False, result)

    def test_push_works_As_expected(self):
        sender = MockAsynchronousSender()
        queue = channel.AsynchronousQueue(sender)
        queue.put(42)
        self.assertEqual(1, sender.start_call_count)
        self.assertEqual(42, queue.get())
        self.assertIsNone(queue.get())

    def test_flush_works_as_expected(self):
        sender = MockAsynchronousSender()
        queue = channel.AsynchronousQueue(sender)
        self.assertIsNotNone(queue.flush_notification)
        result = queue.flush_notification.wait(1)
        self.assertEqual(False, result)
        queue.flush()
        self.assertEqual(1, sender.start_call_count)
        result = queue.flush_notification.wait()
        self.assertEqual(True, result)

    def test_with_null_sender(self):
        sender = channel.NullSender()
        queue = channel.AsynchronousQueue(sender)
        queue.put(1)
        queue.put(2)
        queue.flush()


class MockAsynchronousSender:
    def __init__(self):
        self.send_buffer_size = 2
        self.data = []
        self.queue = None
        self.start_call_count = 0

    def start(self):
        self.start_call_count += 1

    def send(self, data_to_send):
        self.data.append(data_to_send)
