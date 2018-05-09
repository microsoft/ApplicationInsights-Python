import unittest
import datetime
import uuid
import sys
import json

import sys, os, os.path
root_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..', '..')
if root_directory not in sys.path:
    sys.path.append(root_directory)

from applicationinsights.channel.contracts import User
from .Utils import TestJsonEncoder

class TestUser(unittest.TestCase):
    def test_construct(self):
        item = User()
        self.assertNotEqual(item, None)
    
    def test_account_acquisition_date_property_works_as_expected(self):
        expected = 'Test string'
        item = User()
        item.account_acquisition_date = expected
        actual = item.account_acquisition_date
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.account_acquisition_date = expected
        actual = item.account_acquisition_date
        self.assertEqual(expected, actual)
    
    def test_account_id_property_works_as_expected(self):
        expected = 'Test string'
        item = User()
        item.account_id = expected
        actual = item.account_id
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.account_id = expected
        actual = item.account_id
        self.assertEqual(expected, actual)
    
    def test_user_agent_property_works_as_expected(self):
        expected = 'Test string'
        item = User()
        item.user_agent = expected
        actual = item.user_agent
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.user_agent = expected
        actual = item.user_agent
        self.assertEqual(expected, actual)
    
    def test_id_property_works_as_expected(self):
        expected = 'Test string'
        item = User()
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
        expected = 'Other string'
        item.id = expected
        actual = item.id
        self.assertEqual(expected, actual)
    
    def test_serialize_works_as_expected(self):
        item = User()
        item.account_id = 'Test string'
        item.id = 'Test string'
        actual = json.dumps(item.write(), separators=(',', ':'), cls=TestJsonEncoder)
        expected = '{"ai.user.accountId":"Test string","ai.user.id":"Test string"}'
        self.assertEqual(expected, actual)

