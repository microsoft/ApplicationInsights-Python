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

class TestInternal(unittest.TestCase):
    def test_construct(self):
        item = Internal()
        self.assertNotEqual(item, None)
    
    def test_sdk_version_property_works_as_expected(self):
        expected = 'Test string'
        item = Internal()
        item.sdk_version = expected
        actual = item.sdk_version
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.sdk_version = expected
        actual = item.sdk_version
        self.assertEqual(expected, actual)
    
    def test_agent_version_property_works_as_expected(self):
        expected = 'Test string'
        item = Internal()
        item.agent_version = expected
        actual = item.agent_version
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.agent_version = expected
        actual = item.agent_version
        self.assertEqual(expected, actual)
    
    def test_serialize_works_as_expected(self):
        item = Internal()
        item.sdk_version = 'Test string'
        item.agent_version = 'Test string'
        actual = json.dumps(item.write(), separators=(',', ':'), cls=TestJsonEncoder)
        expected = '{"ai.internal.sdkVersion":"Test string","ai.internal.agentVersion":"Test string"}'
        self.assertEqual(expected, actual)

