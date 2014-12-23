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

class TestDataPoint(unittest.TestCase):
    def test_construct(self):
        item = DataPoint()
        self.assertNotEqual(item, None)
    
    def test_name_property_works_as_expected(self):
        expected = 'Test string'
        item = DataPoint()
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
    
    def test_kind_property_works_as_expected(self):
        expected = object()
        item = DataPoint()
        item.kind = expected
        actual = item.kind
        self.assertEqual(expected, actual)
        expected = object()
        item.kind = expected
        actual = item.kind
        self.assertEqual(expected, actual)
    
    def test_value_property_works_as_expected(self):
        expected = 1.5
        item = DataPoint()
        item.value = expected
        actual = item.value
        self.assertEqual(expected, actual)
        expected = 4.8
        item.value = expected
        actual = item.value
        self.assertEqual(expected, actual)
    
    def test_count_property_works_as_expected(self):
        expected = 42
        item = DataPoint()
        item.count = expected
        actual = item.count
        self.assertEqual(expected, actual)
        expected = 13
        item.count = expected
        actual = item.count
        self.assertEqual(expected, actual)
    
    def test_min_property_works_as_expected(self):
        expected = 1.5
        item = DataPoint()
        item.min = expected
        actual = item.min
        self.assertEqual(expected, actual)
        expected = 4.8
        item.min = expected
        actual = item.min
        self.assertEqual(expected, actual)
    
    def test_max_property_works_as_expected(self):
        expected = 1.5
        item = DataPoint()
        item.max = expected
        actual = item.max
        self.assertEqual(expected, actual)
        expected = 4.8
        item.max = expected
        actual = item.max
        self.assertEqual(expected, actual)
    
    def test_std_dev_property_works_as_expected(self):
        expected = 1.5
        item = DataPoint()
        item.std_dev = expected
        actual = item.std_dev
        self.assertEqual(expected, actual)
        expected = 4.8
        item.std_dev = expected
        actual = item.std_dev
        self.assertEqual(expected, actual)
    
    def test_serialize_works_as_expected(self):
        item = DataPoint()
        item.name = 'Test string'
        item.kind = object()
        item.value = 1.5
        item.count = 42
        item.min = 1.5
        item.max = 1.5
        item.std_dev = 1.5
        actual = json.dumps(item.write(), separators=(',', ':'), cls=TestJsonEncoder)
        expected = '{"name":"Test string","kind":{},"value":1.5,"count":42,"min":1.5,"max":1.5,"stdDev":1.5}'
        self.assertEqual(expected, actual)

