import unittest
import datetime
import uuid
import sys
import json

import sys, os, os.path
root_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..', '..')
if root_directory not in sys.path:
    sys.path.append(root_directory)

from applicationinsights.channel.contracts import *
from .Utils import TestJsonEncoder

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
        for value in [ object() ]:
            item.metrics.append(value)
        
        for key, value in { 'key1': 'test value 1' , 'key2': 'test value 2' }.items():
            item.properties[key] = value
        actual = json.dumps(item.write(), separators=(',', ':'), cls=TestJsonEncoder)
        expected = '{"ver":42,"metrics":[{}],"properties":{"key1":"test value 1","key2":"test value 2"}}'
        self.assertEqual(expected, actual)

