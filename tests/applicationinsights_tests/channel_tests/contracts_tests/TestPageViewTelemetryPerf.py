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

class TestPageViewTelemetryPerf(unittest.TestCase):
    def test_constructPageViewTelemetryPerf(self):
        item = PageViewTelemetryPerf()
        self.assertNotEqual(item, None)
    
    def test_perfTotalPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = PageViewTelemetryPerf()
        item.perfTotal = expected
        actual = item.perfTotal
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.perfTotal = expected
        actual = item.perfTotal
        self.assertEqual(expected, actual)
    
    def test_networkConnectPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = PageViewTelemetryPerf()
        item.networkConnect = expected
        actual = item.networkConnect
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.networkConnect = expected
        actual = item.networkConnect
        self.assertEqual(expected, actual)
    
    def test_sentRequestPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = PageViewTelemetryPerf()
        item.sentRequest = expected
        actual = item.sentRequest
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.sentRequest = expected
        actual = item.sentRequest
        self.assertEqual(expected, actual)
    
    def test_receivedResponsePropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = PageViewTelemetryPerf()
        item.receivedResponse = expected
        actual = item.receivedResponse
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.receivedResponse = expected
        actual = item.receivedResponse
        self.assertEqual(expected, actual)
    
    def test_domProcessingPropertyWorksAsExpected(self):
        expected = "Test string 1"
        item = PageViewTelemetryPerf()
        item.domProcessing = expected
        actual = item.domProcessing
        self.assertEqual(expected, actual)
        expected = "Test string 2"
        item.domProcessing = expected
        actual = item.domProcessing
        self.assertEqual(expected, actual)
    
    def test_serializeMethod(self):
        item = PageViewTelemetryPerf()
        item.perfTotal = "Test string 1"
        item.networkConnect = "Test string 1"
        item.sentRequest = "Test string 1"
        item.receivedResponse = "Test string 1"
        item.domProcessing = "Test string 1"
        actual = item.serialize()
        expected = '{"perfTotal":"Test string 1","networkConnect":"Test string 1","sentRequest":"Test string 1","receivedResponse":"Test string 1","domProcessing":"Test string 1"}'
        self.assertEqual(expected, actual)

