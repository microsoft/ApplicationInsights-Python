import unittest

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import channel, exceptions


class TestEnable(unittest.TestCase):
    def test_enable(self):
        original = sys.excepthook
        sys.excepthook = mock_excepthook
        sender = MockSynchronousSender()
        queue = channel.SynchronousQueue(sender)
        telemetry_channel = channel.TelemetryChannel(None, queue)
        telemetry_channel.context.properties["foo"] = "bar"
        telemetry_channel.context.operation.id = 1001
        exceptions.enable('foo', telemetry_channel=telemetry_channel)
        try:
            raise Exception('Boom')
        except:
            sys.excepthook(*sys.exc_info())
        sys.excepthook = original
        data = sender.data[0][0]
        self.assertIsNotNone(data)
        self.assertEqual('foo', data.ikey)
        self.assertEqual('Microsoft.ApplicationInsights.Exception', data.name)
        self.assertEqual('bar', data.data.base_data.properties['foo'])
        self.assertEqual(1001, data.tags.get('ai.operation.id')) 

    def test_enable_raises_exception_on_no_instrumentation_key(self):
        self.assertRaises(Exception, exceptions.enable, None)


def mock_excepthook(type, value, tb):
    pass


class MockSynchronousSender:
    def __init__(self):
        self.send_buffer_size = 1
        self.data = []
        self.queue = None

    def send(self, data_to_send):
        self.data.append(data_to_send)