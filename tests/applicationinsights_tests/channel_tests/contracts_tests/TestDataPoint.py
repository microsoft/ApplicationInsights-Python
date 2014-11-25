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
        expected = DataPointType()
        item = DataPoint()
        item.kind = expected
        actual = item.kind
        self.assertEqual(expected, actual)
        expected = DataPointType()
        item.kind = expected
        actual = item.kind
        self.assertEqual(expected, actual)
    
    def test_value_property_works_as_expected(self):
        expected = 3.14159265358979
        item = DataPoint()
        item.value = expected
        actual = item.value
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
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
        expected = 3.14159265358979
        item = DataPoint()
        item.min = expected
        actual = item.min
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
        item.min = expected
        actual = item.min
        self.assertEqual(expected, actual)
    
    def test_max_property_works_as_expected(self):
        expected = 3.14159265358979
        item = DataPoint()
        item.max = expected
        actual = item.max
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
        item.max = expected
        actual = item.max
        self.assertEqual(expected, actual)
    
    def test_std_dev_property_works_as_expected(self):
        expected = 3.14159265358979
        item = DataPoint()
        item.std_dev = expected
        actual = item.std_dev
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
        item.std_dev = expected
        actual = item.std_dev
        self.assertEqual(expected, actual)
    
    def test_serialize_works_as_expected(self):
        item = DataPoint()
        item.name = 'Test string'
        item.kind = DataPointType.aggregation
        item.value = 3.14159265358979
        item.count = 42
        item.min = 3.14159265358979
        item.max = 3.14159265358979
        item.std_dev = 3.14159265358979
        actual = json.dumps(item.write())
        expected = '{"name": "Test string", "kind": 1, "value": 3.14159265358979, "count": 42, "min": 3.14159265358979, "max": 3.14159265358979, "stdDev": 3.14159265358979}'
        self.assertEqual(actual, expected)

