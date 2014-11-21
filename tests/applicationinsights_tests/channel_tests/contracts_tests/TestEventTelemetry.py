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

class TestEventTelemetry(unittest.TestCase):
    def test_constructEventTelemetry(self):
        item = EventTelemetry()
        self.assertNotEqual(item, None)
    
    def test_verPropertyWorksAsExpected(self):
        expected = 42
        item = EventTelemetry()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 13
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_namePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = EventTelemetry()
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
    
    def test_propertiesPropertyWorksAsExpected(self):
        item = EventTelemetry()
        actual = item.properties
        self.assertNotEqual(actual, None)
    
    def test_measurementsPropertyWorksAsExpected(self):
        item = EventTelemetry()
        actual = item.measurements
        self.assertNotEqual(actual, None)
    
    def test_serializeMethod(self):
        item = EventTelemetry()
        item.ver = 42
        item.name = "Test string 1"
        myItemDictionary =  { "key1": "test value 1" }
        for key, value in myItemDictionary.items():
            item.properties[key] = value
        
        myItemDictionary =  { "key1": 3.1415 }
        for key, value in myItemDictionary.items():
            item.measurements[key] = value
        
        actual = item.serialize()
        expected = '{"ver":42,"name":"Test string 1","properties":{"key1": "test value 1"},"measurements":{"key1": 3.1415}}'
        self.assertEqual(expected, actual)

