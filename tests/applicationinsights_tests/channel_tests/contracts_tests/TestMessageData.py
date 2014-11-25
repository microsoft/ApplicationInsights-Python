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

class TestMessageData(unittest.TestCase):
    def test_construct(self):
        item = MessageData()
        self.assertNotEqual(item, None)

    def test_ver_property_works_as_expected(self):
        expected = 42
        item = MessageData()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 13
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_message_property_works_as_expected(self):
        expected = 'Test string'
        item = MessageData()
        item.message = expected
        actual = item.message
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.message = expected
        actual = item.message
        self.assertEqual(expected, actual)
    
    def test_severity_level_property_works_as_expected(self):
        expected = SeverityLevel.verbose
        item = MessageData()
        item.severity_level = expected
        actual = item.severity_level
        self.assertEqual(expected, actual)
        expected = SeverityLevel.warning
        item.severity_level = expected
        actual = item.severity_level
        self.assertEqual(expected, actual)
    
    def test_properties_property_works_as_expected(self):
        item = MessageData()
        actual = item.properties
        self.assertNotEqual(actual, None)
    
    def test_serialize_works_as_expected(self):
        item = MessageData()
        item.ver = 42
        item.message = 'Test string'
        item.severity_level = SeverityLevel.warning
        myItemDictionary =  { 'key1': 'test value 1', 'key2': 'test value 2' }
        for key, value in myItemDictionary.items():
            item.properties[key] = value
        
        actual = json.dumps(item.write())
        expected = '{"ver": 42, "message": "Test string", "severityLevel": 2, "properties": {"key1": "test value 1", "key2": "test value 2"}}'
        self.assertEqual(actual, expected)

