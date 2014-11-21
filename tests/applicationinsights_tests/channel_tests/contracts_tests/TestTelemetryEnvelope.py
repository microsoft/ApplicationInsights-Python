import unittest
import datetime
import uuid
import sys
import json

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "..", "..")
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights.channel.contracts import *

class TestTelemetryEnvelope(unittest.TestCase):
    def test_constructTelemetryEnvelope(self):
        item = TelemetryEnvelope()
        self.assertNotEqual(item, None)
    
    def test_verPropertyWorksAsExpected(self):
        expected = 42
        item = TelemetryEnvelope()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 13
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_namePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = TelemetryEnvelope()
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
    
    def test_timePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = TelemetryEnvelope()
        item.time = expected
        actual = item.time
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.time = expected
        actual = item.time
        self.assertEqual(expected, actual)
    
    def test_iKeyPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = TelemetryEnvelope()
        item.iKey = expected
        actual = item.iKey
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.iKey = expected
        actual = item.iKey
        self.assertEqual(expected, actual)
    
    def test_applicationPropertyWorksAsExpected(self):
        expected = ApplicationContext()
        item = TelemetryEnvelope()
        item.application = expected
        actual = item.application
        self.assertEqual(expected, actual)
        expected = ApplicationContext()
        item.application = expected
        actual = item.application
        self.assertEqual(expected, actual)
    
    def test_devicePropertyWorksAsExpected(self):
        expected = DeviceContext()
        item = TelemetryEnvelope()
        item.device = expected
        actual = item.device
        self.assertEqual(expected, actual)
        expected = DeviceContext()
        item.device = expected
        actual = item.device
        self.assertEqual(expected, actual)
    
    def test_userPropertyWorksAsExpected(self):
        expected = UserContext()
        item = TelemetryEnvelope()
        item.user = expected
        actual = item.user
        self.assertEqual(expected, actual)
        expected = UserContext()
        item.user = expected
        actual = item.user
        self.assertEqual(expected, actual)
    
    def test_sessionPropertyWorksAsExpected(self):
        expected = SessionContext()
        item = TelemetryEnvelope()
        item.session = expected
        actual = item.session
        self.assertEqual(expected, actual)
        expected = SessionContext()
        item.session = expected
        actual = item.session
        self.assertEqual(expected, actual)
    
    def test_locationPropertyWorksAsExpected(self):
        expected = LocationContext()
        item = TelemetryEnvelope()
        item.location = expected
        actual = item.location
        self.assertEqual(expected, actual)
        expected = LocationContext()
        item.location = expected
        actual = item.location
        self.assertEqual(expected, actual)
    
    def test_operationPropertyWorksAsExpected(self):
        expected = OperationContext()
        item = TelemetryEnvelope()
        item.operation = expected
        actual = item.operation
        self.assertEqual(expected, actual)
        expected = OperationContext()
        item.operation = expected
        actual = item.operation
        self.assertEqual(expected, actual)
    
    def test_dataPropertyWorksAsExpected(self):
        expected = TelemetryEnvelopeData()
        item = TelemetryEnvelope()
        item.data = expected
        actual = item.data
        self.assertEqual(expected, actual)
        expected = TelemetryEnvelopeData()
        item.data = expected
        actual = item.data
        self.assertEqual(expected, actual)
    
    def test_serializeMethod(self):
        item = TelemetryEnvelope()
        item.ver = 42
        item.name = "Test string 1"
        item.time = "Test string 1"
        item.iKey = "Test string 1"
        item.application = ApplicationContext()
        item.device = DeviceContext()
        item.user = UserContext()
        item.session = SessionContext()
        item.location = LocationContext()
        item.operation = OperationContext()
        item.data = TelemetryEnvelopeData()
        actual = item.serialize()
        self.assertNotEqual(actual, None)

