import time
import datetime
import json
import uuid
import unittest
import random
try:
    import BaseHTTPServer
except ImportError:
    import http.server as BaseHTTPServer

from test import test_support

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "..")
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import channel

class TestTelemetrySender(unittest.TestCase):
    def setUp(self):
        # recover the telemetry sender type
        self.TelemetrySender = channel.TelemetryChannel().sender.__class__

    def tearDown(self):
        # clean up the telemetry sender type
        del self.TelemetrySender

    def test_constructTelemetrySender(self):
        actual = self.TelemetrySender()
        self.assertEqual("http://dc.services.visualstudio.com/v2/track", actual.serviceEndpointUri)
          
    def test_constructTelemetrySenderWithNoEndpoint(self):
        self.assertRaises(Exception, self.TelemetrySender, None)
                  
    def test_serviceEndpointUriPropertyWorksAsExpected(self):
        actual = self.TelemetrySender()
        self.assertEqual("http://dc.services.visualstudio.com/v2/track", actual.serviceEndpointUri)
        actual = self.TelemetrySender("blah")
        self.assertEqual("blah", actual.serviceEndpointUri)

    def test_sendIntervalInMillisecondsPropertyWorksAsExpected(self):
        actual = self.TelemetrySender()
        self.assertEqual(6000, actual.sendIntervalInMilliseconds)
        actual.sendIntervalInMilliseconds = 12345;
        self.assertEqual(12345, actual.sendIntervalInMilliseconds)
        actual.sendIntervalInMilliseconds = -42;
        self.assertEqual(1000, actual.sendIntervalInMilliseconds)
        
    def test_maxQueueItemCountPropertyWorksAsExpected(self):
        actual = self.TelemetrySender()
        self.assertEqual(100, actual.maxQueueItemCount)
        actual.maxQueueItemCount = 12345;
        self.assertEqual(12345, actual.maxQueueItemCount)
        actual.maxQueueItemCount = -42;
        self.assertEqual(1, actual.maxQueueItemCount)

    def test_sendWorksAsExpected(self):
        port = random.randint(50000, 60000)
        actual = self.TelemetrySender("http://localhost:" + str(port) + "/track")
        actual.maxQueueItemCount = 3
        actual.sendIntervalInMilliseconds = 2000
        MockHTTPRequestHandler.ExpectedContent = "[42,13]"
        MockHTTPRequestHandler.TestCase = self # save a reference to the test case in our handler
        actual.send(MockSerializable("42")) # send the mock item
        actual.send(MockSerializable("13")) # send the mock item
        runHttpHandlerOnce(handler=MockHTTPRequestHandler, port=port) # run the HTTP request
        time.sleep(1)
        if "failed" in dir(self):
            self.fail(self.failed)


class MockSerializable(object):
    def __init__(self, data):
        self.__data = data

    def serialize(self):
        return self.__data


class MockHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    ExpectedContent = None
    TestCase = None
    def do_POST(self):
        contentLength = int(self.headers['Content-Length'])
        content = self.rfile.read(contentLength)
        response = ""
        if isinstance(content, bytes):
            content = content.decode("utf-8")
            response = b""

        if "POST" != self.command:
            MockHTTPRequestHandler.TestCase.failed = '"POST" != self.command'
        if "application/json; charset=utf-8" != self.headers["Content-Type"]:
            MockHTTPRequestHandler.TestCase.failed = '"application/json; charset=utf-8" != self.headers.type'
        if MockHTTPRequestHandler.ExpectedContent != content:
            MockHTTPRequestHandler.TestCase.failed = '"' + MockHTTPRequestHandler.ExpectedContent + '" != content'

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", "0")
        self.end_headers()
        self.wfile.write(response)
        

def runHttpHandlerOnce(server=BaseHTTPServer.HTTPServer, handler=BaseHTTPServer.BaseHTTPRequestHandler, port=8121):
    serverAddress = ('', port)
    httpd = server(serverAddress, handler)
    httpd.handle_request()
