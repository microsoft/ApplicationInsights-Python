import random
import unittest
import time
import threading

try:
    # Python 2.x
    import BaseHTTPServer as HTTPServer
except ImportError:
    # Python 3.x
    import http.server as HTTPServer

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import channel

class TestSenderBase(unittest.TestCase):
    def test_construct(self):
        actual = channel.SenderBase('http://tempuri.org/')
        self.assertIsNotNone(actual)
        self.assertEqual('http://tempuri.org/', actual.service_endpoint_uri)
        self.assertIsNone(actual.queue)
        self.assertEqual(100, actual.send_buffer_size)

    def test_service_endpoint_uri_works_as_expected(self):
        actual = channel.SenderBase('http://tempuri.org/')
        self.assertEqual('http://tempuri.org/', actual.service_endpoint_uri)
        actual.service_endpoint_uri = 'foo'
        self.assertEqual('foo', actual.service_endpoint_uri)

    def test_queue_works_as_expected(self):
        actual = channel.SenderBase('http://tempuri.org/')
        self.assertIsNone(actual.queue)
        expected = object()
        actual.queue = expected
        self.assertEqual(expected, actual.queue)

    def test_send_buffer_size_works_as_expected(self):
        actual = channel.SenderBase('http://tempuri.org/')
        self.assertEqual(100, actual.send_buffer_size)
        actual.send_buffer_size = 42
        self.assertEqual(42, actual.send_buffer_size)
        actual.send_buffer_size = -1
        self.assertEqual(1, actual.send_buffer_size)

    def test_send_works_as_expected(self):
        port = random.randint(50000, 60000)
        actual = channel.SenderBase("http://localhost:" + str(port) + "/track")
        actual.queue = channel.QueueBase(None)
        MockHTTPRequestHandler.ExpectedContent = "[42, 13]"
        MockHTTPRequestHandler.TestCase = self # save a reference to the test case in our handler
        thread = WorkerThread(actual)
        thread.start()
        runHttpHandlerOnce(handler=MockHTTPRequestHandler, port=port) # run the HTTP request
        thread.join()
        if "failed" in dir(self):
            self.fail(self.failed)
        self.assertEqual(None, actual.queue.get())


class WorkerThread(threading.Thread):
    def __init__(self, sender):
        threading.Thread.__init__(self)
        self.sender = sender

    def run(self):
        time.sleep(1)
        self.sender.send([ MockSerializable(42), MockSerializable(13) ])


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