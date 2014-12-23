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

class TestApplication(unittest.TestCase):
    def test_construct(self):
        item = Application()
        self.assertNotEqual(item, None)
    
    def test_ver_property_works_as_expected(self):
        expected = 'Test string'
        item = Application()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_serialize_works_as_expected(self):
        item = Application()
        item.ver = 'Test string'
        actual = json.dumps(item.write(), separators=(',', ':'), cls=TestJsonEncoder)
        expected = '{"ai.application.ver":"Test string"}'
        self.assertEqual(expected, actual)

