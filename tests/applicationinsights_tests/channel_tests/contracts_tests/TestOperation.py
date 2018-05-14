import unittest
import datetime
import uuid
import sys
import json

import sys, os, os.path
root_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..', '..')
if root_directory not in sys.path:
    sys.path.append(root_directory)

from applicationinsights.channel.contracts import Operation
from .Utils import TestJsonEncoder

class TestOperation(unittest.TestCase):
    def test_construct(self):
        item = Operation()
        self.assertNotEqual(item, None)
    
    def test_id_property_works_as_expected(self):
        expected = 'Test string'
        item = Operation()
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
    
    def test_name_property_works_as_expected(self):
        expected = 'Test string'
        item = Operation()
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
    
    def test_parent_id_property_works_as_expected(self):
        expected = 'Test string'
        item = Operation()
        item.parent_id = expected
        actual = item.parent_id
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.parent_id = expected
        actual = item.parent_id
        self.assertEqual(expected, actual)
    
    def test_root_id_property_works_as_expected(self):
        expected = 'Test string'
        item = Operation()
        item.root_id = expected
        actual = item.root_id
        self.assertEqual(expected, actual)
        expected = 'Other string'
    
    def test_serialize_works_as_expected(self):
        item = Operation()
        item.id = 'Test string'
        item.name = 'Test string'
        item.parent_id = 'Test string'
        actual = json.dumps(item.write(), separators=(',', ':'), cls=TestJsonEncoder)
        expected = '{"ai.operation.id":"Test string","ai.operation.name":"Test string","ai.operation.parentId":"Test string"}'
        self.assertEqual(expected, actual)

