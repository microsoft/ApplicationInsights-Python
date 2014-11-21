import unittest
import datetime
import uuid
import sys
import json

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "..", "..")
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights.channel.contracts import *

class TestOperationContext(unittest.TestCase):
    def test_constructOperationContext(self):
        item = OperationContext()
        self.assertNotEqual(item, None)
    
    def test_idPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = OperationContext()
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
    
    def test_serializeMethod(self):
        item = OperationContext()
        item.id = "Test string 1"
        actual = item.serialize()
        expected = '{"id":"Test string 1"}'
        self.assertEqual(expected, actual)

