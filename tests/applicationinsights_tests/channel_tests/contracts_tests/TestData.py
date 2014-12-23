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

class TestData(unittest.TestCase):
    def test_construct(self):
        item = Data()
        self.assertNotEqual(item, None)
    
    def test_base_type_property_works_as_expected(self):
        expected = 'Test string'
        item = Data()
        item.base_type = expected
        actual = item.base_type
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.base_type = expected
        actual = item.base_type
        self.assertEqual(expected, actual)
    
    def test_base_data_property_works_as_expected(self):
        expected = object()
        item = Data()
        item.base_data = expected
        actual = item.base_data
        self.assertEqual(expected, actual)
        expected = object()
        item.base_data = expected
        actual = item.base_data
        self.assertEqual(expected, actual)
    
    def test_serialize_works_as_expected(self):
        item = Data()
        item.base_type = 'Test string'
        item.base_data = object()
        actual = json.dumps(item.write(), separators=(',', ':'), cls=TestJsonEncoder)
        expected = '{"baseType":"Test string","baseData":{}}'
        self.assertEqual(expected, actual)

