import unittest
import datetime
import uuid
import sys
import json

import sys, os, os.path
root_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..', '..')
if root_directory not in sys.path:
    sys.path.append(root_directory)

from applicationinsights.channel.contracts import Session
from .Utils import TestJsonEncoder

class TestSession(unittest.TestCase):
    def test_construct(self):
        item = Session()
        self.assertNotEqual(item, None)
    
    def test_id_property_works_as_expected(self):
        expected = 'Test string'
        item = Session()
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
    
    def test_is_first_property_works_as_expected(self):
        expected = 'Test string'
        item = Session()
        item.is_first = expected
        actual = item.is_first
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.is_first = expected
        actual = item.is_first
        self.assertEqual(expected, actual)
    
    def test_is_new_property_works_as_expected(self):
        expected = 'Test string'
        item = Session()
        item.is_new = expected
        actual = item.is_new
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.is_new = expected
        actual = item.is_new
        self.assertEqual(expected, actual)
    
    def test_serialize_works_as_expected(self):
        item = Session()
        item.id = 'Test string'
        item.is_first = 'Test string'
        actual = json.dumps(item.write(), separators=(',', ':'), cls=TestJsonEncoder)
        expected = '{"ai.session.id":"Test string","ai.session.isFirst":"Test string"}'
        self.assertEqual(expected, actual)

