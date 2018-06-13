import unittest
import datetime
import uuid
import sys
import json

import sys, os, os.path
root_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..', '..')
if root_directory not in sys.path:
    sys.path.append(root_directory)

from applicationinsights.channel.contracts import RemoteDependencyData
from .Utils import TestJsonEncoder

class TestRemoteDependencyData(unittest.TestCase):
    def test_construct(self):
        item = RemoteDependencyData()
        self.assertNotEqual(item, None)
    
    def test_ver_property_works_as_expected(self):
        expected = 42
        item = RemoteDependencyData()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 13
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_name_property_works_as_expected(self):
        expected = 'Test string'
        item = RemoteDependencyData()
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
    
    def test_kind_property_works_as_expected(self):
        expected = object()
        item = RemoteDependencyData()
        item.kind = expected
        actual = item.kind
        self.assertEqual(expected, actual)
        expected = object()
        item.kind = expected
        actual = item.kind
        self.assertEqual(expected, actual)
    
    def test_value_property_works_as_expected(self):
        expected = 1.5
        item = RemoteDependencyData()
        item.value = expected
        actual = item.value
        self.assertEqual(expected, actual)
        expected = 4.8
        item.value = expected
        actual = item.value
        self.assertEqual(expected, actual)
    
    def test_count_property_works_as_expected(self):
        expected = 42
        item = RemoteDependencyData()
        item.count = expected
        actual = item.count
        self.assertEqual(expected, actual)
        expected = 13
        item.count = expected
        actual = item.count
        self.assertEqual(expected, actual)
    
    def test_min_property_works_as_expected(self):
        expected = 1.5
        item = RemoteDependencyData()
        item.min = expected
        actual = item.min
        self.assertEqual(expected, actual)
        expected = 4.8
        item.min = expected
        actual = item.min
        self.assertEqual(expected, actual)
    
    def test_max_property_works_as_expected(self):
        expected = 1.5
        item = RemoteDependencyData()
        item.max = expected
        actual = item.max
        self.assertEqual(expected, actual)
        expected = 4.8
        item.max = expected
        actual = item.max
        self.assertEqual(expected, actual)
    
    def test_std_dev_property_works_as_expected(self):
        expected = 1.5
        item = RemoteDependencyData()
        item.std_dev = expected
        actual = item.std_dev
        self.assertEqual(expected, actual)
        expected = 4.8
        item.std_dev = expected
        actual = item.std_dev
        self.assertEqual(expected, actual)
    
    def test_dependency_kind_property_works_as_expected(self):
        expected = object()
        item = RemoteDependencyData()
        item.dependency_kind = expected
        actual = item.dependency_kind
        self.assertEqual(expected, actual)
        expected = object()
        item.dependency_kind = expected
        actual = item.dependency_kind
        self.assertEqual(expected, actual)
    
    def test_success_property_works_as_expected(self):
        expected = True
        item = RemoteDependencyData()
        item.success = expected
        actual = item.success
        self.assertEqual(expected, actual)
        expected = False
        item.success = expected
        actual = item.success
        self.assertEqual(expected, actual)
    
    def test_async_property_works_as_expected(self):
        expected = True
        item = RemoteDependencyData()
        item.async = expected
        actual = item.async
        self.assertEqual(expected, actual)
        expected = False
        item.async = expected
        actual = item.async
        self.assertEqual(expected, actual)
    
    def test_dependency_source_property_works_as_expected(self):
        expected = object()
        item = RemoteDependencyData()
        item.dependency_source = expected
        actual = item.dependency_source
        self.assertEqual(expected, actual)
        expected = object()
        item.dependency_source = expected
        actual = item.dependency_source
        self.assertEqual(expected, actual)
    
    def test_properties_property_works_as_expected(self):
        item = RemoteDependencyData()
        actual = item.properties
        self.assertNotEqual(actual, None)
    
    def test_serialize_works_as_expected(self):
        item = RemoteDependencyData()
        item.ver = 42
        item.name = 'Test string'
        item.kind = object()
        item.duration = 1.5
        item.dependency_kind = object()
        item.success = True
        item.async = True
        item.dependency_source = object()
        for key, value in { 'key1': 'test value 1' , 'key2': 'test value 2' }.items():
            item.properties[key] = value
        actual = json.dumps(item.write(), separators=(',', ':'), cls=TestJsonEncoder)
        expected = '{"ver":42,"name":"Test string","duration":1.5,"success":true,"properties":{"key1":"test value 1","key2":"test value 2"}}'
        self.assertEqual(expected, actual)

