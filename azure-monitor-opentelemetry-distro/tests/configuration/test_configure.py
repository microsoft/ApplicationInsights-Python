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
from unittest.mock import Mock, patch, call

from azure.monitor.opentelemetry.distro import (
    configure_azure_monitor,
    _setup_instrumentations,
    _setup_tracing,
    _SUPPORTED_INSTRUMENTED_LIBRARIES,
)
from opentelemetry.semconv.resource import ResourceAttributes


class TestConfigure(unittest.TestCase):
    @patch(
        "azure.monitor.opentelemetry.distro.BatchSpanProcessor",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.AzureMonitorTraceExporter",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.get_tracer_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.set_tracer_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.TracerProvider",
        autospec=True,
    )
    @patch(
        "azure.monitor.opentelemetry.distro.ApplicationInsightsSampler",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.getLogger",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.LoggingHandler",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.BatchLogRecordProcessor",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.AzureMonitorLogExporter",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.get_logger_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.set_logger_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.LoggerProvider",
        autospec=True,
    )
    @patch(
        "azure.monitor.opentelemetry.distro.Resource",
    )
    def test_configure_azure_monitor(
        self,
        resource_mock,
        lp_mock,
        set_logger_provider_mock,
        get_logger_provider_mock,
        log_exporter_mock,
        blrp_mock,
        logging_handler_mock,
        get_logger_mock,
        sampler_mock,
        tp_mock,
        set_tracer_provider_mock,
        get_tracer_provider_mock,
        trace_exporter_mock,
        bsp_mock,
    ):
        resource_init_mock = Mock()
        resource_mock.create.return_value = resource_init_mock

        lp_init_mock = Mock()
        lp_mock.return_value = lp_init_mock
        get_logger_provider_mock.return_value = lp_init_mock
        log_exp_init_mock = Mock()
        log_exporter_mock.return_value = log_exp_init_mock
        blrp_init_mock = Mock()
        blrp_mock.return_value = blrp_init_mock
        logging_handler_init_mock = Mock()
        logging_handler_mock.return_value = logging_handler_init_mock
        logger_mock = Mock()
        get_logger_mock.return_value = logger_mock

        sampler_init_mock = Mock()
        sampler_mock.return_value = sampler_init_mock
        tp_init_mock = Mock()
        tp_mock.return_value = tp_init_mock
        get_tracer_provider_mock.return_value = tp_init_mock
        trace_exp_init_mock = Mock()
        trace_exporter_mock.return_value = trace_exp_init_mock
        bsp_init_mock = Mock()
        bsp_mock.return_value = bsp_init_mock

        configure_azure_monitor(
            connection_string="test_cs",
            console_exporting=False,
            disable_logging=False,
            disable_tracing=False,
            logging_export_interval_millis=10000,
            logging_level="test_logging_level",
            service_name="test_service_name",
            service_namespace="test_namespace",
            service_instance_id="test_id",
            sampling_ratio=0.5,
            tracing_export_interval_millis=15000,
        )
        resource_mock.create.assert_called_once_with(
            {
                ResourceAttributes.SERVICE_NAME: "test_service_name",
                ResourceAttributes.SERVICE_NAMESPACE: "test_namespace",
                ResourceAttributes.SERVICE_INSTANCE_ID: "test_id",
            }
        )

        lp_mock.assert_called_once_with(resource=resource_init_mock)
        set_logger_provider_mock.assert_called_once_with(lp_init_mock)
        get_logger_provider_mock.assert_called()
        log_exporter_mock.assert_called_once()
        blrp_mock.assert_called_once_with(
            log_exp_init_mock, export_timeout_millis=10000
        )
        lp_init_mock.add_log_record_processor.assert_called_once_with(
            blrp_init_mock
        )
        logging_handler_mock.assert_called_once_with(
            level="test_logging_level", logger_provider=lp_init_mock
        )
        get_logger_mock.assert_called_once_with()
        logger_mock.addHandler.assert_called_once_with(
            logging_handler_init_mock
        )

        sampler_mock.assert_called_once_with(sampling_ratio=0.5)
        tp_mock.assert_called_once_with(
            resource=resource_init_mock,
            sampler=sampler_init_mock,
        )
        set_tracer_provider_mock.assert_called_once_with(tp_init_mock)
        get_tracer_provider_mock.assert_called()
        trace_exporter_mock.assert_called_once()
        bsp_mock.assert_called_once_with(
            trace_exp_init_mock, export_timeout_millis=15000
        )
        tp_init_mock.add_span_processor(bsp_init_mock)

    @patch(
        "azure.monitor.opentelemetry.distro.BatchSpanProcessor",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.AzureMonitorTraceExporter",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.get_tracer_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.set_tracer_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.TracerProvider",
        autospec=True,
    )
    @patch(
        "azure.monitor.opentelemetry.distro.ApplicationInsightsSampler",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.getLogger",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.LoggingHandler",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.BatchLogRecordProcessor",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.AzureMonitorLogExporter",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.get_logger_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.set_logger_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.LoggerProvider",
        autospec=True,
    )
    @patch(
        "azure.monitor.opentelemetry.distro.Resource",
    )
    def test_configure_azure_monitor_disable_tracing_and_logging(
        self,
        resource_mock,
        lp_mock,
        set_logger_provider_mock,
        get_logger_provider_mock,
        log_exporter_mock,
        blrp_mock,
        logging_handler_mock,
        get_logger_mock,
        sampler_mock,
        tp_mock,
        set_tracer_provider_mock,
        get_tracer_provider_mock,
        trace_exporter_mock,
        bsp_mock,
    ):
        configure_azure_monitor(
            connection_string="test_cs",
            disable_logging=True,
            disable_tracing=True,
        )
        resource_mock.assert_not_called()

        lp_mock.assert_not_called()
        set_logger_provider_mock.assert_not_called()
        get_logger_provider_mock.assert_not_called()
        log_exporter_mock.assert_not_called()
        blrp_mock.assert_not_called()
        logging_handler_mock.assert_not_called()
        get_logger_mock.assert_not_called()

        sampler_mock.assert_not_called()
        tp_mock.assert_not_called()
        set_tracer_provider_mock.assert_not_called()
        get_tracer_provider_mock.assert_not_called()
        trace_exporter_mock.assert_not_called()
        bsp_mock.assert_not_called()

    @patch(
        "azure.monitor.opentelemetry.distro.BatchSpanProcessor",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.AzureMonitorTraceExporter",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.get_tracer_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.set_tracer_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.TracerProvider",
        autospec=True,
    )
    @patch(
        "azure.monitor.opentelemetry.distro.ApplicationInsightsSampler",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.getLogger",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.LoggingHandler",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.BatchLogRecordProcessor",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.AzureMonitorLogExporter",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.get_logger_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.set_logger_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.LoggerProvider",
        autospec=True,
    )
    @patch(
        "azure.monitor.opentelemetry.distro.Resource",
    )
    def test_configure_azure_monitor_disable_tracing(
        self,
        resource_mock,
        lp_mock,
        set_logger_provider_mock,
        get_logger_provider_mock,
        log_exporter_mock,
        blrp_mock,
        logging_handler_mock,
        get_logger_mock,
        sampler_mock,
        tp_mock,
        set_tracer_provider_mock,
        get_tracer_provider_mock,
        trace_exporter_mock,
        bsp_mock,
    ):
        resource_init_mock = Mock()
        resource_mock.create.return_value = resource_init_mock

        lp_init_mock = Mock()
        lp_mock.return_value = lp_init_mock
        get_logger_provider_mock.return_value = lp_init_mock
        log_exp_init_mock = Mock()
        log_exporter_mock.return_value = log_exp_init_mock
        blrp_init_mock = Mock()
        blrp_mock.return_value = blrp_init_mock
        logging_handler_init_mock = Mock()
        logging_handler_mock.return_value = logging_handler_init_mock
        logger_mock = Mock()
        get_logger_mock.return_value = logger_mock

        configure_azure_monitor(
            connection_string="test_cs",
            console_exporting=False,
            disable_logging=False,
            disable_tracing=True,
            logging_export_interval_millis=10000,
            logging_level="test_logging_level",
            service_name="test_service_name",
            service_namespace="test_namespace",
            service_instance_id="test_id",
        )
        resource_mock.create.assert_called_once_with(
            {
                ResourceAttributes.SERVICE_NAME: "test_service_name",
                ResourceAttributes.SERVICE_NAMESPACE: "test_namespace",
                ResourceAttributes.SERVICE_INSTANCE_ID: "test_id",
            }
        )

        lp_mock.assert_called_once_with(resource=resource_init_mock)
        set_logger_provider_mock.assert_called_once_with(lp_init_mock)
        get_logger_provider_mock.assert_called()
        log_exporter_mock.assert_called_once()
        blrp_mock.assert_called_once_with(
            log_exp_init_mock, export_timeout_millis=10000
        )
        lp_init_mock.add_log_record_processor.assert_called_once_with(
            blrp_init_mock
        )
        logging_handler_mock.assert_called_once_with(
            level="test_logging_level", logger_provider=lp_init_mock
        )
        get_logger_mock.assert_called_once_with()
        logger_mock.addHandler.assert_called_once_with(
            logging_handler_init_mock
        )

        sampler_mock.assert_not_called()
        tp_mock.assert_not_called()
        set_tracer_provider_mock.assert_not_called()
        get_tracer_provider_mock.assert_not_called()
        trace_exporter_mock.assert_not_called()
        bsp_mock.assert_not_called()

    @patch(
        "azure.monitor.opentelemetry.distro.BatchSpanProcessor",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.AzureMonitorTraceExporter",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.get_tracer_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.set_tracer_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.TracerProvider",
        autospec=True,
    )
    @patch(
        "azure.monitor.opentelemetry.distro.ApplicationInsightsSampler",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.getLogger",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.LoggingHandler",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.BatchLogRecordProcessor",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.AzureMonitorLogExporter",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.get_logger_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.set_logger_provider",
    )
    @patch(
        "azure.monitor.opentelemetry.distro.LoggerProvider",
        autospec=True,
    )
    @patch(
        "azure.monitor.opentelemetry.distro.Resource",
    )
    def test_configure_azure_monitor_disable_logging(
        self,
        resource_mock,
        lp_mock,
        set_logger_provider_mock,
        get_logger_provider_mock,
        log_exporter_mock,
        blrp_mock,
        logging_handler_mock,
        get_logger_mock,
        sampler_mock,
        tp_mock,
        set_tracer_provider_mock,
        get_tracer_provider_mock,
        trace_exporter_mock,
        bsp_mock,
    ):
        resource_init_mock = Mock()
        resource_mock.create.return_value = resource_init_mock

        sampler_init_mock = Mock()
        sampler_mock.return_value = sampler_init_mock
        tp_init_mock = Mock()
        tp_mock.return_value = tp_init_mock
        get_tracer_provider_mock.return_value = tp_init_mock
        trace_exp_init_mock = Mock()
        trace_exporter_mock.return_value = trace_exp_init_mock
        bsp_init_mock = Mock()
        bsp_mock.return_value = bsp_init_mock

        configure_azure_monitor(
            connection_string="test_cs",
            console_exporting=False,
            disable_logging=True,
            disable_tracing=False,
            logging_level="test_logging_level",
            service_name="test_service_name",
            service_namespace="test_namespace",
            service_instance_id="test_id",
            sampling_ratio=0.5,
            tracing_export_interval_millis=15000,
        )
        resource_mock.create.assert_called_once_with(
            {
                ResourceAttributes.SERVICE_NAME: "test_service_name",
                ResourceAttributes.SERVICE_NAMESPACE: "test_namespace",
                ResourceAttributes.SERVICE_INSTANCE_ID: "test_id",
            }
        )

        lp_mock.assert_not_called()
        set_logger_provider_mock.assert_not_called()
        get_logger_provider_mock.assert_not_called()
        log_exporter_mock.assert_not_called()
        blrp_mock.assert_not_called()
        logging_handler_mock.assert_not_called()
        get_logger_mock.assert_not_called()

        sampler_mock.assert_called_once_with(sampling_ratio=0.5)
        tp_mock.assert_called_once_with(
            resource=resource_init_mock,
            sampler=sampler_init_mock,
        )
        set_tracer_provider_mock.assert_called_once_with(tp_init_mock)
        get_tracer_provider_mock.assert_called()
        trace_exporter_mock.assert_called_once()
        bsp_mock.assert_called_once_with(
            trace_exp_init_mock, export_timeout_millis=15000
        )
        tp_init_mock.add_span_processor(bsp_init_mock)


    @patch("azure.monitor.opentelemetry.distro.getattr")
    def test_setup_instrumentations(
        self,         
        getattr_mock,
    ):
        for lib_name in _SUPPORTED_INSTRUMENTED_LIBRARIES:
            with patch("importlib.import_module") as import_module_mock:
                instrumentations = [lib_name]
                instrument_mock = Mock()
                instrumentor_mock = Mock()
                instrumentor_mock.return_value = instrument_mock
                getattr_mock.return_value = instrumentor_mock
                _setup_instrumentations(instrumentations)
                self.assertEqual(import_module_mock.call_count, 2)
                instr_lib_name = "opentelemetry.instrumentation." + lib_name
                import_module_mock.assert_has_calls([call(lib_name), call(instr_lib_name)])
                instrumentor_mock.assert_called_once()
                instrument_mock.instrument.assert_called_once()

    @patch("azure.monitor.opentelemetry.distro.getattr")
    def test_setup_instrumentations_lib_not_found(
        self,         
        getattr_mock,
    ):
        with patch("importlib.import_module") as import_module_mock:
            instrumentations = ["non_supported_lib"]
            instrument_mock = Mock()
            instrumentor_mock = Mock()
            instrumentor_mock.return_value = instrument_mock
            getattr_mock.return_value = instrumentor_mock
            _setup_instrumentations(instrumentations)
            import_module_mock.assert_not_called()
            instrumentor_mock.assert_not_called()
            instrument_mock.instrument.assert_not_called()

    @patch("azure.monitor.opentelemetry.distro.getattr")
    def test_setup_instrumentations_import_lib_failed(
        self,         
        getattr_mock,
    ):
        for lib_name in _SUPPORTED_INSTRUMENTED_LIBRARIES:
            with patch(
                "importlib.import_module",
                side_effect=ImportError()
            ) as import_module_mock:
                instrumentations = [lib_name]
                instrument_mock = Mock()
                instrumentor_mock = Mock()
                instrumentor_mock.return_value = instrument_mock
                getattr_mock.return_value = instrumentor_mock
                _setup_instrumentations(instrumentations)
                import_module_mock.assert_called_once()
                instrumentor_mock.assert_not_called()
                instrument_mock.instrument.assert_not_called()

    @patch("azure.monitor.opentelemetry.distro.getattr")
    def test_setup_instrumentations_import_instr_failed(
        self,         
        getattr_mock,
    ):
        for lib_name in _SUPPORTED_INSTRUMENTED_LIBRARIES:
            with patch("importlib.import_module") as import_module_mock:
                instrumentations = [lib_name]
                instrument_mock = Mock()
                instrumentor_mock = Mock()
                instrumentor_mock.return_value = instrument_mock
                getattr_mock.return_value = instrumentor_mock
                import_module_mock.side_effect = [None, ImportError()]
                _setup_instrumentations(instrumentations)
                instr_lib_name = "opentelemetry.instrumentation." + lib_name
                import_module_mock.assert_has_calls([call(lib_name), call(instr_lib_name)])
                instrumentor_mock.assert_not_called()
                instrument_mock.instrument.assert_not_called()

    @patch("azure.monitor.opentelemetry.distro.getattr")
    def test_setup_instrumentations_failed_general(
        self,         
        getattr_mock,
    ):
        for lib_name in _SUPPORTED_INSTRUMENTED_LIBRARIES:
            with patch("importlib.import_module") as import_module_mock:
                instrumentations = [lib_name]
                instrument_mock = Mock()
                instrumentor_mock = Mock()
                instrumentor_mock.return_value = instrument_mock
                getattr_mock.side_effect = Exception()
                _setup_instrumentations(instrumentations)
                self.assertEqual(import_module_mock.call_count, 2)
                instr_lib_name = "opentelemetry.instrumentation." + lib_name
                import_module_mock.assert_has_calls([call(lib_name), call(instr_lib_name)])
                instrumentor_mock.assert_not_called()
                instrument_mock.instrument.assert_not_called()

