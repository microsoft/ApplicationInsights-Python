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

class TestPageViewTelemetry(unittest.TestCase):
    def test_constructPageViewTelemetry(self):
        item = PageViewTelemetry()
        self.assertNotEqual(item, None)
    
    def test_verPropertyWorksAsExpected(self):
        expected = 42
        item = PageViewTelemetry()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 13
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_urlPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = PageViewTelemetry()
        item.url = expected
        actual = item.url
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.url = expected
        actual = item.url
        self.assertEqual(expected, actual)
    
    def test_pageViewPerfPropertyWorksAsExpected(self):
        expected = PageViewTelemetryPerf()
        item = PageViewTelemetry()
        item.pageViewPerf = expected
        actual = item.pageViewPerf
        self.assertEqual(expected, actual)
        expected = PageViewTelemetryPerf()
        item.pageViewPerf = expected
        actual = item.pageViewPerf
        self.assertEqual(expected, actual)
    
    def test_namePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = PageViewTelemetry()
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
    
    def test_durationPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = PageViewTelemetry()
        item.duration = expected
        actual = item.duration
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.duration = expected
        actual = item.duration
        self.assertEqual(expected, actual)
    
    def test_propertiesPropertyWorksAsExpected(self):
        item = PageViewTelemetry()
        actual = item.properties
        self.assertNotEqual(actual, None)
    
    def test_measurementsPropertyWorksAsExpected(self):
        item = PageViewTelemetry()
        actual = item.measurements
        self.assertNotEqual(actual, None)
    
    def test_serializeMethod(self):
        item = PageViewTelemetry()
        item.ver = 42
        item.url = "Test string 1"
        item.pageViewPerf = PageViewTelemetryPerf()
        item.name = "Test string 1"
        item.duration = "Test string 1"
        myItemDictionary =  { "key1": "test value 1" }
        for key, value in myItemDictionary.items():
            item.properties[key] = value
        
        myItemDictionary =  { "key1": 3.1415 }
        for key, value in myItemDictionary.items():
            item.measurements[key] = value
        
        actual = item.serialize()
        self.assertNotEqual(actual, None)

