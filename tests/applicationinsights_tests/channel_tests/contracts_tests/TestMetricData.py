import unittest
import datetime
import uuid
import sys
import json

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..', '..')
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights.channel.contracts import *

class TestMetricData(unittest.TestCase):
    def test_construct(self):
        item = MetricData()
        self.assertNotEqual(item, None)

    def test_ver_property_works_as_expected(self):
        expected = 42
        item = MetricData()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 13
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_metrics_property_works_as_expected(self):
        item = MetricData()
        actual = item.metrics
        self.assertNotEqual(actual, None)
    
    def test_properties_property_works_as_expected(self):
        item = MetricData()
        actual = item.properties
        self.assertNotEqual(actual, None)
    
    def test_serialize_works_as_expected(self):
        item = MetricData()
        item.ver = 42
        for value in [ DataPoint() ]:
            item.metrics.append(value)
        
        myItemDictionary =  { 'key1': 'test value 1', 'key2': 'test value 2' }
        for key, value in myItemDictionary.items():
            item.properties[key] = value
        
        actual = json.dumps(item.write())
        expected = '{"ver": 42, "metrics": [{"name": null, "kind": 0, "value": null}], "properties": {"key1": "test value 1", "key2": "test value 2"}}'
        self.assertEqual(actual, expected)

