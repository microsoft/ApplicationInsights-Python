# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from azure.monitor.opentelemetry.distro.util import get_configurations


class TestUtil(unittest.TestCase):
    def test_get_configurations(self):
        configurations = get_configurations(
            connection_string="test_cs",
            disable_tracing="test_disable",
            service_name="test_service_name",
            service_namespace="test_namespace",
            service_instance_id="test_id",
        )

        self.assertEqual(configurations["connection_string"], "test_cs")
        self.assertEqual(configurations["disable_tracing"], "test_disable")
        self.assertEqual(configurations["service_name"], "test_service_name")
        self.assertEqual(configurations["service_namespace"], "test_namespace")
        self.assertEqual(configurations["service_instance_id"], "test_id")

    def test_get_configurations_default(self):
        configurations = get_configurations()
        self.assertEqual(configurations["connection_string"], None)
        self.assertEqual(configurations["disable_tracing"], False)
        self.assertEqual(configurations["service_name"], "")
        self.assertEqual(configurations["service_namespace"], "")
        self.assertEqual(configurations["service_instance_id"], "")
