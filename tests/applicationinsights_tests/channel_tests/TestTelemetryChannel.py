import unittest
from test import test_support

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "..")
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import channel

class TestTelemetryChannel(unittest.TestCase):   
    def test_constructTelemetryChannel(self):
        actual = channel.TelemetryChannel()
        self.assertIsNotNone(actual)
    
    def test_constructTelemetryChannelWithContextAndSender(self):
        mockSender = MockTelemetrySender()
        contextGlobal = channel.TelemetryContext()
        actual = channel.TelemetryChannel(contextGlobal, mockSender)
        actual.write(channel.contracts.MessageTelemetry())
        self.assertIsNotNone(mockSender.data)
        self.assertEqual(contextGlobal.device, mockSender.data.device)

    def test_writeWithNoGlobalOrLocalContextRaisesException(self):
        mockSender = MockTelemetrySender()
        actual = channel.TelemetryChannel(None, mockSender)
        self.assertRaises(Exception, actual.write, channel.contracts.MessageTelemetry(), None)
        
    def test_writeWithNoDataRaisesException(self):
        mockSender = MockTelemetrySender()
        actual = channel.TelemetryChannel(None, mockSender)
        self.assertRaises(Exception, actual.write, None)

    def test_writeWithNonClassTypeRaisesException(self):
        mockSender = MockTelemetrySender()
        actual = channel.TelemetryChannel(None, mockSender)
        self.assertRaises(Exception, actual.write, 42)

    def test_writeWithBadTypeRaisesException(self):
        mockSender = MockTelemetrySender()
        actual = channel.TelemetryChannel(None, mockSender)
        self.assertRaises(Exception, actual.write, mockSender)

    def test_writeTransfersLocalConvextOverGlobalContext(self):
        mockSender = MockTelemetrySender()
        contextGlobal = channel.TelemetryContext()
        contextLocal = channel.TelemetryContext()
        actual = channel.TelemetryChannel(contextGlobal, mockSender)
        actual.write(channel.contracts.MessageTelemetry(), contextLocal)
        self.assertIsNotNone(mockSender.data)
        self.assertEqual(contextLocal.device, mockSender.data.device)
 
    def test_writeConstructsValidEnvelope(self):
        mockSender = MockTelemetrySender()
        contextGlobal = channel.TelemetryContext()
        contextGlobal.instrumentationKey = "42"
        actual = channel.TelemetryChannel(contextGlobal, mockSender)        
        cases = [
                    (channel.contracts.EventTelemetry(), "Microsoft.ApplicationInsights.Event", "Microsoft.ApplicationInsights.EventData"),
                    (channel.contracts.MetricTelemetry(), "Microsoft.ApplicationInsights.Metric", "Microsoft.ApplicationInsights.MetricData"),
                    (channel.contracts.MessageTelemetry(), "Microsoft.ApplicationInsights.Message", "Microsoft.ApplicationInsights.MessageData"),
                    (channel.contracts.PageViewTelemetry(), "Microsoft.ApplicationInsights.Pageview", "Microsoft.ApplicationInsights.PageviewData"),
                    (channel.contracts.ExceptionTelemetry(), "Microsoft.ApplicationInsights.Exception", "Microsoft.ApplicationInsights.ExceptionData")
                ]
        for message, typeName1, typeName2 in cases:
            actual.write(message)        
            self.assertIsNotNone(mockSender.data)
            self.assertTrue(isinstance(mockSender.data, channel.contracts.TelemetryEnvelope))
            self.assertEqual(typeName1, mockSender.data.name)
            self.assertIsNotNone(mockSender.data.time)
            self.assertEqual("42", mockSender.data.iKey)
            self.assertEqual(contextGlobal.device, mockSender.data.device)
            self.assertEqual(contextGlobal.application, mockSender.data.application)
            self.assertEqual(contextGlobal.user, mockSender.data.user)
            self.assertEqual(contextGlobal.session, mockSender.data.session)
            self.assertEqual(contextGlobal.location, mockSender.data.location)
            self.assertEqual(contextGlobal.operation, mockSender.data.operation)
            self.assertIsNotNone(mockSender.data.data)
            self.assertEqual(typeName2, mockSender.data.data.type)
            self.assertEqual(message, mockSender.data.data.item)

class MockTelemetrySender(channel.TelemetryChannel().sender.__class__):
    def __init__(self):
        self.data = None

    def send(self, envelope):
        self.data = envelope;
