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

class TestTelemetryEnvelopeData(unittest.TestCase):
    def test_constructTelemetryEnvelopeData(self):
        item = TelemetryEnvelopeData()
        self.assertNotEqual(item, None)
    
    def test_typePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = TelemetryEnvelopeData()
        item.type = expected
        actual = item.type
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.type = expected
        actual = item.type
        self.assertEqual(expected, actual)
    
    def test_itemPropertyWorksAsExpected(self):
        expected = MetricTelemetry()
        item = TelemetryEnvelopeData()
        item.item = expected
        actual = item.item
        self.assertEqual(expected, actual)
        expected = MessageTelemetry()
        item.item = expected
        actual = item.item
        self.assertEqual(expected, actual)
    
    def test_serializeMethod(self):
        item = TelemetryEnvelopeData()
        item.type = "Test string 1"
        item.item = MetricTelemetry()
        actual = item.serialize()
        self.assertNotEqual(actual, None)

