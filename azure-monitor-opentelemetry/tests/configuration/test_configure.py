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
from unittest.mock import Mock, call, patch

from azure.monitor.opentelemetry._configure import (
    _SUPPORTED_INSTRUMENTED_LIBRARIES,
    _get_resource,
    _setup_instrumentations,
    _setup_logging,
    _setup_metrics,
    _setup_tracing,
    configure_azure_monitor,
)


class TestConfigure(unittest.TestCase):
    @patch(
        "azure.monitor.opentelemetry._configure._setup_instrumentations",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._setup_metrics",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._setup_logging",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._setup_tracing",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._get_resource",
    )
    def test_configure_azure_monitor(
        self,
        resource_mock,
        tracing_mock,
        logging_mock,
        metrics_mock,
        instrumentation_mock,
    ):
        kwargs = {
            "connection_string": "test_cs",
            "disable_tracing": False,
            "disable_logging": False,
            "disable_metrics": False,
            "logging_export_interval_millis": 10000,
            "logging_level": "test_logging_level",
            "logger_name": "test_logger_name",
            "metric_readers": "test_metric_readers",
            "service_name": "test_service_name",
            "service_namespace": "test_namespace",
            "service_instance_id": "test_id",
            "sampling_ratio": 0.5,
            "tracing_export_interval_millis": 15000,
            "views": "test_views",
        }
        resource_init_mock = Mock()
        resource_mock.return_value = resource_init_mock
        configure_azure_monitor(**kwargs)
        resource_mock.assert_called_once_with(kwargs)
        tracing_mock.assert_called_once_with(resource_init_mock, kwargs)
        logging_mock.assert_called_once_with(resource_init_mock, kwargs)
        metrics_mock.assert_called_once_with(resource_init_mock, kwargs)
        instrumentation_mock.assert_called_once_with(kwargs)

    @patch(
        "azure.monitor.opentelemetry._configure._setup_instrumentations",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._setup_metrics",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._setup_logging",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._setup_tracing",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._get_resource",
    )
    def test_configure_azure_monitor_disable_tracing(
        self,
        resource_mock,
        tracing_mock,
        logging_mock,
        metrics_mock,
        instrumentation_mock,
    ):
        kwargs = {
            "connection_string": "test_cs",
            "disable_tracing": True,
            "disable_logging": False,
            "disable_metrics": False,
            "logging_export_interval_millis": 10000,
            "logging_level": "test_logging_level",
            "logger_name": "test_logger_name",
            "service_name": "test_service_name",
            "service_namespace": "test_namespace",
            "service_instance_id": "test_id",
            "sampling_ratio": 0.5,
            "tracing_export_interval_millis": 15000,
            "views": "test_views",
        }
        resource_init_mock = Mock()
        resource_mock.return_value = resource_init_mock
        configure_azure_monitor(**kwargs)
        resource_mock.assert_called_once_with(kwargs)
        tracing_mock.assert_not_called()
        logging_mock.assert_called_once_with(resource_init_mock, kwargs)
        metrics_mock.assert_called_once_with(resource_init_mock, kwargs)
        instrumentation_mock.assert_called_once_with(kwargs)

    @patch(
        "azure.monitor.opentelemetry._configure._setup_instrumentations",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._setup_metrics",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._setup_logging",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._setup_tracing",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._get_resource",
    )
    def test_configure_azure_monitor_disable_logging(
        self,
        resource_mock,
        tracing_mock,
        logging_mock,
        metrics_mock,
        instrumentation_mock,
    ):
        kwargs = {
            "connection_string": "test_cs",
            "disable_tracing": False,
            "disable_logging": True,
            "disable_metrics": False,
            "logging_export_interval_millis": 10000,
            "logging_level": "test_logging_level",
            "logger_name": "test_logger_name",
            "service_name": "test_service_name",
            "service_namespace": "test_namespace",
            "service_instance_id": "test_id",
            "sampling_ratio": 0.5,
            "tracing_export_interval_millis": 15000,
            "views": "test_views",
        }
        resource_init_mock = Mock()
        resource_mock.return_value = resource_init_mock
        configure_azure_monitor(**kwargs)
        resource_mock.assert_called_once_with(kwargs)
        tracing_mock.assert_called_once_with(resource_init_mock, kwargs)
        logging_mock.assert_not_called()
        metrics_mock.assert_called_once_with(resource_init_mock, kwargs)
        instrumentation_mock.assert_called_once_with(kwargs)

    @patch(
        "azure.monitor.opentelemetry._configure._setup_instrumentations",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._setup_metrics",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._setup_logging",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._setup_tracing",
    )
    @patch(
        "azure.monitor.opentelemetry._configure._get_resource",
    )
    def test_configure_azure_monitor_disable_metrics(
        self,
        resource_mock,
        tracing_mock,
        logging_mock,
        metrics_mock,
        instrumentation_mock,
    ):
        kwargs = {
            "connection_string": "test_cs",
            "disable_tracing": False,
            "disable_logging": False,
            "disable_metrics": True,
            "logging_export_interval_millis": 10000,
            "logging_level": "test_logging_level",
            "service_name": "test_service_name",
            "service_namespace": "test_namespace",
            "service_instance_id": "test_id",
            "sampling_ratio": 0.5,
            "tracing_export_interval_millis": 15000,
            "views": "test_views",
        }
        resource_init_mock = Mock()
        resource_mock.return_value = resource_init_mock
        configure_azure_monitor(**kwargs)
        resource_mock.assert_called_once_with(kwargs)
        tracing_mock.assert_called_once_with(resource_init_mock, kwargs)
        logging_mock.assert_called_once_with(resource_init_mock, kwargs)
        metrics_mock.assert_not_called()
        instrumentation_mock.assert_called_once_with(kwargs)

    def test_get_resource(self):
        configuration = {"resource": "test_resource"}
        res = _get_resource(configuration)
        self.assertEqual(res, "test_resource")

    @patch(
        "azure.monitor.opentelemetry._configure.Resource",
    )
    def test_get_resource_default(self, resource_mock):
        configuration = {}
        _get_resource(configuration)
        resource_mock.create.assert_called_once_with()

    @patch(
        "azure.monitor.opentelemetry._configure.BatchSpanProcessor",
    )
    @patch(
        "azure.monitor.opentelemetry._configure.AzureMonitorTraceExporter",
    )
    @patch(
        "azure.monitor.opentelemetry._configure.get_tracer_provider",
    )
    @patch(
        "azure.monitor.opentelemetry._configure.set_tracer_provider",
    )
    @patch(
        "azure.monitor.opentelemetry._configure.TracerProvider",
        autospec=True,
    )
    @patch(
        "azure.monitor.opentelemetry._configure.ApplicationInsightsSampler",
    )
    def test_setup_tracing(
        self,
        sampler_mock,
        tp_mock,
        set_tracer_provider_mock,
        get_tracer_provider_mock,
        trace_exporter_mock,
        bsp_mock,
    ):
        resource_mock = Mock()
        sampler_init_mock = Mock()
        sampler_mock.return_value = sampler_init_mock
        tp_init_mock = Mock()
        tp_mock.return_value = tp_init_mock
        get_tracer_provider_mock.return_value = tp_init_mock
        trace_exp_init_mock = Mock()
        trace_exporter_mock.return_value = trace_exp_init_mock
        bsp_init_mock = Mock()
        bsp_mock.return_value = bsp_init_mock

        configurations = {
            "connection_string": "test_cs",
            "disable_tracing": False,
            "sampling_ratio": 0.5,
            "tracing_export_interval_millis": 15000,
        }
        _setup_tracing(resource_mock, configurations)
        sampler_mock.assert_called_once_with(sampling_ratio=0.5)
        tp_mock.assert_called_once_with(
            resource=resource_mock,
            sampler=sampler_init_mock,
        )
        set_tracer_provider_mock.assert_called_once_with(tp_init_mock)
        get_tracer_provider_mock.assert_called()
        trace_exporter_mock.assert_called_once()
        bsp_mock.assert_called_once_with(
            trace_exp_init_mock, schedule_delay_millis=15000
        )
        tp_init_mock.add_span_processor.assert_called_once_with(bsp_init_mock)

    @patch(
        "azure.monitor.opentelemetry._configure.getLogger",
    )
    @patch(
        "azure.monitor.opentelemetry._configure.LoggingHandler",
    )
    @patch(
        "azure.monitor.opentelemetry._configure.BatchLogRecordProcessor",
    )
    @patch(
        "azure.monitor.opentelemetry._configure.AzureMonitorLogExporter",
    )
    @patch(
        "azure.monitor.opentelemetry._configure.get_logger_provider",
    )
    @patch(
        "azure.monitor.opentelemetry._configure.set_logger_provider",
    )
    @patch(
        "azure.monitor.opentelemetry._configure.LoggerProvider",
        autospec=True,
    )
    def test_setup_logging(
        self,
        lp_mock,
        set_logger_provider_mock,
        get_logger_provider_mock,
        log_exporter_mock,
        blrp_mock,
        logging_handler_mock,
        get_logger_mock,
    ):
        resource_mock = Mock()

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

        configurations = {
            "connection_string": "test_cs",
            "disable_logging": False,
            "logging_export_interval_millis": 10000,
            "logging_level": "test_logging_level",
            "logger_name": "test_logger_name",
        }
        _setup_logging(resource_mock, configurations)

        lp_mock.assert_called_once_with(resource=resource_mock)
        set_logger_provider_mock.assert_called_once_with(lp_init_mock)
        get_logger_provider_mock.assert_called()
        log_exporter_mock.assert_called_once()
        blrp_mock.assert_called_once_with(
            log_exp_init_mock, schedule_delay_millis=10000
        )
        lp_init_mock.add_log_record_processor.assert_called_once_with(
            blrp_init_mock
        )
        logging_handler_mock.assert_called_once_with(
            level="test_logging_level", logger_provider=lp_init_mock
        )
        get_logger_mock.assert_called_once_with("test_logger_name")
        logger_mock.addHandler.assert_called_once_with(
            logging_handler_init_mock
        )

    @patch(
        "azure.monitor.opentelemetry._configure.PeriodicExportingMetricReader",
    )
    @patch(
        "azure.monitor.opentelemetry._configure.AzureMonitorMetricExporter",
    )
    @patch(
        "azure.monitor.opentelemetry._configure.set_meter_provider",
    )
    @patch(
        "azure.monitor.opentelemetry._configure.MeterProvider",
        autospec=True,
    )
    def test_setup_metrics(
        self,
        mp_mock,
        set_meter_provider_mock,
        metric_exporter_mock,
        reader_mock,
    ):
        resource_mock = Mock()
        mp_init_mock = Mock()
        mp_mock.return_value = mp_init_mock
        metric_exp_init_mock = Mock()
        metric_exporter_mock.return_value = metric_exp_init_mock
        reader_init_mock = Mock()
        reader_mock.return_value = reader_init_mock

        configurations = {
            "connection_string": "test_cs",
            "disable_metrics": False,
            "metric_readers": ["test_reader1", "test_reader2"],
            "views": "test_views",
        }
        _setup_metrics(resource_mock, configurations)
        mp_mock.assert_called_once_with(
            metric_readers=[reader_init_mock, "test_reader1", "test_reader2"],
            resource=resource_mock,
            views="test_views",
        )
        set_meter_provider_mock.assert_called_once_with(mp_init_mock)
        metric_exporter_mock.assert_called_once()
        reader_mock.assert_called_once_with(metric_exp_init_mock)

    @patch("azure.monitor.opentelemetry._configure.getattr")
    def test_setup_instrumentations(
        self,
        getattr_mock,
    ):
        with patch("importlib.import_module") as import_module_mock:
            configurations = {}
            instrument_mock = Mock()
            instrumentor_mock = Mock()
            instrumentor_mock.return_value = instrument_mock
            getattr_mock.return_value = instrumentor_mock
            _setup_instrumentations(configurations)
            self.assertEqual(
                import_module_mock.call_count,
                len(_SUPPORTED_INSTRUMENTED_LIBRARIES) * 2,
            )
            import_calls = []
            for lib_name in _SUPPORTED_INSTRUMENTED_LIBRARIES:
                import_calls.append(call(lib_name))
                import_calls.append(
                    call("opentelemetry.instrumentation." + lib_name)
                )
            import_module_mock.assert_has_calls(import_calls)
            self.assertEqual(
                instrumentor_mock.call_count,
                len(_SUPPORTED_INSTRUMENTED_LIBRARIES),
            )
            self.assertEqual(
                instrument_mock.instrument.call_count,
                len(_SUPPORTED_INSTRUMENTED_LIBRARIES),
            )

    @patch("azure.monitor.opentelemetry._configure.getattr")
    def test_setup_instrumentations_lib_excluded(
        self,
        getattr_mock,
    ):
        instr_exclude = _SUPPORTED_INSTRUMENTED_LIBRARIES[0]
        with patch("importlib.import_module") as import_module_mock:
            configurations = {"exclude_instrumentations": [instr_exclude]}
            instrument_mock = Mock()
            instrumentor_mock = Mock()
            instrumentor_mock.return_value = instrument_mock
            getattr_mock.return_value = instrumentor_mock
            _setup_instrumentations(configurations)
            assert call(instr_exclude) not in import_module_mock.mock_calls
            self.assertEqual(
                len(_SUPPORTED_INSTRUMENTED_LIBRARIES) - 1,
                instrument_mock.instrument.call_count,
            )

    @patch("azure.monitor.opentelemetry._configure._logger")
    @patch("azure.monitor.opentelemetry._configure.getattr")
    def test_setup_instrumentations_import_lib_failed(
        self,
        getattr_mock,
        logger_mock,
    ):
        with patch(
            "importlib.import_module", side_effect=ImportError()
        ) as import_module_mock:
            instrument_mock = Mock()
            instrumentor_mock = Mock()
            instrumentor_mock.return_value = instrument_mock
            getattr_mock.return_value = instrumentor_mock
            _setup_instrumentations({})
            self.assertEqual(
                len(_SUPPORTED_INSTRUMENTED_LIBRARIES),
                import_module_mock.call_count,
            )
            self.assertEqual(
                len(_SUPPORTED_INSTRUMENTED_LIBRARIES),
                logger_mock.warning.call_count,
            )
            instrumentor_mock.assert_not_called()
            instrument_mock.instrument.assert_not_called()

    @patch("azure.monitor.opentelemetry._configure._logger")
    @patch("azure.monitor.opentelemetry._configure.getattr")
    def test_setup_instrumentations_import_instr_failed(
        self,
        getattr_mock,
        logger_mock,
    ):
        with patch("importlib.import_module") as import_module_mock:
            instrument_mock = Mock()
            instrumentor_mock = Mock()
            instrumentor_mock.return_value = instrument_mock
            getattr_mock.return_value = instrumentor_mock
            side_effect_calls = []
            for _ in _SUPPORTED_INSTRUMENTED_LIBRARIES:
                side_effect_calls.append(None)
                side_effect_calls.append(ImportError())
            import_module_mock.side_effect = side_effect_calls
            _setup_instrumentations({})
            import_calls = []
            for lib_name in _SUPPORTED_INSTRUMENTED_LIBRARIES:
                import_calls.append(call(lib_name))
                import_calls.append(
                    call("opentelemetry.instrumentation." + lib_name)
                )
            import_module_mock.assert_has_calls(import_calls)
            self.assertEqual(
                len(_SUPPORTED_INSTRUMENTED_LIBRARIES),
                logger_mock.warning.call_count,
            )
            instrumentor_mock.assert_not_called()
            instrument_mock.instrument.assert_not_called()

    @patch("azure.monitor.opentelemetry._configure._logger")
    @patch("azure.monitor.opentelemetry._configure.getattr")
    def test_setup_instrumentations_failed_general(
        self,
        getattr_mock,
        logger_mock,
    ):
        with patch("importlib.import_module"):
            instrument_mock = Mock()
            instrumentor_mock = Mock()
            instrumentor_mock.return_value = instrument_mock
            side_effect_calls = []
            for _ in _SUPPORTED_INSTRUMENTED_LIBRARIES:
                side_effect_calls.append(Exception())
            getattr_mock.side_effect = side_effect_calls
            _setup_instrumentations({})
            import_calls = []
            for lib_name in _SUPPORTED_INSTRUMENTED_LIBRARIES:
                import_calls.append(call(lib_name))
                import_calls.append(
                    call("opentelemetry.instrumentation." + lib_name)
                )
            instrumentor_mock.assert_not_called()
            instrument_mock.instrument.assert_not_called()

    @patch("azure.monitor.opentelemetry._configure.getattr")
    def test_setup_instrumentations_custom_configuration(
        self,
        getattr_mock,
    ):
        with patch("importlib.import_module"):
            config_libr_name = _SUPPORTED_INSTRUMENTED_LIBRARIES[0]
            configurations = {
                config_libr_name + "_config": {"test_key": "test_value"},
            }
            instrument_mock = Mock()
            instrumentor_mock = Mock()
            instrumentor_mock.return_value = instrument_mock
            getattr_mock.return_value = instrumentor_mock
            _setup_instrumentations(configurations)
            instrument_calls = [{"test_key": "test_value"}]
            for _ in _SUPPORTED_INSTRUMENTED_LIBRARIES[1:-1]:
                instrument_calls.append(call())

    @patch("azure.monitor.opentelemetry._configure.getattr")
    def test_setup_instrumentations_custom_configuration_excluded(
        self,
        getattr_mock,
    ):
        with patch("importlib.import_module"):
            config_libr_name = _SUPPORTED_INSTRUMENTED_LIBRARIES[0]
            configurations = {
                "exclude_instrumentations": [config_libr_name],
                config_libr_name + "_config": {"test_key": "test_value"},
            }
            instrument_mock = Mock()
            instrumentor_mock = Mock()
            instrumentor_mock.return_value = instrument_mock
            getattr_mock.return_value = instrumentor_mock
            _setup_instrumentations(configurations)
            assert (
                call({"test_key": "test_value"})
                not in instrument_mock.instrument.mock_calls
            )

    @patch("azure.monitor.opentelemetry._configure.getattr")
    def test_setup_instrumentations_custom_configuration_incorrect(
        self,
        getattr_mock,
    ):
        with patch("importlib.import_module"):
            config_libr_name = _SUPPORTED_INSTRUMENTED_LIBRARIES[0]
            configurations = {
                config_libr_name
                + "incorrect_config": {"test_key": "test_value"},
            }
            instrument_mock = Mock()
            instrumentor_mock = Mock()
            instrumentor_mock.return_value = instrument_mock
            getattr_mock.return_value = instrumentor_mock
            _setup_instrumentations(configurations)
            instrument_calls = []
            for _ in _SUPPORTED_INSTRUMENTED_LIBRARIES:
                instrument_calls.append(call())
            instrument_mock.instrument.has_calls(instrument_calls)
