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

class TestPageViewData(unittest.TestCase):
    def test_construct(self):
        item = PageViewData()
        self.assertNotEqual(item, None)

    def test_ver_property_works_as_expected(self):
        expected = 42
        item = PageViewData()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 13
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_url_property_works_as_expected(self):
        expected = 'Test string'
        item = PageViewData()
        item.url = expected
        actual = item.url
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.url = expected
        actual = item.url
        self.assertEqual(expected, actual)
    
    def test_name_property_works_as_expected(self):
        expected = 'Test string'
        item = PageViewData()
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
    
    def test_duration_property_works_as_expected(self):
        expected = 'Test string'
        item = PageViewData()
        item.duration = expected
        actual = item.duration
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.duration = expected
        actual = item.duration
        self.assertEqual(expected, actual)
    
    def test_properties_property_works_as_expected(self):
        item = PageViewData()
        actual = item.properties
        self.assertNotEqual(actual, None)
    
    def test_measurements_property_works_as_expected(self):
        item = PageViewData()
        actual = item.measurements
        self.assertNotEqual(actual, None)
    
    def test_serialize_works_as_expected(self):
        item = PageViewData()
        item.ver = 42
        item.url = 'Test string'
        item.name = 'Test string'
        item.duration = 'Test string'
        myItemDictionary =  { 'key1': 'test value 1', 'key2': 'test value 2' }
        for key, value in myItemDictionary.items():
            item.properties[key] = value
        
        myItemDictionary =  { 'key1': 3.1415, 'key2': 42.2 }
        for key, value in myItemDictionary.items():
            item.measurements[key] = value
        
        actual = json.dumps(item.write())
        expected = '{"ver": 42, "url": "Test string", "name": "Test string", "duration": "Test string", "properties": {"key1": "test value 1", "key2": "test value 2"}, "measurements": {"key1": 3.1415, "key2": 42.2}}'
        self.assertEqual(expected, actual)

