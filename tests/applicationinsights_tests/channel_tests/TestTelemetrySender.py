import time
import datetime
import json
import uuid
import unittest
import random
try:
    import BaseHTTPServer as HTTPServer
except ImportError:
    import http.server as HTTPServer

from test import test_support

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..')
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

    def test_construct(self):
        actual = self.TelemetrySender()
        self.assertEqual("http://dc.services.visualstudio.com/v2/track", actual.service_endpoint_uri)
          
    def test_construct_with_no_endpoint(self):
        self.assertRaises(Exception, self.TelemetrySender, None)
                  
    def test_service_endpoint_uri_property_works_as_expected(self):
        actual = self.TelemetrySender()
        self.assertEqual("http://dc.services.visualstudio.com/v2/track", actual.service_endpoint_uri)
        actual = self.TelemetrySender("blah")
        self.assertEqual("blah", actual.service_endpoint_uri)

    def test_send_interval_in_milliseconds_property_works_as_expected(self):
        actual = self.TelemetrySender()
        self.assertEqual(6000, actual.send_interval_in_milliseconds)
        actual.send_interval_in_milliseconds = 12345;
        self.assertEqual(12345, actual.send_interval_in_milliseconds)
        actual.send_interval_in_milliseconds = -42;
        self.assertEqual(1000, actual.send_interval_in_milliseconds)
        
    def test_max_queue_item_count_property_works_as_expected(self):
        actual = self.TelemetrySender()
        self.assertEqual(100, actual.max_queue_item_count)
        actual.max_queue_item_count = 12345;
        self.assertEqual(12345, actual.max_queue_item_count)
        actual.max_queue_item_count = -42;
        self.assertEqual(1, actual.max_queue_item_count)

    def test_send_works_as_expected(self):
        port = random.randint(50000, 60000)
        actual = self.TelemetrySender("http://localhost:" + str(port) + "/track")
        actual.max_queue_item_count = 3
        actual.send_interval_in_milliseconds = 2000
        MockHTTPRequestHandler.ExpectedContent = "[42, 13]"
        MockHTTPRequestHandler.TestCase = self # save a reference to the test case in our handler
        actual.send(MockSerializable(42)) # send the mock item
        actual.send(MockSerializable(13)) # send the mock item
        runHttpHandlerOnce(handler=MockHTTPRequestHandler, port=port) # run the HTTP request
        time.sleep(1)
        if "failed" in dir(self):
            self.fail(self.failed)


class MockSerializable(object):
    def __init__(self, data):
        self._data = data

    def write(self):
        return self._data


class MockHTTPRequestHandler(HTTPServer.BaseHTTPRequestHandler):
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
        

def runHttpHandlerOnce(server=HTTPServer.HTTPServer, handler=HTTPServer.BaseHTTPRequestHandler, port=8121):
    serverAddress = ('', port)
    httpd = server(serverAddress, handler)
    httpd.handle_request()
