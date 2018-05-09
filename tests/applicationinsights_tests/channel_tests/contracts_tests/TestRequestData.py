import unittest
import datetime
import uuid
import sys
import json

import sys, os, os.path
root_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..', '..')
if root_directory not in sys.path:
    sys.path.append(root_directory)

from applicationinsights.channel.contracts import RequestData
from .Utils import TestJsonEncoder

class TestRequestData(unittest.TestCase):
    def test_construct(self):
        item = RequestData()
        self.assertNotEqual(item, None)
    
    def test_ver_property_works_as_expected(self):
        expected = 42
        item = RequestData()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 13
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_id_property_works_as_expected(self):
        expected = 'Test string'
        item = RequestData()
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
    
    def test_name_property_works_as_expected(self):
        expected = 'Test string'
        item = RequestData()
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
    
    def test_start_time_property_works_as_expected(self):
        expected = 'Test string'
        item = RequestData()
        item.start_time = expected
        actual = item.start_time
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.start_time = expected
        actual = item.start_time
        self.assertEqual(expected, actual)
    
    def test_duration_property_works_as_expected(self):
        expected = 'Test string'
        item = RequestData()
        item.duration = expected
        actual = item.duration
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.duration = expected
        actual = item.duration
        self.assertEqual(expected, actual)
    
    def test_response_code_property_works_as_expected(self):
        expected = 'Test string'
        item = RequestData()
        item.response_code = expected
        actual = item.response_code
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.response_code = expected
        actual = item.response_code
        self.assertEqual(expected, actual)
    
    def test_success_property_works_as_expected(self):
        expected = True
        item = RequestData()
        item.success = expected
        actual = item.success
        self.assertEqual(expected, actual)
        expected = False
        item.success = expected
        actual = item.success
        self.assertEqual(expected, actual)
    
    def test_http_method_property_works_as_expected(self):
        expected = 'Test string'
        item = RequestData()
        item.http_method = expected
        actual = item.http_method
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.http_method = expected
        actual = item.http_method
        self.assertEqual(expected, actual)
    
    def test_url_property_works_as_expected(self):
        expected = 'Test string'
        item = RequestData()
        item.url = expected
        actual = item.url
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.url = expected
        actual = item.url
        self.assertEqual(expected, actual)
    
    def test_properties_property_works_as_expected(self):
        item = RequestData()
        actual = item.properties
        self.assertNotEqual(actual, None)
    
    def test_measurements_property_works_as_expected(self):
        item = RequestData()
        actual = item.measurements
        self.assertNotEqual(actual, None)
    
    def test_serialize_works_as_expected(self):
        item = RequestData()
        item.ver = 42
        item.id = 'Test string'
        item.name = 'Test string'
        item.duration = 'Test string'
        item.response_code = 'Test string'
        item.success = True
        item.url = 'Test string'
        for key, value in { 'key1': 'test value 1' , 'key2': 'test value 2' }.items():
            item.properties[key] = value
        for key, value in { 'key1': 3.1415 , 'key2': 42.2 }.items():
            item.measurements[key] = value
        actual = json.dumps(item.write(), separators=(',', ':'), cls=TestJsonEncoder)
        expected = '{"ver":42,"id":"Test string","name":"Test string","duration":"Test string","responseCode":"Test string","success":true,"url":"Test string","properties":{"key1":"test value 1","key2":"test value 2"},"measurements":{"key1":3.1415,"key2":42.2}}'
        self.assertEqual(expected, actual)

