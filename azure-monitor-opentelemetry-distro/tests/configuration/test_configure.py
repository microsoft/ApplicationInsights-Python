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
from unittest.mock import patch, Mock

from opentelemetry.semconv.resource import ResourceAttributes

from azure.monitor.opentelemetry.distro import configure_opentelemetry


class TestConfigure(unittest.TestCase):
    @patch(
        "azure.monitor.opentelemetry.distro.BatchSpanProcessor",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.AzureMonitorTraceExporter",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.TracerProvider",
        autospec=True,
    )
    @patch(
        "azure.monitor.opentelemetry.distro.Resource",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.trace",
    )
    def test_configure_opentelemetry(
        self,
        trace_mock,
        resource_mock,
        tp_mock,
        exporter_mock,
        bsp_mock,
    ):
        tp_init_mock = Mock()
        tp_mock.return_value = tp_init_mock
        exp_init_mock = Mock()
        exporter_mock.return_value = exp_init_mock
        resource_init_mock = Mock()
        resource_mock.create.return_value = resource_init_mock
        bsp_init_mock = Mock()
        bsp_mock.return_value = bsp_init_mock
        configure_opentelemetry(
            connection_string="test_cs",
            disable_tracing=False,
            service_name="test_service_name",
            service_namespace="test_namespace",
            service_instance_id="test_id",
        )
        resource_mock.create.assert_called_once_with({
            ResourceAttributes.SERVICE_NAME: "test_service_name",
            ResourceAttributes.SERVICE_NAMESPACE: "test_namespace",
            ResourceAttributes.SERVICE_INSTANCE_ID: "test_id",
        })
        tp_mock.assert_called_once_with(resource=resource_init_mock)
        trace_mock.set_tracer_provider.assert_called_once_with(tp_init_mock)
        exporter_mock.assert_called_once_with(connection_string="test_cs")
        bsp_mock.assert_called_once_with(exp_init_mock)

    @patch(
        "azure.monitor.opentelemetry.distro.BatchSpanProcessor",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.AzureMonitorTraceExporter",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.TracerProvider",
        autospec=True,
    )
    @patch(
        "azure.monitor.opentelemetry.distro.Resource",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.trace",
    )
    def test_configure_opentelemetry_disable_tracing(
        self,
        trace_mock,
        resource_mock,
        tp_mock,
        exporter_mock,
        bsp_mock,
    ):
        configure_opentelemetry(
            connection_string="test_cs",
            disable_tracing=True,
        )
        resource_mock.assert_not_called()
        tp_mock.assert_not_called()
        trace_mock.set_tracer_provider.assert_not_called()
        exporter_mock.assert_not_called()
        bsp_mock.assert_not_called()
