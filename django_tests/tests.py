import logging
import django

from applicationinsights import TelemetryClient
from applicationinsights.channel import TelemetryChannel, SynchronousQueue, SenderBase
from applicationinsights.django import common
from django.test import TestCase, Client, modify_settings, override_settings

if django.VERSION > (1, 10):
    MIDDLEWARE_NAME = "MIDDLEWARE"
else:
    MIDDLEWARE_NAME = "MIDDLEWARE_CLASSES"

TEST_IKEY = '12345678-1234-5678-0912-123456789abc'

class AITestCase(TestCase):
    def setUp(self):
        self.events = plug_sender().events

    def get_events(self, count):
        common.saved_client.channel.flush()
        self.assertEqual(len(self.events), count, "Expected %d event(s) in queue" % count)
        if count == 1:
            return self.events[0]
        return self.events

@modify_settings(**{MIDDLEWARE_NAME: {'append': 'applicationinsights.django.ApplicationInsightsMiddleware'}})
@override_settings(APPLICATION_INSIGHTS={'ikey': TEST_IKEY})
class MiddlewareTests(AITestCase):
    def test_basic_request(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        event = self.get_events(1)
        tags = event['tags']
        data = event['data']['baseData']
        self.assertEqual(event['name'], 'Microsoft.ApplicationInsights.Request', "Event type")
        self.assertEqual(event['iKey'], TEST_IKEY)
        self.assertEqual(tags['ai.operation.name'], 'GET aitest.views.home', "Operation name")
        self.assertEqual(data['name'], 'GET aitest.views.home', "Request name")
        self.assertEqual(data['responseCode'], 200, "Status code")
        self.assertEqual(data['success'], True, "Success value")
        self.assertEqual(data['httpMethod'], 'GET', "HTTP Method")
        self.assertEqual(data['url'], 'http://testserver/', "Request url")

    def test_logger(self):
        response = self.client.get('/logger')
        self.assertEqual(response.status_code, 200)

        logev, reqev = self.get_events(2)

        # Check request event (minimal, since we validate this elsewhere)
        tags = reqev['tags']
        data = reqev['data']['baseData']
        reqid = tags['ai.operation.id']
        self.assertEqual(reqev['name'], 'Microsoft.ApplicationInsights.Request', "Event type")
        self.assertEqual(data['id'], reqid, "Request id")
        self.assertEqual(data['name'], 'GET aitest.views.logger', "Operation name")
        self.assertEqual(data['url'], 'http://testserver/logger', "Request url")

        self.assertTrue(reqid, "Request id not empty")

        # Check log event
        tags = logev['tags']
        data = logev['data']['baseData']
        self.assertEqual(logev['name'], 'Microsoft.ApplicationInsights.Message', "Event type")
        self.assertEqual(logev['iKey'], TEST_IKEY)
        self.assertEqual(tags['ai.operation.parentId'], reqid, "Parent id")
        self.assertEqual(data['message'], 'Logger message', "Log message")
        self.assertEqual(data['properties']['property'], 'value', "Property=value")

    def test_thrower(self):
        with self.assertRaises(ValueError):
            self.client.get('/thrower')

        errev, reqev = self.get_events(2)

        # Check request event
        tags = reqev['tags']
        data = reqev['data']['baseData']
        reqid = tags['ai.operation.id']
        self.assertEqual(reqev['name'], 'Microsoft.ApplicationInsights.Request', "Event type")
        self.assertEqual(reqev['iKey'], TEST_IKEY)
        self.assertEqual(data['id'], reqid, "Request id")
        self.assertEqual(data['responseCode'], 500, "Response code")
        self.assertEqual(data['success'], False, "Success value")
        self.assertEqual(data['name'], 'GET aitest.views.thrower', "Request name")
        self.assertEqual(data['url'], 'http://testserver/thrower', "Request url")

        self.assertTrue(reqid, "Request id not empty")

        # Check exception event
        tags = errev['tags']
        data = errev['data']['baseData']
        self.assertEqual(errev['name'], 'Microsoft.ApplicationInsights.Exception', "Event type")
        self.assertEqual(tags['ai.operation.parentId'], reqid, "Exception parent id")
        self.assertEqual(len(data['exceptions']), 1, "Exception count")
        exc = data['exceptions'][0]
        self.assertEqual(exc['typeName'], 'ValueError', "Exception type")
        self.assertEqual(exc['hasFullStack'], True, "Has full stack")
        self.assertEqual(exc['parsedStack'][0]['method'], 'thrower', "Stack frame method name")

    def test_error(self):
        response = self.client.get("/errorer")
        self.assertEqual(response.status_code, 404)

        event = self.get_events(1)
        tags = event['tags']
        data = event['data']['baseData']
        self.assertEqual(event['name'], 'Microsoft.ApplicationInsights.Request', "Event type")
        self.assertEqual(tags['ai.operation.name'], 'GET aitest.views.errorer', "Operation name")
        self.assertEqual(data['responseCode'], 404, "Status code")
        self.assertEqual(data['success'], False, "Success value")
        self.assertEqual(data['url'], 'http://testserver/errorer', "Request url")

    def test_no_view(self):
        response = self.client.get('/this/view/does/not/exist')
        self.assertEqual(response.status_code, 404)

        event = self.get_events(1)
        tags = event['tags']
        data = event['data']['baseData']
        self.assertEqual(event['name'], 'Microsoft.ApplicationInsights.Request', "Event type")
        self.assertEqual(data['responseCode'], 404, "Status code")
        self.assertEqual(data['success'], False, "Success value")
        self.assertEqual(data['name'], 'GET http://testserver/this/view/does/not/exist', "Request name")
        self.assertEqual(data['url'], 'http://testserver/this/view/does/not/exist', "Request url")

@override_settings(LOGGING={
    'version': 1,
    'handlers': {
        'appinsights': {
            'class': 'applicationinsights.django.LoggingHandler',
            'level': 'INFO',
        }
    },
    'loggers': {
        __name__: {
            'handlers': ['appinsights'],
            'level': 'INFO',
        }
    }
}, APPLICATION_INSIGHTS={'ikey': TEST_IKEY})
class LoggerTests(AITestCase):
    def test_log_error(self):
        django.setup()
        logger = logging.getLogger(__name__)
        msg = "An error log message"
        logger.error(msg)

        event = self.get_events(1)
        data = event['data']['baseData']
        props = data['properties']
        self.assertEqual(event['name'], 'Microsoft.ApplicationInsights.Message', "Event type")
        self.assertEqual(event['iKey'], TEST_IKEY)
        self.assertEqual(data['message'], msg, "Log message")
        self.assertEqual(data['severityLevel'], 3, "Severity level")
        self.assertEqual(props['fileName'], 'tests.py', "Filename property")
        self.assertEqual(props['level'], 'ERROR', "Level property")
        self.assertEqual(props['module'], 'tests', "Module property")

    def test_log_info(self):
        django.setup()
        logger = logging.getLogger(__name__)
        msg = "An info message"
        logger.info(msg)

        event = self.get_events(1)
        data = event['data']['baseData']
        props = data['properties']
        self.assertEqual(event['name'], 'Microsoft.ApplicationInsights.Message', "Event type")
        self.assertEqual(event['iKey'], TEST_IKEY)
        self.assertEqual(data['message'], msg, "Log message")
        self.assertEqual(data['severityLevel'], 1, "Severity level")
        self.assertEqual(props['fileName'], 'tests.py', "Filename property")
        self.assertEqual(props['level'], 'INFO', "Level property")
        self.assertEqual(props['module'], 'tests', "Module property")

def plug_sender():
    client = common.create_client()
    sender = MockSender()
    common.saved_client._channel = TelemetryChannel(None, SynchronousQueue(sender))
    return sender

class MockSender(SenderBase):
    def __init__(self):
        SenderBase.__init__(self, "https://dc.services.visualstudio.com/v2/track")
        self.events = []

    def send(self, data):
        self.events.extend(a.write() for a in data)
