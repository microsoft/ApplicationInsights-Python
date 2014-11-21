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

class TestRemoteDependencyTelemetry(unittest.TestCase):
    def test_constructRemoteDependencyTelemetry(self):
        item = RemoteDependencyTelemetry()
        self.assertNotEqual(item, None)
    
    def test_namePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = RemoteDependencyTelemetry()
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
    
    def test_dependencyKindPropertyWorksAsExpected(self):
        expected = 42
        item = RemoteDependencyTelemetry()
        item.dependencyKind = expected
        actual = item.dependencyKind
        self.assertEqual(expected, actual)
        expected = 13
        item.dependencyKind = expected
        actual = item.dependencyKind
        self.assertEqual(expected, actual)
    
    def test_valuePropertyWorksAsExpected(self):
        expected = 3.14159265358979
        item = RemoteDependencyTelemetry()
        item.value = expected
        actual = item.value
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
        item.value = expected
        actual = item.value
        self.assertEqual(expected, actual)
    
    def test_resourcePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = RemoteDependencyTelemetry()
        item.resource = expected
        actual = item.resource
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.resource = expected
        actual = item.resource
        self.assertEqual(expected, actual)
    
    def test_kindPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = RemoteDependencyTelemetry()
        item.kind = expected
        actual = item.kind
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.kind = expected
        actual = item.kind
        self.assertEqual(expected, actual)
    
    def test_countPropertyWorksAsExpected(self):
        expected = 42
        item = RemoteDependencyTelemetry()
        item.count = expected
        actual = item.count
        self.assertEqual(expected, actual)
        expected = 13
        item.count = expected
        actual = item.count
        self.assertEqual(expected, actual)
    
    def test_minPropertyWorksAsExpected(self):
        expected = 3.14159265358979
        item = RemoteDependencyTelemetry()
        item.min = expected
        actual = item.min
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
        item.min = expected
        actual = item.min
        self.assertEqual(expected, actual)
    
    def test_maxPropertyWorksAsExpected(self):
        expected = 3.14159265358979
        item = RemoteDependencyTelemetry()
        item.max = expected
        actual = item.max
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
        item.max = expected
        actual = item.max
        self.assertEqual(expected, actual)
    
    def test_stdDevPropertyWorksAsExpected(self):
        expected = 3.14159265358979
        item = RemoteDependencyTelemetry()
        item.stdDev = expected
        actual = item.stdDev
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
        item.stdDev = expected
        actual = item.stdDev
        self.assertEqual(expected, actual)
    
    def test_propertiesPropertyWorksAsExpected(self):
        item = RemoteDependencyTelemetry()
        actual = item.properties
        self.assertNotEqual(actual, None)
    
    def test_measurementsPropertyWorksAsExpected(self):
        item = RemoteDependencyTelemetry()
        actual = item.measurements
        self.assertNotEqual(actual, None)
    
    def test_serializeMethod(self):
        item = RemoteDependencyTelemetry()
        item.name = "Test string 1"
        item.dependencyKind = 42
        item.value = 3.14159265358979
        item.resource = "Test string 1"
        item.kind = "Test string 1"
        item.count = 42
        item.min = 3.14159265358979
        item.max = 3.14159265358979
        item.stdDev = 3.14159265358979
        myItemDictionary =  { "key1": "test value 1" }
        for key, value in myItemDictionary.items():
            item.properties[key] = value
        
        myItemDictionary =  { "key1": 3.1415 }
        for key, value in myItemDictionary.items():
            item.measurements[key] = value
        
        actual = item.serialize()
        expected = '{"name":"Test string 1","dependencyKind":42,"value":3.14159265358979,"resource":"Test string 1","kind":"Test string 1","count":42,"min":3.14159265358979,"max":3.14159265358979,"stdDev":3.14159265358979,"properties":{"key1": "test value 1"},"measurements":{"key1": 3.1415}}'
        self.assertEqual(expected, actual)

