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

class TestEnvelope(unittest.TestCase):
    def test_construct(self):
        item = Envelope()
        self.assertNotEqual(item, None)

    def test_ver_property_works_as_expected(self):
        expected = 42
        item = Envelope()
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
        expected = 13
        item.ver = expected
        actual = item.ver
        self.assertEqual(expected, actual)
    
    def test_name_property_works_as_expected(self):
        expected = 'Test string'
        item = Envelope()
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.name = expected
        actual = item.name
        self.assertEqual(expected, actual)
    
    def test_time_property_works_as_expected(self):
        expected = 'Test string'
        item = Envelope()
        item.time = expected
        actual = item.time
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.time = expected
        actual = item.time
        self.assertEqual(expected, actual)
    
    def test_sample_rate_property_works_as_expected(self):
        expected = 3.14159265358979
        item = Envelope()
        item.sample_rate = expected
        actual = item.sample_rate
        self.assertEqual(expected, actual)
        expected = 2.71828182845905
        item.sample_rate = expected
        actual = item.sample_rate
        self.assertEqual(expected, actual)
    
    def test_seq_property_works_as_expected(self):
        expected = 'Test string'
        item = Envelope()
        item.seq = expected
        actual = item.seq
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.seq = expected
        actual = item.seq
        self.assertEqual(expected, actual)
    
    def test_ikey_property_works_as_expected(self):
        expected = 'Test string'
        item = Envelope()
        item.ikey = expected
        actual = item.ikey
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.ikey = expected
        actual = item.ikey
        self.assertEqual(expected, actual)
    
    def test_flags_property_works_as_expected(self):
        expected = 42
        item = Envelope()
        item.flags = expected
        actual = item.flags
        self.assertEqual(expected, actual)
        expected = 13
        item.flags = expected
        actual = item.flags
        self.assertEqual(expected, actual)
    
    def test_device_id_property_works_as_expected(self):
        expected = 'Test string'
        item = Envelope()
        item.device_id = expected
        actual = item.device_id
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.device_id = expected
        actual = item.device_id
        self.assertEqual(expected, actual)
    
    def test_os_property_works_as_expected(self):
        expected = 'Test string'
        item = Envelope()
        item.os = expected
        actual = item.os
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.os = expected
        actual = item.os
        self.assertEqual(expected, actual)
    
    def test_os_ver_property_works_as_expected(self):
        expected = 'Test string'
        item = Envelope()
        item.os_ver = expected
        actual = item.os_ver
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.os_ver = expected
        actual = item.os_ver
        self.assertEqual(expected, actual)
    
    def test_app_id_property_works_as_expected(self):
        expected = 'Test string'
        item = Envelope()
        item.app_id = expected
        actual = item.app_id
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.app_id = expected
        actual = item.app_id
        self.assertEqual(expected, actual)
    
    def test_app_ver_property_works_as_expected(self):
        expected = 'Test string'
        item = Envelope()
        item.app_ver = expected
        actual = item.app_ver
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.app_ver = expected
        actual = item.app_ver
        self.assertEqual(expected, actual)
    
    def test_user_id_property_works_as_expected(self):
        expected = 'Test string'
        item = Envelope()
        item.user_id = expected
        actual = item.user_id
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.user_id = expected
        actual = item.user_id
        self.assertEqual(expected, actual)
    
    def test_tags_property_works_as_expected(self):
        item = Envelope()
        actual = item.tags
        self.assertNotEqual(actual, None)
    
    def test_data_property_works_as_expected(self):
        expected = Data()
        item = Envelope()
        item.data = expected
        actual = item.data
        self.assertEqual(expected, actual)
        expected = Device()
        item.data = expected
        actual = item.data
        self.assertEqual(expected, actual)
    
    def test_serialize_works_as_expected(self):
        item = Envelope()
        item.ver = 42
        item.name = 'Test string'
        item.time = 'Test string'
        item.sample_rate = 3.14159265358979
        item.seq = 'Test string'
        item.ikey = 'Test string'
        item.flags = 42
        item.device_id = 'Test string'
        item.os = 'Test string'
        item.os_ver = 'Test string'
        item.app_id = 'Test string'
        item.app_ver = 'Test string'
        item.user_id = 'Test string'
        myItemDictionary =  { 'key1': 'test value 1', 'key2': 'test value 2' }
        for key, value in myItemDictionary.items():
            item.tags[key] = value
        
        item.data = Data()
        item.data.base_type = 'Test string'
        actual = json.dumps(item.write())
        expected = '{"ver": 42, "name": "Test string", "time": "Test string", "sampleRate": 3.14159265358979, "seq": "Test string", "iKey": "Test string", "flags": 42, "deviceId": "Test string", "os": "Test string", "osVer": "Test string", "appId": "Test string", "appVer": "Test string", "userId": "Test string", "tags": {"key1": "test value 1", "key2": "test value 2"}, "data": {"baseType": "Test string", "baseData": null}}'
        self.assertEqual(actual, expected)

