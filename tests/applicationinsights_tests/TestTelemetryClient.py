import unittest
import inspect
import json

from test import test_support

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..")
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import TelemetryClient, channel

class TestTelemetryClient(unittest.TestCase):
    def test_contextReturnsNonNullValue(self):
        client = TelemetryClient()
        self.assertIsNotNone(client.context)

    def test_channelWorksAsExpected(self):
        expected = channel.TelemetryChannel()
        client = TelemetryClient(expected)
        self.assertEqual(expected, client.channel)

    def test_trackEventWorksAsExpected(self):
        sender = MockTelemetrySender()
        client = TelemetryClient(channel.TelemetryChannel(context=None, sender=sender))
        client.context.instrumentationKey = "99999999-9999-9999-9999-999999999999"
        client.context.device = None
        client.context.session = None
        client.trackEvent("test", {}, { "x": 42 })
        expected = '{"ver":1,"name":"Microsoft.ApplicationInsights.Event","time":"TIME_PLACEHOLDER","iKey":"99999999-9999-9999-9999-999999999999","data":{"type":"Microsoft.ApplicationInsights.EventData","item":{"ver":1,"name":"test","properties":{"SDKVersion": "Python;0.1"},"measurements":{"x": 42}}}}'
        sender.data.time = "TIME_PLACEHOLDER"
        actual = sender.data.serialize()
        self.assertEqual(expected, actual)

    def test_trackMetricWorksAsExpected(self):
        sender = MockTelemetrySender()
        client = TelemetryClient(channel.TelemetryChannel(context=None, sender=sender))
        client.context.instrumentationKey = "99999999-9999-9999-9999-999999999999"
        client.context.device = None
        client.context.session = None
        client.trackMetric("metric", 42, "A", 13, 1, 123, {})
        expected = '{"ver":1,"name":"Microsoft.ApplicationInsights.Metric","time":"TIME_PLACEHOLDER","iKey":"99999999-9999-9999-9999-999999999999","data":{"type":"Microsoft.ApplicationInsights.MetricData","item":{"ver":1,"metrics":[{"name":"metric","value":42,"kind":"A","count":13,"min":1,"max":123}],"properties":{"SDKVersion": "Python;0.1"}}}}'
        sender.data.time = "TIME_PLACEHOLDER"
        actual = sender.data.serialize()
        self.assertEqual(expected, actual)

    def test_trackTraceWorksAsExpected(self):
        sender = MockTelemetrySender()
        client = TelemetryClient(channel.TelemetryChannel(context=None, sender=sender))
        client.context.instrumentationKey = "99999999-9999-9999-9999-999999999999"
        client.context.device = None
        client.context.session = None
        client.trackTrace("test", {}, { "x": 42 })
        expected = '{"ver":1,"name":"Microsoft.ApplicationInsights.Message","time":"TIME_PLACEHOLDER","iKey":"99999999-9999-9999-9999-999999999999","data":{"type":"Microsoft.ApplicationInsights.MessageData","item":{"ver":1,"message":"test","properties":{"SDKVersion": "Python;0.1"},"measurements":{"x": 42}}}}'
        sender.data.time = "TIME_PLACEHOLDER"
        actual = sender.data.serialize()
        self.assertEqual(expected, actual)

    def test_trackPageViewWorksAsExpected(self):
        sender = MockTelemetrySender()
        client = TelemetryClient(channel.TelemetryChannel(context=None, sender=sender))
        client.context.instrumentationKey = "99999999-9999-9999-9999-999999999999"
        client.context.device = None
        client.context.session = None
        client.trackPageView("test", "http://tempuri.org", 13, {}, { "x": 42 })
        expected = '{"ver":1,"name":"Microsoft.ApplicationInsights.Pageview","time":"TIME_PLACEHOLDER","iKey":"99999999-9999-9999-9999-999999999999","data":{"type":"Microsoft.ApplicationInsights.PageviewData","item":{"ver":1,"url":"http://tempuri.org","name":"test","duration":13,"properties":{"SDKVersion": "Python;0.1"},"measurements":{"x": 42}}}}'
        sender.data.time = "TIME_PLACEHOLDER"
        actual = sender.data.serialize()
        self.assertEqual(expected, actual)

    def test_trackExceptionWorksAsExpected(self):
        sender = MockTelemetrySender()
        client = TelemetryClient(channel.TelemetryChannel(context=None, sender=sender))
        client.context.instrumentationKey = "99999999-9999-9999-9999-999999999999"
        client.context.device = None
        client.context.session = None
        try:
            raise Exception("blah")
        except Exception as e:
            client.trackException(e, {}, { "x": 42 })
        expected27 = '{"ver":1,"name":"Microsoft.ApplicationInsights.Exception","time":"TIME_PLACEHOLDER","iKey":"99999999-9999-9999-9999-999999999999","data":{"type":"Microsoft.ApplicationInsights.ExceptionData","item":{"ver":1,"handledAt":"UserCode","exceptions":[{"id":1,"outerId":0,"typeName":"Exception","message":"blah","hasFullStack":false,"parsedStack":[]}],"properties":{"SDKVersion": "Python;0.1"},"measurements":{"x": 42}}}}'
        expected34 = '{"ver":1,"name":"Microsoft.ApplicationInsights.Exception","time":"TIME_PLACEHOLDER","iKey":"99999999-9999-9999-9999-999999999999","data":{"type":"Microsoft.ApplicationInsights.ExceptionData","item":{"ver":1,"handledAt":"UserCode","exceptions":[{"id":1,"outerId":0,"typeName":"Exception","message":"blah","hasFullStack":true,"parsedStack":[{"level":0,"method":"test_trackExceptionWorksAsExpected(self)","assembly":"<module>","fileName":' + json.dumps(os.path.abspath(inspect.getfile(inspect.currentframe()))) + ',"line":"LINE_PLACEHOLDER"}]}],"properties":{"SDKVersion": "Python;0.1"},"measurements":{"x": 42}}}}'
        expected = expected27
        sender.data.time = "TIME_PLACEHOLDER"
        if len(sender.data.data.item.exceptions[0].parsedStack) > 0:
            expected = expected34
            sender.data.data.item.exceptions[0].parsedStack[0].line = "LINE_PLACEHOLDER"
        actual = sender.data.serialize()
        self.assertEqual(expected, actual)


class MockTelemetrySender(channel.TelemetryChannel().sender.__class__):
    def __init__(self):
        self.data = None

    def send(self, envelope):
        self.data = envelope;
