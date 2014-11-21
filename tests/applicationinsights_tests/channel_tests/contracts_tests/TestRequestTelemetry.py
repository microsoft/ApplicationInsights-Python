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

class TestRequestTelemetry(unittest.TestCase):
    def test_constructRequestTelemetry(self):
        item = RequestTelemetry()
        self.assertNotEqual(item, None)
    
    def test_verPropertyWorksAsExpected(self):
        expected = 42
        item = RequestTelemetry()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 13
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_namePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = RequestTelemetry()
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
    
    def test_idPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = RequestTelemetry()
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
    
    def test_startTimePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = RequestTelemetry()
        item.startTime = expected
        actual = item.startTime
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.startTime = expected
        actual = item.startTime
        self.assertEqual(expected, actual)
    
    def test_durationPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = RequestTelemetry()
        item.duration = expected
        actual = item.duration
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.duration = expected
        actual = item.duration
        self.assertEqual(expected, actual)
    
    def test_responseCodePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = RequestTelemetry()
        item.responseCode = expected
        actual = item.responseCode
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.responseCode = expected
        actual = item.responseCode
        self.assertEqual(expected, actual)
    
    def test_successPropertyWorksAsExpected(self):
        expected = True
        item = RequestTelemetry()
        item.success = expected
        actual = item.success
        self.assertEqual(expected, actual)
        expected = False
        item.success = expected
        actual = item.success
        self.assertEqual(expected, actual)
    
    def test_propertiesPropertyWorksAsExpected(self):
        item = RequestTelemetry()
        actual = item.properties
        self.assertNotEqual(actual, None)
    
    def test_measurementsPropertyWorksAsExpected(self):
        item = RequestTelemetry()
        actual = item.measurements
        self.assertNotEqual(actual, None)
    
    def test_serializeMethod(self):
        item = RequestTelemetry()
        item.ver = 42
        item.name = "Test string 1"
        item.id = "Test string 1"
        item.startTime = "Test string 1"
        item.duration = "Test string 1"
        item.responseCode = "Test string 1"
        item.success = True
        myItemDictionary =  { "key1": "test value 1" }
        for key, value in myItemDictionary.items():
            item.properties[key] = value
        
        myItemDictionary =  { "key1": 3.1415 }
        for key, value in myItemDictionary.items():
            item.measurements[key] = value
        
        actual = item.serialize()
        expected = '{"ver":42,"name":"Test string 1","id":"Test string 1","startTime":"Test string 1","duration":"Test string 1","responseCode":"Test string 1","success":true,"properties":{"key1": "test value 1"},"measurements":{"key1": 3.1415}}'
        self.assertEqual(expected, actual)

