import unittest

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..')
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import channel

class TestTelemetryChannel(unittest.TestCase):   
    def test_construct(self):
        actual = channel.TelemetryChannel()
        self.assertIsNotNone(actual)

    def test_context_works_as_expected(self):
        context_global = channel.TelemetryContext()
        context_global.device.id = "global"
        actual = channel.TelemetryChannel()
        self.assertIsNotNone(actual.context)
        actual = channel.TelemetryChannel(None)
        self.assertIsNotNone(actual.context)
        actual = channel.TelemetryChannel(context_global)
        self.assertEqual(context_global, actual.context)

    def test_queue_works_as_expected(self):
        queue = object()
        actual = channel.TelemetryChannel()
        self.assertIsNotNone(actual.queue)
        actual = channel.TelemetryChannel(None, None)
        self.assertIsNotNone(actual.queue)
        actual = channel.TelemetryChannel(None, queue)
        self.assertEqual(queue, actual.queue)

    def test_sender_works_as_expected(self):
        actual = channel.TelemetryChannel()
        self.assertIsNotNone(actual.sender)

    def test_flush_works_as_expected(self):
        queue = MockQueue()
        actual = channel.TelemetryChannel(None, queue)
        self.assertEqual(0, queue.flush_count)
        actual.flush()
        self.assertEqual(1, queue.flush_count)

    def test_construct_with_context_and_sender(self):
        mock_sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(mock_sender)
        context_global = channel.TelemetryContext()
        context_global.device.id = "global"
        actual = channel.TelemetryChannel(context_global, queue)
        actual.write(channel.contracts.MessageData())
        actual.flush()
        self.assertIsNotNone(mock_sender.data)
        self.assertEqual("global", mock_sender.data.tags["ai.device.id"])

    def test_write_with_no_data_raises_exception(self):
        mock_sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(mock_sender)
        actual = channel.TelemetryChannel(None, queue)
        self.assertRaises(Exception, actual.write, None)

    def test_write_transfers_local_convext_over_global_context(self):
        mock_sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(mock_sender)
        context_global = channel.TelemetryContext()
        context_global.device.id = "global"
        context_local = channel.TelemetryContext()
        context_local.device.id = "local"
        actual = channel.TelemetryChannel(context_global, queue)
        actual.write(channel.contracts.MessageData(), context_local)
        actual.flush()
        self.assertIsNotNone(mock_sender.data)
        self.assertEqual("local", mock_sender.data.tags["ai.device.id"])

    def test_write_constructs_valid_envelope(self):
        mock_sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(mock_sender)
        context_global = channel.TelemetryContext()
        context_global.instrumentation_key = "42"
        actual = channel.TelemetryChannel(context_global, queue)
        cases = [
                    channel.contracts.EventData(),
                    channel.contracts.MetricData(),
                    channel.contracts.MessageData(),
                    channel.contracts.PageViewData(),
                    channel.contracts.ExceptionData(),
                ]
        for item in cases:
            actual.write(item)
            actual.flush()
            self.assertIsNotNone(mock_sender.data)
            self.assertTrue(isinstance(mock_sender.data, channel.contracts.Envelope))
            self.assertEqual(item.ENVELOPE_TYPE_NAME, mock_sender.data.name)
            self.assertIsNotNone(mock_sender.data.time)
            self.assertEqual("42", mock_sender.data.ikey)
            for key, value in context_global.device.write().items():
                self.assertEqual(value, mock_sender.data.tags[key])
            for key, value in context_global.application.write().items():
                self.assertEqual(value, mock_sender.data.tags[key])
            for key, value in context_global.user.write().items():
                self.assertEqual(value, mock_sender.data.tags[key])
            for key, value in context_global.session.write().items():
                self.assertEqual(value, mock_sender.data.tags[key])
            for key, value in context_global.location.write().items():
                self.assertEqual(value, mock_sender.data.tags[key])
            for key, value in context_global.operation.write().items():
                self.assertEqual(value, mock_sender.data.tags[key])
            self.assertIsNotNone(mock_sender.data.data)
            self.assertEqual(item.DATA_TYPE_NAME, mock_sender.data.data.base_type)
            self.assertEqual(item, mock_sender.data.data.base_data)


class MockQueue(object):
    def __init__(self):
        self.flush_count = 0

    def flush(self):
        self.flush_count += 1


class MockTelemetrySender(channel.TelemetryChannel().sender.__class__):
    def __init__(self):
        self.data = None
        self.send_buffer_size = 1

    def send(self, envelope):
        self.data = envelope[0];
