import unittest
import platform
import locale

from test import test_support

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "..")
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import channel

class TestTelemetryContext(unittest.TestCase):
    def test_constructTelemetryContext(self):
        context = channel.TelemetryContext()
        self.assertIsNone(context.instrumentationKey)
        self.assertIsNotNone(context.device)
        self.assertEqual("Other", context.device.type)
        self.assertEqual(platform.node(), context.device.id)
        self.assertEqual(platform.version(), context.device.osVersion)
        self.assertEqual(locale.getdefaultlocale()[0], context.device.locale)
        self.assertIsNotNone(context.application)
        self.assertIsNotNone(context.user)
        self.assertIsNotNone(context.session)
        self.assertIsNotNone(context.operation)
        self.assertIsNotNone(context.location)
        self.assertIsNotNone(context.properties)

    def test_instrumentationKeyPropertyWorksAsExpected(self):
        context = channel.TelemetryContext()
        self.assertIsNone(context.instrumentationKey)
        context.instrumentationKey = "foo"
        self.assertEqual("foo", context.instrumentationKey)

    def test_devicePropertyWorksAsExpected(self):
        context = channel.TelemetryContext()
        self.assertIsNotNone(context.device)
        context.device = None
        self.assertIsNone(context.device)
        context.device = Exception()
        self.assertIsNone(context.device)
        context.device = channel.contracts.DeviceContext()
        self.assertIsNotNone(context.device)

    def test_applicationPropertyWorksAsExpected(self):
        context = channel.TelemetryContext()
        self.assertIsNotNone(context.application)
        context.application = None
        self.assertIsNone(context.application)
        context.application = Exception()
        self.assertIsNone(context.application)
        context.application = channel.contracts.ApplicationContext()
        self.assertIsNotNone(context.application)

    def test_userPropertyWorksAsExpected(self):
        context = channel.TelemetryContext()
        self.assertIsNotNone(context.user)
        context.user = None
        self.assertIsNone(context.user)
        context.user = Exception()
        self.assertIsNone(context.user)
        context.user = channel.contracts.UserContext()
        self.assertIsNotNone(context.user)

    def test_sessionPropertyWorksAsExpected(self):
        context = channel.TelemetryContext()
        self.assertIsNotNone(context.session)
        context.session = None
        self.assertIsNone(context.session)
        context.session = Exception()
        self.assertIsNone(context.session)
        context.session = channel.contracts.SessionContext()
        self.assertIsNotNone(context.session)

    def test_locationPropertyWorksAsExpected(self):
        context = channel.TelemetryContext()
        self.assertIsNotNone(context.location)
        context.location = None
        self.assertIsNone(context.location)
        context.location = Exception()
        self.assertIsNone(context.location)
        context.location = channel.contracts.LocationContext()
        self.assertIsNotNone(context.location)

    def test_operationPropertyWorksAsExpected(self):
        context = channel.TelemetryContext()
        self.assertIsNotNone(context.operation)
        context.operation = None
        self.assertIsNone(context.operation)
        context.operation = Exception()
        self.assertIsNone(context.operation)
        context.operation = channel.contracts.OperationContext()
        self.assertIsNotNone(context.operation)

    def test_propertiesPropertyWorksAsExpected(self):
        context = channel.TelemetryContext()
        self.assertIsNotNone(context.properties)
