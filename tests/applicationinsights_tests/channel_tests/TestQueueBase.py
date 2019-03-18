import unittest

import sys, os, os.path
from shutil import rmtree
from tempfile import mkdtemp

rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import channel
from applicationinsights.channel.QueueBase import PersistQueue

class TestQueueBase(unittest.TestCase):
    def test_construct(self):
        sender = MockQueueBaseSender()
        actual = channel.QueueBase(sender)
        self.assertIsNotNone(actual)
        self.assertEqual(500, actual.max_queue_length)
        self.assertEqual(sender, actual.sender)
        self.assertEqual(actual, sender.queue)

    def test_max_queue_length_works_as_expected(self):
        actual = channel.QueueBase(None)
        self.assertEqual(500, actual.max_queue_length)
        actual.max_queue_length = 1000
        self.assertEqual(1000, actual.max_queue_length)
        actual.max_queue_length = -1
        self.assertEqual(1, actual.max_queue_length)

    def test_sender_works_as_expected(self):
        sender = MockQueueBaseSender()
        actual = channel.QueueBase(sender)
        self.assertEqual(sender, actual.sender)

    def test_put_works_as_expected(self):
        actual = InterceptableQueueBase(None)
        actual.max_queue_length = 1
        actual.put(None)
        actual.put(1)
        actual.put(2)
        self.assertEqual(1, actual.get())
        self.assertEqual(2, actual.get())
        self.assertEqual(None, actual.get())
        self.assertEqual(None, actual.get())
        self.assertEqual(2, actual.flush_count)

    def test_get_works_as_expected(self):
        self.test_put_works_as_expected()

    def test_flush_works_as_expected(self):
        self.test_put_works_as_expected()

    @unittest.skipIf(PersistQueue is None, reason='persist-queue missing')
    def test_queue_persistence(self):
        queue = channel.QueueBase(None, self.persistence_directory)
        queue.put(1)
        queue.put(2)
        self.assertEqual(1, queue.get())
        queue.put(3)
        del queue
        queue = channel.QueueBase(None, self.persistence_directory)
        queue.put(4)
        self.assertEqual(2, queue.get())
        self.assertEqual(3, queue.get())
        self.assertEqual(4, queue.get())
        self.assertEqual(None, queue.get())

    @unittest.skipIf(PersistQueue is not None, reason='persist-queue exists')
    def test_queue_persistence_without_dependency(self):
        with self.assertRaises(ValueError):
            channel.QueueBase(None, self.persistence_directory)

    def setUp(self):
        self.persistence_directory = mkdtemp()

    def tearDown(self):
        rmtree(self.persistence_directory)

class InterceptableQueueBase(channel.QueueBase):
    def __init__(self, sender):
        channel.QueueBase.__init__(self, sender)
        self.flush_count = 0

    def flush(self):
        self.flush_count += 1

class MockQueueBaseSender(object):
    def __init__(self):
        self.queue = None