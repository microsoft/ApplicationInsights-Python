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

class TestMetricTelemetry(unittest.TestCase):
    def test_constructMetricTelemetry(self):
        item = MetricTelemetry()
        self.assertNotEqual(item, None)
    
    def test_verPropertyWorksAsExpected(self):
        expected = 42
        item = MetricTelemetry()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 13
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_metricsPropertyWorksAsExpected(self):
        item = MetricTelemetry()
        actual = item.metrics
        self.assertNotEqual(actual, None)
    
    def test_propertiesPropertyWorksAsExpected(self):
        item = MetricTelemetry()
        actual = item.properties
        self.assertNotEqual(actual, None)
    
    def test_serializeMethod(self):
        item = MetricTelemetry()
        item.ver = 42
        for value in [ MetricTelemetryDataPoint() ]:
            item.metrics.append(value)
        
        myItemDictionary =  { "key1": "test value 1" }
        for key, value in myItemDictionary.items():
            item.properties[key] = value
        
        actual = item.serialize()
        self.assertNotEqual(actual, None)

