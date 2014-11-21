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

class TestMetricTelemetryDataPoint(unittest.TestCase):
    def test_constructMetricTelemetryDataPoint(self):
        item = MetricTelemetryDataPoint()
        self.assertNotEqual(item, None)
    
    def test_namePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = MetricTelemetryDataPoint()
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
    
    def test_valuePropertyWorksAsExpected(self):
        expected = 3.14159265358979
        item = MetricTelemetryDataPoint()
        item.value = expected
        actual = item.value
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
        item.value = expected
        actual = item.value
        self.assertEqual(expected, actual)
    
    def test_kindPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = MetricTelemetryDataPoint()
        item.kind = expected
        actual = item.kind
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.kind = expected
        actual = item.kind
        self.assertEqual(expected, actual)
    
    def test_countPropertyWorksAsExpected(self):
        expected = 42
        item = MetricTelemetryDataPoint()
        item.count = expected
        actual = item.count
        self.assertEqual(expected, actual)
        expected = 13
        item.count = expected
        actual = item.count
        self.assertEqual(expected, actual)
    
    def test_minPropertyWorksAsExpected(self):
        expected = 3.14159265358979
        item = MetricTelemetryDataPoint()
        item.min = expected
        actual = item.min
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
        item.min = expected
        actual = item.min
        self.assertEqual(expected, actual)
    
    def test_maxPropertyWorksAsExpected(self):
        expected = 3.14159265358979
        item = MetricTelemetryDataPoint()
        item.max = expected
        actual = item.max
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
        item.max = expected
        actual = item.max
        self.assertEqual(expected, actual)
    
    def test_stdDevPropertyWorksAsExpected(self):
        expected = 3.14159265358979
        item = MetricTelemetryDataPoint()
        item.stdDev = expected
        actual = item.stdDev
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
        item.stdDev = expected
        actual = item.stdDev
        self.assertEqual(expected, actual)
    
    def test_serializeMethod(self):
        item = MetricTelemetryDataPoint()
        item.name = "Test string 1"
        item.value = 3.14159265358979
        item.kind = "Test string 1"
        item.count = 42
        item.min = 3.14159265358979
        item.max = 3.14159265358979
        item.stdDev = 3.14159265358979
        actual = item.serialize()
        expected = '{"name":"Test string 1","value":3.14159265358979,"kind":"Test string 1","count":42,"min":3.14159265358979,"max":3.14159265358979,"stdDev":3.14159265358979}'
        self.assertEqual(expected, actual)

