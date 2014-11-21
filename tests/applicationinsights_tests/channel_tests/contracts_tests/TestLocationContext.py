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

class TestLocationContext(unittest.TestCase):
    def test_constructLocationContext(self):
        item = LocationContext()
        self.assertNotEqual(item, None)
    
    def test_latitudePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = LocationContext()
        item.latitude = expected
        actual = item.latitude
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.latitude = expected
        actual = item.latitude
        self.assertEqual(expected, actual)
    
    def test_longitudePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = LocationContext()
        item.longitude = expected
        actual = item.longitude
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.longitude = expected
        actual = item.longitude
        self.assertEqual(expected, actual)
    
    def test_ipPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = LocationContext()
        item.ip = expected
        actual = item.ip
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.ip = expected
        actual = item.ip
        self.assertEqual(expected, actual)
    
    def test_continentPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = LocationContext()
        item.continent = expected
        actual = item.continent
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.continent = expected
        actual = item.continent
        self.assertEqual(expected, actual)
    
    def test_countryPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = LocationContext()
        item.country = expected
        actual = item.country
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.country = expected
        actual = item.country
        self.assertEqual(expected, actual)
    
    def test_provincePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = LocationContext()
        item.province = expected
        actual = item.province
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.province = expected
        actual = item.province
        self.assertEqual(expected, actual)
    
    def test_cityPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = LocationContext()
        item.city = expected
        actual = item.city
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.city = expected
        actual = item.city
        self.assertEqual(expected, actual)
    
    def test_serializeMethod(self):
        item = LocationContext()
        item.latitude = "Test string 1"
        item.longitude = "Test string 1"
        item.ip = "Test string 1"
        item.continent = "Test string 1"
        item.country = "Test string 1"
        item.province = "Test string 1"
        item.city = "Test string 1"
        actual = item.serialize()
        expected = '{"latitude":"Test string 1","longitude":"Test string 1","ip":"Test string 1","continent":"Test string 1","country":"Test string 1","province":"Test string 1","city":"Test string 1"}'
        self.assertEqual(expected, actual)

