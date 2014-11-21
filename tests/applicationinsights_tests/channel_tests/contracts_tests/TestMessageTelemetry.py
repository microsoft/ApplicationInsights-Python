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

class TestMessageTelemetry(unittest.TestCase):
    def test_constructMessageTelemetry(self):
        item = MessageTelemetry()
        self.assertNotEqual(item, None)
    
    def test_verPropertyWorksAsExpected(self):
        expected = 42
        item = MessageTelemetry()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 13
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_messagePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = MessageTelemetry()
        item.message = expected
        actual = item.message
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.message = expected
        actual = item.message
        self.assertEqual(expected, actual)
    
    def test_propertiesPropertyWorksAsExpected(self):
        item = MessageTelemetry()
        actual = item.properties
        self.assertNotEqual(actual, None)
    
    def test_measurementsPropertyWorksAsExpected(self):
        item = MessageTelemetry()
        actual = item.measurements
        self.assertNotEqual(actual, None)
    
    def test_serializeMethod(self):
        item = MessageTelemetry()
        item.ver = 42
        item.message = "Test string 1"
        myItemDictionary =  { "key1": "test value 1" }
        for key, value in myItemDictionary.items():
            item.properties[key] = value
        
        myItemDictionary =  { "key1": 3.1415 }
        for key, value in myItemDictionary.items():
            item.measurements[key] = value
        
        actual = item.serialize()
        expected = '{"ver":42,"message":"Test string 1","properties":{"key1": "test value 1"},"measurements":{"key1": 3.1415}}'
        self.assertEqual(expected, actual)

