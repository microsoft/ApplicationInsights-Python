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

class TestExceptionData(unittest.TestCase):
    def test_construct(self):
        item = ExceptionData()
        self.assertNotEqual(item, None)

    def test_ver_property_works_as_expected(self):
        expected = 42
        item = ExceptionData()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 13
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_handled_at_property_works_as_expected(self):
        expected = 'Test string'
        item = ExceptionData()
        item.handled_at = expected
        actual = item.handled_at
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.handled_at = expected
        actual = item.handled_at
        self.assertEqual(expected, actual)
    
    def test_exceptions_property_works_as_expected(self):
        item = ExceptionData()
        actual = item.exceptions
        self.assertNotEqual(actual, None)
    
    def test_severity_level_property_works_as_expected(self):
        expected = SeverityLevel.warning
        item = ExceptionData()
        item.severity_level = expected
        actual = item.severity_level
        self.assertEqual(expected, actual)
        expected = SeverityLevel.warning
        item.severity_level = expected
        actual = item.severity_level
        self.assertEqual(expected, actual)
    
    def test_properties_property_works_as_expected(self):
        item = ExceptionData()
        actual = item.properties
        self.assertNotEqual(actual, None)
    
    def test_measurements_property_works_as_expected(self):
        item = ExceptionData()
        actual = item.measurements
        self.assertNotEqual(actual, None)
    
    def test_serialize_works_as_expected(self):
        item = ExceptionData()
        item.ver = 42
        item.handled_at = 'Test string'
        for value in [ ExceptionDetails() ]:
            item.exceptions.append(value)
        
        item.severity_level = SeverityLevel.warning
        myItemDictionary =  { 'key1': 'test value 1', 'key2': 'test value 2' }
        for key, value in myItemDictionary.items():
            item.properties[key] = value
        
        myItemDictionary =  { 'key1': 3.1415, 'key2': 42.2 }
        for key, value in myItemDictionary.items():
            item.measurements[key] = value
        
        actual = json.dumps(item.write())
        expected = '{"ver": 42, "handledAt": "Test string", "exceptions": [{"typeName": null, "message": null, "hasFullStack": true}], "severityLevel": 2, "properties": {"key1": "test value 1", "key2": "test value 2"}, "measurements": {"key1": 3.1415, "key2": 42.2}}'
        self.assertEqual(actual, expected)

