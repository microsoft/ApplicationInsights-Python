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

class TestExceptionDetails(unittest.TestCase):
    def test_construct(self):
        item = ExceptionDetails()
        self.assertNotEqual(item, None)
    
    def test_id_property_works_as_expected(self):
        expected = 42
        item = ExceptionDetails()
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
        expected = 13
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
    
    def test_outer_id_property_works_as_expected(self):
        expected = 42
        item = ExceptionDetails()
        item.outer_id = expected
        actual = item.outer_id
        self.assertEqual(expected, actual)
        expected = 13
        item.outer_id = expected
        actual = item.outer_id
        self.assertEqual(expected, actual)
    
    def test_type_name_property_works_as_expected(self):
        expected = 'Test string'
        item = ExceptionDetails()
        item.type_name = expected
        actual = item.type_name
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.type_name = expected
        actual = item.type_name
        self.assertEqual(expected, actual)
    
    def test_message_property_works_as_expected(self):
        expected = 'Test string'
        item = ExceptionDetails()
        item.message = expected
        actual = item.message
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.message = expected
        actual = item.message
        self.assertEqual(expected, actual)
    
    def test_has_full_stack_property_works_as_expected(self):
        expected = True
        item = ExceptionDetails()
        item.has_full_stack = expected
        actual = item.has_full_stack
        self.assertEqual(expected, actual)
        expected = False
        item.has_full_stack = expected
        actual = item.has_full_stack
        self.assertEqual(expected, actual)
    
    def test_stack_property_works_as_expected(self):
        expected = 'Test string'
        item = ExceptionDetails()
        item.stack = expected
        actual = item.stack
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.stack = expected
        actual = item.stack
        self.assertEqual(expected, actual)
    
    def test_parsed_stack_property_works_as_expected(self):
        item = ExceptionDetails()
        actual = item.parsed_stack
        self.assertNotEqual(actual, None)
    
    def test_serialize_works_as_expected(self):
        item = ExceptionDetails()
        item.id = 42
        item.outer_id = 42
        item.type_name = 'Test string'
        item.message = 'Test string'
        item.has_full_stack = True
        item.stack = 'Test string'
        for value in [ object() ]:
            item.parsed_stack.append(value)
        
        actual = json.dumps(item.write(), separators=(',', ':'), cls=TestJsonEncoder)
        expected = '{"id":42,"outerId":42,"typeName":"Test string","message":"Test string","hasFullStack":true,"stack":"Test string","parsedStack":[{}]}'
        self.assertEqual(expected, actual)

