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

class TestDeviceContext(unittest.TestCase):
    def test_constructDeviceContext(self):
        item = DeviceContext()
        self.assertNotEqual(item, None)
    
    def test_typePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = DeviceContext()
        item.type = expected
        actual = item.type
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.type = expected
        actual = item.type
        self.assertEqual(expected, actual)
    
    def test_idPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = DeviceContext()
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
    
    def test_osPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = DeviceContext()
        item.os = expected
        actual = item.os
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.os = expected
        actual = item.os
        self.assertEqual(expected, actual)
    
    def test_osVersionPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = DeviceContext()
        item.osVersion = expected
        actual = item.osVersion
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.osVersion = expected
        actual = item.osVersion
        self.assertEqual(expected, actual)
    
    def test_oemNamePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = DeviceContext()
        item.oemName = expected
        actual = item.oemName
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.oemName = expected
        actual = item.oemName
        self.assertEqual(expected, actual)
    
    def test_modelPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = DeviceContext()
        item.model = expected
        actual = item.model
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.model = expected
        actual = item.model
        self.assertEqual(expected, actual)
    
    def test_networkPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = DeviceContext()
        item.network = expected
        actual = item.network
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.network = expected
        actual = item.network
        self.assertEqual(expected, actual)
    
    def test_resolutionPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = DeviceContext()
        item.resolution = expected
        actual = item.resolution
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.resolution = expected
        actual = item.resolution
        self.assertEqual(expected, actual)
    
    def test_localePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = DeviceContext()
        item.locale = expected
        actual = item.locale
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.locale = expected
        actual = item.locale
        self.assertEqual(expected, actual)
    
    def test_serializeMethod(self):
        item = DeviceContext()
        item.type = "Test string 1"
        item.id = "Test string 1"
        item.os = "Test string 1"
        item.osVersion = "Test string 1"
        item.oemName = "Test string 1"
        item.model = "Test string 1"
        item.network = "Test string 1"
        item.resolution = "Test string 1"
        item.locale = "Test string 1"
        actual = item.serialize()
        expected = '{"type":"Test string 1","id":"Test string 1","os":"Test string 1","osVersion":"Test string 1","oemName":"Test string 1","model":"Test string 1","network":"Test string 1","resolution":"Test string 1","locale":"Test string 1"}'
        self.assertEqual(expected, actual)

