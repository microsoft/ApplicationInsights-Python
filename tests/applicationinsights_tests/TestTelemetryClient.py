import unittest
import inspect
import json
import sys

if sys.version_info < (3,0):
    from test import test_support
else:
    from test import support as test_support

import os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import TelemetryClient, channel


class TestTelemetryClient(unittest.TestCase):
    def test_constructor_throws_with_no_instrumentation_key(self):
        self.assertRaises(Exception, TelemetryClient, None)

    def test_constructor_sets_instrumentation_key(self):
        client = TelemetryClient('foo')
        self.assertEqual('foo', client.context.instrumentation_key)

    def test_constructor_maintains_backwards_compatibility_when_specifying_only_telemetry_channel(self):
        expected = channel.TelemetryChannel()
        client = TelemetryClient(expected)
        self.assertEqual(expected, client.channel)
        self.assertIsNone(client.context.instrumentation_key)

    def test_context_property_works_as_expected(self):
        client = TelemetryClient('foo')
        self.assertIsNotNone(client.context)

    def test_channel_property_works_as_expected(self):
        expected = channel.TelemetryChannel()
        client = TelemetryClient('foo', expected)
        self.assertEqual(expected, client.channel)

    def test_track_event_works_as_expected(self):
        sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(sender)
        client = TelemetryClient('99999999-9999-9999-9999-999999999999', channel.TelemetryChannel(context=None, queue=queue))
        client.context.device = None
        client.track_event('test', { 'foo': 'bar' }, { 'x': 42 })
        client.flush()
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.Event", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.device.id": "DEVICE_ID_PLACEHOLDER", "ai.device.locale": "DEVICE_LOCALE_PLACEHOLDER", "ai.device.osVersion": "DEVICE_OS_VERSION_PLACEHOLDER", "ai.device.type": "DEVICE_TYPE_PLACEHOLDER", "ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "EventData", "baseData": {"ver": 2, "name": "test", "properties": {"foo": "bar"}, "measurements": {"x": 42}}}}'
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        sender.data.tags['ai.device.id'] = "DEVICE_ID_PLACEHOLDER"
        sender.data.tags['ai.device.locale'] = "DEVICE_LOCALE_PLACEHOLDER"
        sender.data.tags['ai.device.osVersion'] = "DEVICE_OS_VERSION_PLACEHOLDER"
        sender.data.tags['ai.device.type'] = "DEVICE_TYPE_PLACEHOLDER"
        actual = json.dumps(sender.data.write())
        self.maxDiff = None
        self.assertEqual(expected, actual)

    def test_track_event_with_context_properties_works_as_expected(self):
        sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(sender)
        client = TelemetryClient('99999999-9999-9999-9999-999999999999', channel.TelemetryChannel(context=None, queue=queue))
        client.context.device = None
        client.context.properties['foo'] = 'bar'
        client.track_event('test')
        client.flush()
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.Event", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.device.id": "DEVICE_ID_PLACEHOLDER", "ai.device.locale": "DEVICE_LOCALE_PLACEHOLDER", "ai.device.osVersion": "DEVICE_OS_VERSION_PLACEHOLDER", "ai.device.type": "DEVICE_TYPE_PLACEHOLDER", "ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "EventData", "baseData": {"ver": 2, "name": "test", "properties": {"foo": "bar"}}}}'
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        sender.data.tags['ai.device.id'] = "DEVICE_ID_PLACEHOLDER"
        sender.data.tags['ai.device.locale'] = "DEVICE_LOCALE_PLACEHOLDER"
        sender.data.tags['ai.device.osVersion'] = "DEVICE_OS_VERSION_PLACEHOLDER"
        sender.data.tags['ai.device.type'] = "DEVICE_TYPE_PLACEHOLDER"
        actual = json.dumps(sender.data.write())
        self.maxDiff = None
        self.assertEqual(expected, actual)

    def test_track_event_with_merged_context_properties_works_as_expected(self):
        key = '99999999-9999-9999-9999-999999999999'
        sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(sender)

        chan = channel.TelemetryChannel(queue=queue)
        chan.context.properties['foo'] = 'bar'

        client1 = TelemetryClient(key, chan)
        client1.context.device = None
        client1.context.properties['x'] = 42

        client2 = TelemetryClient(key, chan)
        client2.context.device = None
        client2.context.properties['x'] = 84

        client1.track_event('test 1')
        client1.flush()
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        sender.data.tags['ai.device.id'] = "DEVICE_ID_PLACEHOLDER"
        sender.data.tags['ai.device.locale'] = "DEVICE_LOCALE_PLACEHOLDER"
        sender.data.tags['ai.device.osVersion'] = "DEVICE_OS_VERSION_PLACEHOLDER"
        sender.data.tags['ai.device.type'] = "DEVICE_TYPE_PLACEHOLDER"
        actual = json.dumps(sender.data.write())
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.Event", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.device.id": "DEVICE_ID_PLACEHOLDER", "ai.device.locale": "DEVICE_LOCALE_PLACEHOLDER", "ai.device.osVersion": "DEVICE_OS_VERSION_PLACEHOLDER", "ai.device.type": "DEVICE_TYPE_PLACEHOLDER", "ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "EventData", "baseData": {"ver": 2, "name": "test 1", "properties": {"foo": "bar", "x": 42}}}}'
        self.maxDiff = None
        self.assertEqual(expected, actual)

        client2.track_event('test 2')
        client2.flush()
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        sender.data.tags['ai.device.id'] = "DEVICE_ID_PLACEHOLDER"
        sender.data.tags['ai.device.locale'] = "DEVICE_LOCALE_PLACEHOLDER"
        sender.data.tags['ai.device.osVersion'] = "DEVICE_OS_VERSION_PLACEHOLDER"
        sender.data.tags['ai.device.type'] = "DEVICE_TYPE_PLACEHOLDER"
        actual = json.dumps(sender.data.write())
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.Event", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.device.id": "DEVICE_ID_PLACEHOLDER", "ai.device.locale": "DEVICE_LOCALE_PLACEHOLDER", "ai.device.osVersion": "DEVICE_OS_VERSION_PLACEHOLDER", "ai.device.type": "DEVICE_TYPE_PLACEHOLDER", "ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "EventData", "baseData": {"ver": 2, "name": "test 2", "properties": {"foo": "bar", "x": 84}}}}'
        self.assertEqual(expected, actual)

    def test_track_metric_works_as_expected(self):
        sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(sender)
        client = TelemetryClient('99999999-9999-9999-9999-999999999999', channel.TelemetryChannel(context=None, queue=queue))
        client.context.device = None
        client.track_metric('metric', 42, channel.contracts.DataPointType.aggregation, 13, 1, 123, 111, {'foo': 'bar'})
        client.flush()
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.Metric", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.device.id": "DEVICE_ID_PLACEHOLDER", "ai.device.locale": "DEVICE_LOCALE_PLACEHOLDER", "ai.device.osVersion": "DEVICE_OS_VERSION_PLACEHOLDER", "ai.device.type": "DEVICE_TYPE_PLACEHOLDER", "ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "MetricData", "baseData": {"ver": 2, "metrics": [{"name": "metric", "kind": 1, "value": 42, "count": 13, "min": 1, "max": 123, "stdDev": 111}], "properties": {"foo": "bar"}}}}'
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        sender.data.tags['ai.device.id'] = "DEVICE_ID_PLACEHOLDER"
        sender.data.tags['ai.device.locale'] = "DEVICE_LOCALE_PLACEHOLDER"
        sender.data.tags['ai.device.osVersion'] = "DEVICE_OS_VERSION_PLACEHOLDER"
        sender.data.tags['ai.device.type'] = "DEVICE_TYPE_PLACEHOLDER"
        actual = json.dumps(sender.data.write())
        self.maxDiff = None
        self.assertEqual(expected, actual)

    def test_track_trace_works_as_expected(self):
        sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(sender)
        client = TelemetryClient('99999999-9999-9999-9999-999999999999', channel.TelemetryChannel(context=None, queue=queue))
        client.context.device = None
        client.track_trace('test', { 'foo': 'bar' }, severity='WARNING')
        client.flush()
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.Message", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.device.id": "DEVICE_ID_PLACEHOLDER", "ai.device.locale": "DEVICE_LOCALE_PLACEHOLDER", "ai.device.osVersion": "DEVICE_OS_VERSION_PLACEHOLDER", "ai.device.type": "DEVICE_TYPE_PLACEHOLDER", "ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "MessageData", "baseData": {"ver": 2, "message": "test", "severityLevel": 2, "properties": {"foo": "bar"}}}}'
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        sender.data.tags['ai.device.id'] = "DEVICE_ID_PLACEHOLDER"
        sender.data.tags['ai.device.locale'] = "DEVICE_LOCALE_PLACEHOLDER"
        sender.data.tags['ai.device.osVersion'] = "DEVICE_OS_VERSION_PLACEHOLDER"
        sender.data.tags['ai.device.type'] = "DEVICE_TYPE_PLACEHOLDER"
        actual = json.dumps(sender.data.write())
        self.maxDiff = None
        self.assertEqual(expected, actual)

    def test_track_pageview_works_as_expected(self):
        sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(sender)
        client = TelemetryClient('99999999-9999-9999-9999-999999999999', channel.TelemetryChannel(context=None, queue=queue))
        client.context.device = None
        client.track_pageview('test', 'http://tempuri.org', 13, { 'foo': 'bar' }, { 'x': 42 })
        client.flush()
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.PageView", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.device.id": "DEVICE_ID_PLACEHOLDER", "ai.device.locale": "DEVICE_LOCALE_PLACEHOLDER", "ai.device.osVersion": "DEVICE_OS_VERSION_PLACEHOLDER", "ai.device.type": "DEVICE_TYPE_PLACEHOLDER", "ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "PageViewData", "baseData": {"ver": 2, "url": "http://tempuri.org", "name": "test", "duration": 13, "properties": {"foo": "bar"}, "measurements": {"x": 42}}}}'
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        sender.data.tags['ai.device.id'] = "DEVICE_ID_PLACEHOLDER"
        sender.data.tags['ai.device.locale'] = "DEVICE_LOCALE_PLACEHOLDER"
        sender.data.tags['ai.device.osVersion'] = "DEVICE_OS_VERSION_PLACEHOLDER"
        sender.data.tags['ai.device.type'] = "DEVICE_TYPE_PLACEHOLDER"
        actual = json.dumps(sender.data.write())
        self.maxDiff = None
        self.assertEqual(expected, actual)

    def test_track_exception_works_as_expected(self):
        sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(sender)
        client = TelemetryClient('99999999-9999-9999-9999-999999999999', channel.TelemetryChannel(context=None, queue=queue))
        client.context.device = None
        try:
            raise Exception("blah")
        except Exception as e:
            client.track_exception(*sys.exc_info(), properties={}, measurements={ 'x': 42 })
            client.flush()
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.Exception", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.device.id": "DEVICE_ID_PLACEHOLDER", "ai.device.locale": "DEVICE_LOCALE_PLACEHOLDER", "ai.device.osVersion": "DEVICE_OS_VERSION_PLACEHOLDER", "ai.device.type": "DEVICE_TYPE_PLACEHOLDER", "ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "ExceptionData", "baseData": {"ver": 2, "exceptions": [{"id": 1, "outerId": 0, "typeName": "Exception", "message": "blah", "hasFullStack": true, "parsedStack": [{"level": 0, "method": "test_track_exception_works_as_expected", "assembly": "Unknown", "fileName": "TestTelemetryClient.py", "line": 0}]}], "measurements": {"x": 42}}}}'
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        sender.data.tags['ai.device.id'] = "DEVICE_ID_PLACEHOLDER"
        sender.data.tags['ai.device.locale'] = "DEVICE_LOCALE_PLACEHOLDER"
        sender.data.tags['ai.device.osVersion'] = "DEVICE_OS_VERSION_PLACEHOLDER"
        sender.data.tags['ai.device.type'] = "DEVICE_TYPE_PLACEHOLDER"
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
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.Exception", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.device.id": "DEVICE_ID_PLACEHOLDER", "ai.device.locale": "DEVICE_LOCALE_PLACEHOLDER", "ai.device.osVersion": "DEVICE_OS_VERSION_PLACEHOLDER", "ai.device.type": "DEVICE_TYPE_PLACEHOLDER", "ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "ExceptionData", "baseData": {"ver": 2, "exceptions": [{"id": 1, "outerId": 0, "typeName": "Exception", "message": "blah", "hasFullStack": true, "parsedStack": [{"level": 0, "method": "test_track_exception_works_as_expected", "assembly": "Unknown", "fileName": "TestTelemetryClient.py", "line": 0}]}]}}}'
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        sender.data.tags['ai.device.id'] = "DEVICE_ID_PLACEHOLDER"
        sender.data.tags['ai.device.locale'] = "DEVICE_LOCALE_PLACEHOLDER"
        sender.data.tags['ai.device.osVersion'] = "DEVICE_OS_VERSION_PLACEHOLDER"
        sender.data.tags['ai.device.type'] = "DEVICE_TYPE_PLACEHOLDER"
        for item in sender.data.data.base_data.exceptions:
            for frame in item.parsed_stack:
                frame.file_name = os.path.basename(frame.file_name)
                frame.line = 0
        actual = json.dumps(sender.data.write())
        self.assertEqual(expected, actual)

    def test_track_request_works_as_expected(self):
        sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(sender)
        client = TelemetryClient(channel.TelemetryChannel(context=None, queue=queue))
        client.context.instrumentation_key = '99999999-9999-9999-9999-999999999999'
        client.context.device = None
        client.track_request('test', 'http://tempuri.org', True, 'START_TIME', 13, 42, 'OPTIONS', { 'foo': 'bar' }, { 'x': 42 }, 'ID_PLACEHOLDER')
        client.flush()
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.Request", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.device.id": "DEVICE_ID_PLACEHOLDER", "ai.device.locale": "DEVICE_LOCALE_PLACEHOLDER", "ai.device.osVersion": "DEVICE_OS_VERSION_PLACEHOLDER", "ai.device.type": "DEVICE_TYPE_PLACEHOLDER", "ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "RequestData", "baseData": {"ver": 2, "id": "ID_PLACEHOLDER", "name": "test", "duration": "00:00:00.013", "responseCode": "42", "success": true, "url": "http://tempuri.org", "properties": {"foo": "bar"}, "measurements": {"x": 42}}}}'
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        sender.data.tags['ai.device.id'] = "DEVICE_ID_PLACEHOLDER"
        sender.data.tags['ai.device.locale'] = "DEVICE_LOCALE_PLACEHOLDER"
        sender.data.tags['ai.device.osVersion'] = "DEVICE_OS_VERSION_PLACEHOLDER"
        sender.data.tags['ai.device.type'] = "DEVICE_TYPE_PLACEHOLDER"
        actual = json.dumps(sender.data.write())
        self.maxDiff = None
        self.assertEqual(expected, actual)

    def test_track_dependency_works_as_expected(self):
        sender = MockTelemetrySender()
        queue = channel.SynchronousQueue(sender)
        client = TelemetryClient(channel.TelemetryChannel(context=None, queue=queue))
        client.context.instrumentation_key = '99999999-9999-9999-9999-999999999999'
        client.context.device = None
        client.track_dependency('test', 'COMMAND_PLACEHOLDER', 'HTTP', 'localhost', 13, True, 200, { 'foo': 'bar' }, { 'x': 42 }, 'ID_PLACEHOLDER')
        client.flush()
        expected = '{"ver": 1, "name": "Microsoft.ApplicationInsights.RemoteDependency", "time": "TIME_PLACEHOLDER", "sampleRate": 100.0, "iKey": "99999999-9999-9999-9999-999999999999", "tags": {"ai.device.id": "DEVICE_ID_PLACEHOLDER", "ai.device.locale": "DEVICE_LOCALE_PLACEHOLDER", "ai.device.osVersion": "DEVICE_OS_VERSION_PLACEHOLDER", "ai.device.type": "DEVICE_TYPE_PLACEHOLDER", "ai.internal.sdkVersion": "SDK_VERSION_PLACEHOLDER"}, "data": {"baseType": "RemoteDependencyData", "baseData": {"ver": 2, "name": "test", "id": "ID_PLACEHOLDER", "resultCode": "200", "duration": "00:00:00.013", "success": true, "data": "COMMAND_PLACEHOLDER", "target": "localhost", "type": "HTTP", "properties": {"foo": "bar"}, "measurements": {"x": 42}}}}'
        sender.data.time = 'TIME_PLACEHOLDER'
        sender.data.tags['ai.internal.sdkVersion'] = 'SDK_VERSION_PLACEHOLDER'
        sender.data.tags['ai.device.id'] = "DEVICE_ID_PLACEHOLDER"
        sender.data.tags['ai.device.locale'] = "DEVICE_LOCALE_PLACEHOLDER"
        sender.data.tags['ai.device.osVersion'] = "DEVICE_OS_VERSION_PLACEHOLDER"
        sender.data.tags['ai.device.type'] = "DEVICE_TYPE_PLACEHOLDER"
        actual = json.dumps(sender.data.write())
        self.maxDiff = None
        self.assertEqual(expected, actual)


class MockTelemetrySender(channel.TelemetryChannel().sender.__class__):
    def __init__(self):
        self.data = None
        self.send_buffer_size = 1

    def send(self, envelope):
        self.data = envelope[0]
