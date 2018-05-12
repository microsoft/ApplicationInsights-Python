import unittest
import datetime
import uuid
import sys
import json

import sys, os, os.path
root_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..', '..')
if root_directory not in sys.path:
    sys.path.append(root_directory)

from applicationinsights.channel.contracts import Device
from .Utils import TestJsonEncoder

class TestDevice(unittest.TestCase):
    def test_construct(self):
        item = Device()
        self.assertNotEqual(item, None)
    
    def test_id_property_works_as_expected(self):
        expected = 'Test string'
        item = Device()
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
    
    def test_ip_property_works_as_expected(self):
        expected = 'Test string'
        item = Device()
        item.ip = expected
        actual = item.ip
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.ip = expected
        actual = item.ip
        self.assertEqual(expected, actual)
    
    def test_language_property_works_as_expected(self):
        expected = 'Test string'
        item = Device()
        item.language = expected
        actual = item.language
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.language = expected
        actual = item.language
        self.assertEqual(expected, actual)
    
    def test_locale_property_works_as_expected(self):
        expected = 'Test string'
        item = Device()
        item.locale = expected
        actual = item.locale
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.locale = expected
        actual = item.locale
        self.assertEqual(expected, actual)
    
    def test_model_property_works_as_expected(self):
        expected = 'Test string'
        item = Device()
        item.model = expected
        actual = item.model
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.model = expected
        actual = item.model
        self.assertEqual(expected, actual)
    
    def test_network_property_works_as_expected(self):
        expected = 'Test string'
        item = Device()
        item.network = expected
        actual = item.network
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.network = expected
        actual = item.network
        self.assertEqual(expected, actual)
    
    def test_oem_name_property_works_as_expected(self):
        expected = 'Test string'
        item = Device()
        item.oem_name = expected
        actual = item.oem_name
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.oem_name = expected
        actual = item.oem_name
        self.assertEqual(expected, actual)
    
    def test_os_property_works_as_expected(self):
        expected = 'Test string'
        item = Device()
        item.os = expected
        actual = item.os
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.os = expected
        actual = item.os
        self.assertEqual(expected, actual)
    
    def test_os_version_property_works_as_expected(self):
        expected = 'Test string'
        item = Device()
        item.os_version = expected
        actual = item.os_version
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.os_version = expected
        actual = item.os_version
        self.assertEqual(expected, actual)
    
    def test_role_instance_property_works_as_expected(self):
        expected = 'Test string'
        item = Device()
        item.role_instance = expected
        actual = item.role_instance
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.role_instance = expected
        actual = item.role_instance
        self.assertEqual(expected, actual)
    
    def test_role_name_property_works_as_expected(self):
        expected = 'Test string'
        item = Device()
        item.role_name = expected
        actual = item.role_name
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.role_name = expected
        actual = item.role_name
        self.assertEqual(expected, actual)
    
    def test_screen_resolution_property_works_as_expected(self):
        expected = 'Test string'
        item = Device()
        item.screen_resolution = expected
        actual = item.screen_resolution
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.screen_resolution = expected
        actual = item.screen_resolution
        self.assertEqual(expected, actual)
    
    def test_type_property_works_as_expected(self):
        expected = 'Test string'
        item = Device()
        item.type = expected
        actual = item.type
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.type = expected
        actual = item.type
        self.assertEqual(expected, actual)
    
    def test_vm_name_property_works_as_expected(self):
        expected = 'Test string'
        item = Device()
        item.vm_name = expected
        actual = item.vm_name
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.vm_name = expected
        actual = item.vm_name
        self.assertEqual(expected, actual)
    
    def test_serialize_works_as_expected(self):
        item = Device()
        item.id = 'Test string'
        item.locale = 'Test string'
        item.model = 'Test string'
        item.oem_name = 'Test string'
        item.os_version = 'Test string'
        item.type = 'Test string'
        actual = json.dumps(item.write(), separators=(',', ':'), cls=TestJsonEncoder)
        expected = '{"ai.device.id":"Test string","ai.device.locale":"Test string","ai.device.model":"Test string","ai.device.oemName":"Test string","ai.device.osVersion":"Test string","ai.device.type":"Test string"}'
        self.assertEqual(expected, actual)

