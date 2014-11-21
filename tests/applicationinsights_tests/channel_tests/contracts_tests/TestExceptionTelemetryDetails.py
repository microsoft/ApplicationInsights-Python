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

class TestExceptionTelemetryDetails(unittest.TestCase):
    def test_constructExceptionTelemetryDetails(self):
        item = ExceptionTelemetryDetails()
        self.assertNotEqual(item, None)
    
    def test_idPropertyWorksAsExpected(self):
        expected = 42
        item = ExceptionTelemetryDetails()
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
        expected = 13
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
    
    def test_outerIdPropertyWorksAsExpected(self):
        expected = 42
        item = ExceptionTelemetryDetails()
        item.outerId = expected
        actual = item.outerId
        self.assertEqual(expected, actual)
        expected = 13
        item.outerId = expected
        actual = item.outerId
        self.assertEqual(expected, actual)
    
    def test_typeNamePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = ExceptionTelemetryDetails()
        item.typeName = expected
        actual = item.typeName
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.typeName = expected
        actual = item.typeName
        self.assertEqual(expected, actual)
    
    def test_messagePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = ExceptionTelemetryDetails()
        item.message = expected
        actual = item.message
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.message = expected
        actual = item.message
        self.assertEqual(expected, actual)
    
    def test_hasFullStackPropertyWorksAsExpected(self):
        expected = True
        item = ExceptionTelemetryDetails()
        item.hasFullStack = expected
        actual = item.hasFullStack
        self.assertEqual(expected, actual)
        expected = False
        item.hasFullStack = expected
        actual = item.hasFullStack
        self.assertEqual(expected, actual)
    
    def test_stackPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = ExceptionTelemetryDetails()
        item.stack = expected
        actual = item.stack
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.stack = expected
        actual = item.stack
        self.assertEqual(expected, actual)
    
    def test_parsedStackPropertyWorksAsExpected(self):
        item = ExceptionTelemetryDetails()
        actual = item.parsedStack
        self.assertNotEqual(actual, None)
    
    def test_serializeMethod(self):
        item = ExceptionTelemetryDetails()
        item.id = 42
        item.outerId = 42
        item.typeName = "Test string 1"
        item.message = "Test string 1"
        item.hasFullStack = True
        item.stack = "Test string 1"
        for value in [ ExceptionTelemetryStackFrame() ]:
            item.parsedStack.append(value)
        
        actual = item.serialize()
        self.assertNotEqual(actual, None)

