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

class TestEventData(unittest.TestCase):
    def test_construct(self):
        item = EventData()
        self.assertNotEqual(item, None)
    
    def test_ver_property_works_as_expected(self):
        expected = 42
        item = EventData()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 13
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_name_property_works_as_expected(self):
        expected = 'Test string'
        item = EventData()
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
    
    def test_properties_property_works_as_expected(self):
        item = EventData()
        actual = item.properties
        self.assertNotEqual(actual, None)
    
    def test_measurements_property_works_as_expected(self):
        item = EventData()
        actual = item.measurements
        self.assertNotEqual(actual, None)
    
    def test_serialize_works_as_expected(self):
        item = EventData()
        item.ver = 42
        item.name = 'Test string'
        for key, value in { 'key1': 'test value 1' , 'key2': 'test value 2' }.items():
            item.properties[key] = value
        for key, value in { 'key1': 3.1415 , 'key2': 42.2 }.items():
            item.measurements[key] = value
        actual = json.dumps(item.write(), separators=(',', ':'), cls=TestJsonEncoder)
        expected = '{"ver":42,"name":"Test string","properties":{"key1":"test value 1","key2":"test value 2"},"measurements":{"key1":3.1415,"key2":42.2}}'
        self.assertEqual(expected, actual)

