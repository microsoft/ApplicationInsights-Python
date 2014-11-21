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

class TestExceptionTelemetry(unittest.TestCase):
    def test_constructExceptionTelemetry(self):
        item = ExceptionTelemetry()
        self.assertNotEqual(item, None)
    
    def test_verPropertyWorksAsExpected(self):
        expected = 42
        item = ExceptionTelemetry()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 13
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_handledAtPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = ExceptionTelemetry()
        item.handledAt = expected
        actual = item.handledAt
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.handledAt = expected
        actual = item.handledAt
        self.assertEqual(expected, actual)
    
    def test_exceptionsPropertyWorksAsExpected(self):
        item = ExceptionTelemetry()
        actual = item.exceptions
        self.assertNotEqual(actual, None)
    
    def test_propertiesPropertyWorksAsExpected(self):
        item = ExceptionTelemetry()
        actual = item.properties
        self.assertNotEqual(actual, None)
    
    def test_measurementsPropertyWorksAsExpected(self):
        item = ExceptionTelemetry()
        actual = item.measurements
        self.assertNotEqual(actual, None)
    
    def test_serializeMethod(self):
        item = ExceptionTelemetry()
        item.ver = 42
        item.handledAt = "Test string 1"
        for value in [ ExceptionTelemetryDetails() ]:
            item.exceptions.append(value)
        
        myItemDictionary =  { "key1": "test value 1" }
        for key, value in myItemDictionary.items():
            item.properties[key] = value
        
        myItemDictionary =  { "key1": 3.1415 }
        for key, value in myItemDictionary.items():
            item.measurements[key] = value
        
        actual = item.serialize()
        self.assertNotEqual(actual, None)

