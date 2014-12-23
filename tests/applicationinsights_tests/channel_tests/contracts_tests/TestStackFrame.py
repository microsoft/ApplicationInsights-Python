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

class TestStackFrame(unittest.TestCase):
    def test_construct(self):
        item = StackFrame()
        self.assertNotEqual(item, None)
    
    def test_level_property_works_as_expected(self):
        expected = 42
        item = StackFrame()
        item.level = expected
        actual = item.level
        self.assertEqual(expected, actual)
        expected = 13
        item.level = expected
        actual = item.level
        self.assertEqual(expected, actual)
    
    def test_method_property_works_as_expected(self):
        expected = 'Test string'
        item = StackFrame()
        item.method = expected
        actual = item.method
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.method = expected
        actual = item.method
        self.assertEqual(expected, actual)
    
    def test_assembly_property_works_as_expected(self):
        expected = 'Test string'
        item = StackFrame()
        item.assembly = expected
        actual = item.assembly
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.assembly = expected
        actual = item.assembly
        self.assertEqual(expected, actual)
    
    def test_file_name_property_works_as_expected(self):
        expected = 'Test string'
        item = StackFrame()
        item.file_name = expected
        actual = item.file_name
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.file_name = expected
        actual = item.file_name
        self.assertEqual(expected, actual)
    
    def test_line_property_works_as_expected(self):
        expected = 42
        item = StackFrame()
        item.line = expected
        actual = item.line
        self.assertEqual(expected, actual)
        expected = 13
        item.line = expected
        actual = item.line
        self.assertEqual(expected, actual)
    
    def test_serialize_works_as_expected(self):
        item = StackFrame()
        item.level = 42
        item.method = 'Test string'
        item.assembly = 'Test string'
        item.file_name = 'Test string'
        item.line = 42
        actual = json.dumps(item.write(), separators=(',', ':'), cls=TestJsonEncoder)
        expected = '{"level":42,"method":"Test string","assembly":"Test string","fileName":"Test string","line":42}'
        self.assertEqual(expected, actual)

