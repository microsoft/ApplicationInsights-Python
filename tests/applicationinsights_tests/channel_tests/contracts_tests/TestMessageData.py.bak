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
        expected = object()
        item = MessageData()
        item.severity_level = expected
        actual = item.severity_level
        self.assertEqual(expected, actual)
        expected = object()
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
        item.severity_level = object()
        for key, value in { 'key1': 'test value 1' , 'key2': 'test value 2' }.items():
            item.properties[key] = value
        actual = json.dumps(item.write(), separators=(',', ':'), cls=TestJsonEncoder)
        expected = '{"ver":42,"message":"Test string","severityLevel":{},"properties":{"key1":"test value 1","key2":"test value 2"}}'
        self.assertEqual(expected, actual)

