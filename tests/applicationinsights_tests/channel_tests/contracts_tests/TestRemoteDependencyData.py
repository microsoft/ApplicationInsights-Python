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
        expected = DataPointType()
        item = RemoteDependencyData()
        item.kind = expected
        actual = item.kind
        self.assertEqual(expected, actual)
        expected = DataPointType()
        item.kind = expected
        actual = item.kind
        self.assertEqual(expected, actual)
    
    def test_value_property_works_as_expected(self):
        expected = 3.14159265358979
        item = RemoteDependencyData()
        item.value = expected
        actual = item.value
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
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
        expected = 3.14159265358979
        item = RemoteDependencyData()
        item.min = expected
        actual = item.min
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
        item.min = expected
        actual = item.min
        self.assertEqual(expected, actual)
    
    def test_max_property_works_as_expected(self):
        expected = 3.14159265358979
        item = RemoteDependencyData()
        item.max = expected
        actual = item.max
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
        item.max = expected
        actual = item.max
        self.assertEqual(expected, actual)
    
    def test_std_dev_property_works_as_expected(self):
        expected = 3.14159265358979
        item = RemoteDependencyData()
        item.std_dev = expected
        actual = item.std_dev
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
        item.std_dev = expected
        actual = item.std_dev
        self.assertEqual(expected, actual)
    
    def test_dependency_kind_property_works_as_expected(self):
        expected = DependencyKind()
        item = RemoteDependencyData()
        item.dependency_kind = expected
        actual = item.dependency_kind
        self.assertEqual(expected, actual)
        expected = DependencyKind()
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
        expected = DependencySourceType()
        item = RemoteDependencyData()
        item.dependency_source = expected
        actual = item.dependency_source
        self.assertEqual(expected, actual)
        expected = DependencySourceType()
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
        item.kind = DataPointType.aggregation
        item.value = 3.14159265358979
        item.count = 42
        item.min = 3.14159265358979
        item.max = 3.14159265358979
        item.std_dev = 3.14159265358979
        item.dependency_kind = DependencyKind.http_any
        item.success = True
        item.async = True
        item.dependency_source = DependencySourceType.apmc
        myItemDictionary =  { 'key1': 'test value 1', 'key2': 'test value 2' }
        for key, value in myItemDictionary.items():
            item.properties[key] = value
        
        actual = json.dumps(item.write())
        expected = '{"ver": 42, "name": "Test string", "kind": 1, "value": 3.14159265358979, "count": 42, "min": 3.14159265358979, "max": 3.14159265358979, "stdDev": 3.14159265358979, "dependencyKind": 2, "async": true, "dependencySource": 2, "properties": {"key1": "test value 1", "key2": "test value 2"}}'
        self.assertEqual(actual, expected)

