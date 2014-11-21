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

class TestExceptionTelemetryStackFrame(unittest.TestCase):
    def test_constructExceptionTelemetryStackFrame(self):
        item = ExceptionTelemetryStackFrame()
        self.assertNotEqual(item, None)
    
    def test_levelPropertyWorksAsExpected(self):
        expected = 42
        item = ExceptionTelemetryStackFrame()
        item.level = expected
        actual = item.level
        self.assertEqual(expected, actual)
        expected = 13
        item.level = expected
        actual = item.level
        self.assertEqual(expected, actual)
    
    def test_methodPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = ExceptionTelemetryStackFrame()
        item.method = expected
        actual = item.method
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.method = expected
        actual = item.method
        self.assertEqual(expected, actual)
    
    def test_assemblyPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = ExceptionTelemetryStackFrame()
        item.assembly = expected
        actual = item.assembly
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.assembly = expected
        actual = item.assembly
        self.assertEqual(expected, actual)
    
    def test_fileNamePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = ExceptionTelemetryStackFrame()
        item.fileName = expected
        actual = item.fileName
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.fileName = expected
        actual = item.fileName
        self.assertEqual(expected, actual)
    
    def test_linePropertyWorksAsExpected(self):
        expected = 42
        item = ExceptionTelemetryStackFrame()
        item.line = expected
        actual = item.line
        self.assertEqual(expected, actual)
        expected = 13
        item.line = expected
        actual = item.line
        self.assertEqual(expected, actual)
    
    def test_serializeMethod(self):
        item = ExceptionTelemetryStackFrame()
        item.level = 42
        item.method = "Test string 1"
        item.assembly = "Test string 1"
        item.fileName = "Test string 1"
        item.line = 42
        actual = item.serialize()
        expected = '{"level":42,"method":"Test string 1","assembly":"Test string 1","fileName":"Test string 1","line":42}'
        self.assertEqual(expected, actual)

