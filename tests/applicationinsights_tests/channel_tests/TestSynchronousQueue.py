import unittest

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import channel

class TestSynchronousQueue(unittest.TestCase):
    def test_construct(self):
        actual = channel.SynchronousQueue(MockSynchronousSender())
        self.assertIsNotNone(actual)

    def test_flush_works_as_expected(self):
        sender = MockSynchronousSender()
        queue = channel.SynchronousQueue(sender)
        queue.max_queue_length = 3
        for i in range(1, 8):
            queue.put(i)
        self.assertEqual([[1, 2], [3], [4, 5], [6]], sender.data)
        temp = []
        while queue._queue.qsize() > 0:
            temp.append(queue._queue.get())
        self.assertEqual([7], temp)


class MockSynchronousSender:
    def __init__(self):
        self.send_buffer_size = 2
        self.data = []
        self.queue = None

    def send(self, data_to_send):
        self.data.append(data_to_send)
