import unittest
import wsgiref

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import requests

class TestWSGIApplication(unittest.TestCase):
    def test_construct(self):
        app = mock_app
        wrapper = requests.WSGIApplication('foo', app)
        self.assertIsNotNone(wrapper)
        self.assertIsNotNone(wrapper.client)
        self.assertEqual('foo', wrapper.client.context.instrumentation_key)

    def test_construct_raises_exception_on_no_instrumentation_key(self):
        self.assertRaises(Exception, requests.WSGIApplication, None, object())

    def test_construct_raises_exception_on_no_wsgi_application(self):
        self.assertRaises(Exception, requests.WSGIApplication, 'foo', None)

    def test_wsgi_works_as_expected(self):
        app = mock_app
        wrapper = requests.WSGIApplication('test', app)
        sender = self._intercept_sender(wrapper)
        env = {
            'REQUEST_METHOD': 'PUT',
            'PATH_INFO': '/foo/bar',
            'QUERY_STRING': 'a=b'
        }

        result = wrapper(env, mock_start_response)
        result_string = None
        for part in result:
            result_string = part

        data = sender.data[0][0]
        self.assertEqual('Microsoft.ApplicationInsights.Request', data.name)
        self.assertEqual('test', data.ikey)
        self.assertEqual('RequestData', data.data.base_type)
        self.assertEqual('PUT', data.data.base_data.http_method)
        self.assertEqual('/foo/bar', data.data.base_data.name)
        self.assertEqual('201', data.data.base_data.response_code)
        self.assertTrue(data.data.base_data.success)
        self.assertEqual('http://unknown/foo/bar?a=b', data.data.base_data.url)
        self.assertIsNotNone(data.data.base_data.id)
        self.assertEqual(b'Hello World!', result_string)
        self.assertEqual(1, mock_start_response_calls)
        self.assertEqual('201 BLAH', mock_start_response_status)
        self.assertEqual([('Content-type', 'text/plain')], mock_start_response_headers)

    def _intercept_sender(self, wsgi_application):
        client = wsgi_application.client

        # mock out the sender
        sender = MockAsynchronousSender()
        queue = client.channel.queue
        queue.max_queue_length = 1
        queue._sender = sender
        sender.queue = queue

        return sender


mock_start_response_calls = 0
mock_start_response_status = None
mock_start_response_headers = None


def mock_start_response(status, headers, exc_info=None):
    global mock_start_response_calls
    global mock_start_response_status
    global mock_start_response_headers
    mock_start_response_calls += 1
    mock_start_response_status = status
    mock_start_response_headers = headers


def mock_app(environ, start_response):
    status = '201 BLAH'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return [b'Hello World!']


class MockAsynchronousSender:
    def __init__(self):
        self.send_buffer_size = 1
        self.data = []
        self.queue = None

    def start(self):
        while True:
            data = []
            while len(data) < self.send_buffer_size:
                item = self.queue.get()
                if not item:
                    break
                data.append(item)
            if len(data) == 0:
                break
            self.send(data)

    def send(self, data_to_send):
        self.data.append(data_to_send)