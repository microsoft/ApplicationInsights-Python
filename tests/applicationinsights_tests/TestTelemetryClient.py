import unittest
import inspect
import json

from test import test_support

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import TelemetryClient, channel

class TestTelemetryClient(unittest.TestCase):
    def test_context_property_works_as_expected(self):
        client = TelemetryClient()
        self.assertIsNotNone(client.context)

    def test_channel_property_works_as_expected(self):
        expected = channel.TelemetryChannel()
        client = TelemetryClient(expected)
        self.assertEqual(expected, client.channel)

    def test_track_event_works_as_expected(self):
        sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(sender)
        client = TelemetryClient(channel.TelemetryChannel(context=None, queue=queue))
        client.context.instrumentation_key = '99999999-9999-9999-9999-999999999999'
        client.context.device = None
        client.track_event('test', { 'foo': 'bar' }, { 'x': 42 })
        client.flush()
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.Event", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "EventData", "baseData": {"ver": 2, "name": "test", "properties": {"foo": "bar"}, "measurements": {"x": 42}}}}'
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        actual = json.dumps(sender.data.write())
        self.maxDiff = None
        self.assertEqual(expected, actual)

    def test_track_metric_works_as_expected(self):
        sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(sender)
        client = TelemetryClient(channel.TelemetryChannel(context=None, queue=queue))
        client.context.instrumentation_key = '99999999-9999-9999-9999-999999999999'
        client.context.device = None
        client.track_metric('metric', 42, channel.contracts.DataPointType.aggregation, 13, 1, 123, 111, {'foo': 'bar'})
        client.flush()
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.Metric", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "MetricData", "baseData": {"ver": 2, "metrics": [{"name": "metric", "kind": 1, "value": 42, "count": 13, "min": 1, "max": 123, "stdDev": 111}], "properties": {"foo": "bar"}}}}'
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        actual = json.dumps(sender.data.write())
        self.maxDiff = None
        self.assertEqual(expected, actual)

    def test_track_trace_works_as_expected(self):
        sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(sender)
        client = TelemetryClient(channel.TelemetryChannel(context=None, queue=queue))
        client.context.instrumentation_key = '99999999-9999-9999-9999-999999999999'
        client.context.device = None
        client.track_trace('test', { 'foo': 'bar' })
        client.flush()
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.Message", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "MessageData", "baseData": {"ver": 2, "message": "test", "properties": {"foo": "bar"}}}}'
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        actual = json.dumps(sender.data.write())
        self.maxDiff = None
        self.assertEqual(expected, actual)

    def test_track_pageview_works_as_expected(self):
        sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(sender)
        client = TelemetryClient(channel.TelemetryChannel(context=None, queue=queue))
        client.context.instrumentation_key = '99999999-9999-9999-9999-999999999999'
        client.context.device = None
        client.track_pageview('test', 'http://tempuri.org', 13, { 'foo': 'bar' }, { 'x': 42 })
        client.flush()
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.PageView", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "PageViewData", "baseData": {"ver": 2, "url": "http://tempuri.org", "name": "test", "duration": 13, "properties": {"foo": "bar"}, "measurements": {"x": 42}}}}'
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        actual = json.dumps(sender.data.write())
        self.maxDiff = None
        self.assertEqual(expected, actual)

    def test_track_exception_works_as_expected(self):
        sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(sender)
        client = TelemetryClient(channel.TelemetryChannel(context=None, queue=queue))
        client.context.instrumentation_key = '99999999-9999-9999-9999-999999999999'
        client.context.device = None
        try:
            raise Exception("blah")
        except Exception as e:
            client.track_exception(*sys.exc_info(), properties={}, measurements={ 'x': 42 })
            client.flush()
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.Exception", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "ExceptionData", "baseData": {"ver": 2, "handledAt": "UserCode", "exceptions": [{"id": 1, "outerId": 0, "typeName": "Exception", "message": "blah", "parsedStack": [{"level": 0, "method": "test_track_exception_works_as_expected", "assembly": "Unknown", "fileName": "TestTelemetryClient.py", "line": 0}]}], "measurements": {"x": 42}}}}'
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        for item in sender.data.data.base_data.exceptions:
            for frame in item.parsed_stack:
                frame.file_name = os.path.basename(frame.file_name)
                frame.line = 0
        actual = json.dumps(sender.data.write())
        self.assertEqual(expected, actual)
        try:
            raise Exception("blah")
        except Exception as e:
            client.track_exception()
            client.flush()
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.Exception", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "ExceptionData", "baseData": {"ver": 2, "handledAt": "UserCode", "exceptions": [{"id": 1, "outerId": 0, "typeName": "Exception", "message": "blah", "parsedStack": [{"level": 0, "method": "test_track_exception_works_as_expected", "assembly": "Unknown", "fileName": "TestTelemetryClient.py", "line": 0}]}]}}}'
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        for item in sender.data.data.base_data.exceptions:
            for frame in item.parsed_stack:
                frame.file_name = os.path.basename(frame.file_name)
                frame.line = 0
        actual = json.dumps(sender.data.write())
        self.assertEqual(expected, actual)


class MockTelemetrySender(channel.TelemetryChannel().sender.__class__):
    def __init__(self):
        self.data = None
        self.send_buffer_size = 1

    def send(self, envelope):
        self.data = envelope[0];
