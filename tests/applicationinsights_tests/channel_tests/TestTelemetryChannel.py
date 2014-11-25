import unittest
from test import test_support

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..')
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import channel

class TestTelemetryChannel(unittest.TestCase):   
    def test_construct(self):
        actual = channel.TelemetryChannel()
        self.assertIsNotNone(actual)
    
    def test_construct_with_context_and_sender(self):
        mock_sender = MockTelemetrySender()
        context_global = channel.TelemetryContext()
        context_global.device.id = "global"
        actual = channel.TelemetryChannel(context_global, mock_sender)
        actual.write(channel.contracts.MessageData())
        self.assertIsNotNone(mock_sender.data)
        self.assertEqual("global", mock_sender.data.tags["ai.device.id"])

    def test_write_with_no_global_or_local_context_raises_exception(self):
        mock_sender = MockTelemetrySender()
        actual = channel.TelemetryChannel(None, mock_sender)
        self.assertRaises(Exception, actual.write, channel.contracts.MessageData(), None)
        
    def test_write_with_no_data_raises_exception(self):
        mock_sender = MockTelemetrySender()
        actual = channel.TelemetryChannel(None, mock_sender)
        self.assertRaises(Exception, actual.write, None)

    def test_write_transfers_local_convext_over_global_context(self):
        mock_sender = MockTelemetrySender()
        context_global = channel.TelemetryContext()
        context_global.device.id = "global"
        context_local = channel.TelemetryContext()
        context_local.device.id = "local"
        actual = channel.TelemetryChannel(context_global, mock_sender)
        actual.write(channel.contracts.MessageData(), context_local)
        self.assertIsNotNone(mock_sender.data)
        self.assertEqual("local", mock_sender.data.tags["ai.device.id"])
 
    def test_write_constructs_valid_envelope(self):
        mock_sender = MockTelemetrySender()
        context_global = channel.TelemetryContext()
        context_global.instrumentation_key = "42"
        actual = channel.TelemetryChannel(context_global, mock_sender)        
        cases = [
                    channel.contracts.EventData(),
                    channel.contracts.MetricData(),
                    channel.contracts.MessageData(),
                    channel.contracts.PageViewData(),
                    channel.contracts.ExceptionData(),
                ]
        for item in cases:
            actual.write(item)        
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

class MockTelemetrySender(channel.TelemetryChannel().sender.__class__):
    def __init__(self):
        self.data = None

    def send(self, envelope):
        self.data = envelope;
