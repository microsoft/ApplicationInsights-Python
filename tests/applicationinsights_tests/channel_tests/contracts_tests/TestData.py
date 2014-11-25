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
        expected = Application()
        item = Data()
        item.base_data = expected
        actual = item.base_data
        self.assertEqual(expected, actual)
        expected = Device()
        item.base_data = expected
        actual = item.base_data
        self.assertEqual(expected, actual)
    
    def test_serialize_works_as_expected(self):
        item = Data()
        item.base_type = 'Test string'
        item.base_data = Application()
        actual = json.dumps(item.write())
        expected = '{"baseType": "Test string"}'
        self.assertEqual(actual, expected)

