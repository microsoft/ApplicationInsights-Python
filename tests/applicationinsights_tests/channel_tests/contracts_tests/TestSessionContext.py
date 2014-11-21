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

class TestSessionContext(unittest.TestCase):
    def test_constructSessionContext(self):
        item = SessionContext()
        self.assertNotEqual(item, None)
    
    def test_idPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = SessionContext()
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
    
    def test_firstSessionPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = SessionContext()
        item.firstSession = expected
        actual = item.firstSession
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.firstSession = expected
        actual = item.firstSession
        self.assertEqual(expected, actual)
    
    def test_serializeMethod(self):
        item = SessionContext()
        item.id = "Test string 1"
        item.firstSession = "Test string 1"
        actual = item.serialize()
        expected = '{"id":"Test string 1","firstSession":"Test string 1"}'
        self.assertEqual(expected, actual)

