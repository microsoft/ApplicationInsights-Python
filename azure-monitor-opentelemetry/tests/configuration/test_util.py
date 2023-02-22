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

from azure.monitor.opentelemetry.util import _get_configurations


class TestUtil(unittest.TestCase):
    def test_get_configurations(self):
        configurations = _get_configurations(
            connection_string="test_cs",
            disable_logging="test_disable_logging",
            disable_tracing="test_disable_tracing",
            instrumentations=["test_instrumentation"],
            logging_level="test_logging_level",
            logger_name="test_logger_name",
            service_name="test_service_name",
            service_namespace="test_namespace",
            service_instance_id="test_id",
            sampling_ratio="test_sample_ratio",
            tracing_export_interval="test_tracing_interval",
            logging_export_interval="test_logging_interval",
            metric_readers=("test_readers"),
            views=("test_view"),
        )

        self.assertEqual(configurations["connection_string"], "test_cs")
        self.assertEqual(
            configurations["disable_logging"], "test_disable_logging"
        )
        self.assertEqual(
            configurations["disable_tracing"], "test_disable_tracing"
        )
        self.assertEqual(
            configurations["instrumentations"], ["test_instrumentation"]
        )
        self.assertEqual(configurations["logging_level"], "test_logging_level")
        self.assertEqual(configurations["logger_name"], "test_logger_name")
        self.assertEqual(configurations["service_name"], "test_service_name")
        self.assertEqual(configurations["service_namespace"], "test_namespace")
        self.assertEqual(configurations["service_instance_id"], "test_id")
        self.assertEqual(configurations["sampling_ratio"], "test_sample_ratio")
        self.assertEqual(
            configurations["tracing_export_interval"], "test_tracing_interval"
        )
        self.assertEqual(
            configurations["logging_export_interval"], "test_logging_interval"
        )
        self.assertEqual(configurations["metric_readers"], ("test_readers"))
        self.assertEqual(configurations["views"], ("test_view"))
