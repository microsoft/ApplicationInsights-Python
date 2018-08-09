import unittest
import platform
import locale

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..')
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import channel


class TestTelemetryContext(unittest.TestCase):
    def test_construct(self):
        context = channel.TelemetryContext()
        self.assertIsNone(context.instrumentation_key)
        self.assertIsNotNone(context.device)
        self.assertEqual("Other", context.device.type)
        self.assertEqual(platform.node(), context.device.id)
        self.assertEqual(platform.version(), context.device.os_version)
        self.assertEqual(locale.getdefaultlocale()[0], context.device.locale)
        self.assertIsNotNone(context.cloud)
        self.assertIsNotNone(context.application)
        self.assertIsNotNone(context.user)
        self.assertIsNotNone(context.session)
        self.assertIsNotNone(context.operation)
        self.assertIsNotNone(context.location)
        self.assertIsNotNone(context.properties)

    def test_instrumentation_key_attribute_works_as_expected(self):
        context = channel.TelemetryContext()
        self.assertIsNone(context.instrumentation_key)
        context.instrumentation_key = "foo"
        self.assertEqual("foo", context.instrumentation_key)

    def test_device_attribute_works_as_expected(self):
        context = channel.TelemetryContext()
        self.assertIsNotNone(context.device)
        context.device = None
        self.assertIsNone(context.device)
        context.device = Exception()
        self.assertIsNotNone(context.device)
        self.assertIsInstance(context.device, Exception)
        context.device = channel.contracts.Device()
        self.assertIsNotNone(context.device)
        self.assertIsInstance(context.device, channel.contracts.Device)

    def test_cloud_attribute_works_as_expected(self):
        context = channel.TelemetryContext()
        self.assertIsNotNone(context.cloud)
        context.cloud = None
        self.assertIsNone(context.cloud)
        context.cloud = Exception()
        self.assertIsNotNone(context.cloud)
        self.assertIsInstance(context.cloud, Exception)
        context.cloud = channel.contracts.Cloud()
        self.assertIsNotNone(context.cloud)
        self.assertIsInstance(context.cloud, channel.contracts.Cloud)

    def test_application_attribute_works_as_expected(self):
        context = channel.TelemetryContext()
        self.assertIsNotNone(context.application)
        context.application = None
        self.assertIsNone(context.application)
        context.application = Exception()
        self.assertIsNotNone(context.application)
        self.assertIsInstance(context.application, Exception)
        context.application = channel.contracts.Application()
        self.assertIsNotNone(context.application)
        self.assertIsInstance(context.application, channel.contracts.Application)

    def test_user_attribute_works_as_expected(self):
        context = channel.TelemetryContext()
        self.assertIsNotNone(context.user)
        context.user = None
        self.assertIsNone(context.user)
        context.user = Exception()
        self.assertIsNotNone(context.user)
        self.assertIsInstance(context.user, Exception)
        context.user = channel.contracts.User()
        self.assertIsNotNone(context.user)
        self.assertIsInstance(context.user, channel.contracts.User)

    def test_session_attribute_works_as_expected(self):
        context = channel.TelemetryContext()
        self.assertIsNotNone(context.session)
        context.session = None
        self.assertIsNone(context.session)
        context.session = Exception()
        self.assertIsNotNone(context.session)
        self.assertIsInstance(context.session, Exception)
        context.session = channel.contracts.Session()
        self.assertIsNotNone(context.session)
        self.assertIsInstance(context.session, channel.contracts.Session)

    def test_location_attribute_works_as_expected(self):
        context = channel.TelemetryContext()
        self.assertIsNotNone(context.location)
        context.location = None
        self.assertIsNone(context.location)
        context.location = Exception()
        self.assertIsNotNone(context.location)
        self.assertIsInstance(context.location, Exception)
        context.location = channel.contracts.Location()
        self.assertIsNotNone(context.location)
        self.assertIsInstance(context.location, channel.contracts.Location)

    def test_operation_attribute_works_as_expected(self):
        context = channel.TelemetryContext()
        self.assertIsNotNone(context.operation)
        context.operation = None
        self.assertIsNone(context.operation)
        context.operation = Exception()
        self.assertIsNotNone(context.operation)
        self.assertIsInstance(context.operation, Exception)
        context.operation = channel.contracts.Operation()
        self.assertIsNotNone(context.operation)
        self.assertIsInstance(context.operation, channel.contracts.Operation)

    def test_properties_property_works_as_expected(self):
        context = channel.TelemetryContext()
        self.assertIsNotNone(context.properties)
