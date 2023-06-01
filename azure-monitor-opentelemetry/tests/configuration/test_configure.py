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
    _get_extra_exporters,
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
    def test_configure_azure_monitor(
        self,
        tracing_mock,
        logging_mock,
        metrics_mock,
        instrumentation_mock,
    ):
        kwargs = {
            "connection_string": "test_cs",
        }
        configure_azure_monitor(**kwargs)
        tracing_mock.assert_called_once()
        logging_mock.assert_called_once()
        metrics_mock.assert_called_once()
        instrumentation_mock.assert_called_once_with()

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
        "azure.monitor.opentelemetry._configure._get_configurations",
    )
    def test_configure_azure_monitor_disable_tracing(
        self,
        config_mock,
        tracing_mock,
        logging_mock,
        metrics_mock,
        instrumentation_mock,
    ):
        configurations = {
            "connection_string": "test_cs",
            "disable_tracing": True,
            "disable_logging": False,
            "disable_metrics": False,
        }
        config_mock.return_value = configurations
        configure_azure_monitor()
        tracing_mock.assert_not_called()
        logging_mock.assert_called_once_with(configurations)
        metrics_mock.assert_called_once_with(configurations)
        instrumentation_mock.assert_called_once_with()

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
        "azure.monitor.opentelemetry._configure._get_configurations",
    )
    def test_configure_azure_monitor_disable_logging(
        self,
        config_mock,
        tracing_mock,
        logging_mock,
        metrics_mock,
        instrumentation_mock,
    ):
        configurations = {
            "connection_string": "test_cs",
            "disable_tracing": False,
            "disable_logging": True,
            "disable_metrics": False,
        }
        config_mock.return_value = configurations
        configure_azure_monitor()
        tracing_mock.assert_called_once_with(configurations)
        logging_mock.assert_not_called()
        metrics_mock.assert_called_once_with(configurations)
        instrumentation_mock.assert_called_once_with()

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
        "azure.monitor.opentelemetry._configure._get_configurations",
    )
    def test_configure_azure_monitor_disable_metrics(
        self,
        config_mock,
        tracing_mock,
        logging_mock,
        metrics_mock,
        instrumentation_mock,
    ):
        configurations = {
            "connection_string": "test_cs",
            "disable_tracing": False,
            "disable_logging": False,
            "disable_metrics": True,
        }
        config_mock.return_value = configurations
        configure_azure_monitor()
        tracing_mock.assert_called_once_with(configurations)
        logging_mock.assert_called_once_with(configurations)
        metrics_mock.assert_not_called()
        instrumentation_mock.assert_called_once_with()

    @patch(
        "azure.monitor.opentelemetry._configure._get_extra_exporters",
    )
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
        extra_exporters_mock,
    ):
        sampler_init_mock = Mock()
        sampler_mock.return_value = sampler_init_mock
        tp_init_mock = Mock()
        tp_mock.return_value = tp_init_mock
        get_tracer_provider_mock.return_value = tp_init_mock
        trace_exp_init_mock = Mock()
        trace_exporter_mock.return_value = trace_exp_init_mock
        bsp_init_mock = Mock()
        bsp_mock.return_value = bsp_init_mock
        custom_exporter_mock1 = Mock()
        custom_exporter_mock2 = Mock()
        extra_exporters_mock.return_value = [
            custom_exporter_mock1,
            custom_exporter_mock2,
        ]

        configurations = {
            "connection_string": "test_cs",
            "sampling_ratio": 0.5,
        }
        _setup_tracing(configurations)
        sampler_mock.assert_called_once_with(sampling_ratio=0.5)
        tp_mock.assert_called_once_with(
            sampler=sampler_init_mock,
        )
        set_tracer_provider_mock.assert_called_once_with(tp_init_mock)
        get_tracer_provider_mock.assert_called()
        trace_exporter_mock.assert_called_once_with(**configurations)
        bsp_mock.assert_has_calls(
            [
                call(trace_exp_init_mock),
                call(custom_exporter_mock1),
                call(custom_exporter_mock2),
            ]
        )
        tp_init_mock.add_span_processor.assert_has_calls(
            [call(bsp_init_mock), call(bsp_init_mock), call(bsp_init_mock)]
        )

    @patch(
        "azure.monitor.opentelemetry._configure._get_extra_exporters",
    )
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
        extra_exporters_mock,
    ):
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
        custom_exporter_mock1 = Mock()
        custom_exporter_mock2 = Mock()
        extra_exporters_mock.return_value = [
            custom_exporter_mock1,
            custom_exporter_mock2,
        ]

        configurations = {
            "connection_string": "test_cs",
            "logging_export_interval_ms": 10000,
        }
        _setup_logging(configurations)

        lp_mock.assert_called_once_with()
        set_logger_provider_mock.assert_called_once_with(lp_init_mock)
        get_logger_provider_mock.assert_called()
        log_exporter_mock.assert_called_once_with(**configurations)
        blrp_mock.assert_has_calls(
            [
                call(log_exp_init_mock, schedule_delay_millis=10000),
                call(custom_exporter_mock1, schedule_delay_millis=10000),
                call(custom_exporter_mock2, schedule_delay_millis=10000),
            ]
        )
        lp_init_mock.add_log_record_processor.assert_has_calls(
            [call(blrp_init_mock), call(blrp_init_mock), call(blrp_init_mock)]
        )
        logging_handler_mock.assert_called_once_with(
            logger_provider=lp_init_mock
        )
        get_logger_mock.assert_called_once_with()
        logger_mock.addHandler.assert_called_once_with(
            logging_handler_init_mock
        )

    @patch(
        "azure.monitor.opentelemetry._configure._get_extra_exporters",
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
        extra_exporters_mock,
    ):
        mp_init_mock = Mock()
        mp_mock.return_value = mp_init_mock
        metric_exp_init_mock = Mock()
        metric_exporter_mock.return_value = metric_exp_init_mock
        reader_init_mock = Mock()
        reader_mock.return_value = reader_init_mock
        custom_exporter_mock1 = Mock()
        custom_exporter_mock2 = Mock()
        extra_exporters_mock.return_value = [
            custom_exporter_mock1,
            custom_exporter_mock2,
        ]

        configurations = {
            "connection_string": "test_cs",
        }
        _setup_metrics(configurations)
        mp_mock.assert_called_once_with(
            metric_readers=[
                reader_init_mock,
                reader_init_mock,
                reader_init_mock,
            ],
        )
        set_meter_provider_mock.assert_called_once_with(mp_init_mock)
        metric_exporter_mock.assert_called_once_with(**configurations)
        reader_mock.assert_has_calls(
            [
                call(metric_exp_init_mock),
                call(custom_exporter_mock1),
                call(custom_exporter_mock2),
            ]
        )

    @patch(
        "azure.monitor.opentelemetry._configure.get_dist_dependency_conflicts"
    )
    @patch("azure.monitor.opentelemetry._configure.iter_entry_points")
    def test_setup_instrumentations_lib_not_supported(
        self,
        iter_mock,
        dep_mock,
    ):
        ep_mock = Mock()
        ep2_mock = Mock()
        iter_mock.return_value = (ep_mock, ep2_mock)
        instrumentor_mock = Mock()
        instr_class_mock = Mock()
        instr_class_mock.return_value = instrumentor_mock
        ep_mock.name = "test_instr"
        ep2_mock.name = _SUPPORTED_INSTRUMENTED_LIBRARIES[1]
        ep2_mock.load.return_value = instr_class_mock
        dep_mock.return_value = None
        _setup_instrumentations()
        dep_mock.assert_called_with(ep2_mock.dist)
        ep_mock.load.assert_not_called()
        ep2_mock.load.assert_called_once()
        instrumentor_mock.instrument.assert_called_once()

    @patch("azure.monitor.opentelemetry._configure._logger")
    @patch(
        "azure.monitor.opentelemetry._configure.get_dist_dependency_conflicts"
    )
    @patch("azure.monitor.opentelemetry._configure.iter_entry_points")
    def test_setup_instrumentations_conflict(
        self,
        iter_mock,
        dep_mock,
        logger_mock,
    ):
        ep_mock = Mock()
        iter_mock.return_value = (ep_mock,)
        instrumentor_mock = Mock()
        instr_class_mock = Mock()
        instr_class_mock.return_value = instrumentor_mock
        ep_mock.name = _SUPPORTED_INSTRUMENTED_LIBRARIES[0]
        ep_mock.load.return_value = instr_class_mock
        dep_mock.return_value = True
        _setup_instrumentations()
        dep_mock.assert_called_with(ep_mock.dist)
        ep_mock.load.assert_not_called()
        instrumentor_mock.instrument.assert_not_called()
        logger_mock.debug.assert_called_once()

    @patch("azure.monitor.opentelemetry._configure._logger")
    @patch(
        "azure.monitor.opentelemetry._configure.get_dist_dependency_conflicts"
    )
    @patch("azure.monitor.opentelemetry._configure.iter_entry_points")
    def test_setup_instrumentations_exception(
        self,
        iter_mock,
        dep_mock,
        logger_mock,
    ):
        ep_mock = Mock()
        iter_mock.return_value = (ep_mock,)
        instrumentor_mock = Mock()
        instr_class_mock = Mock()
        instr_class_mock.return_value = instrumentor_mock
        ep_mock.name = _SUPPORTED_INSTRUMENTED_LIBRARIES[0]
        ep_mock.load.side_effect = Exception()
        dep_mock.return_value = None
        _setup_instrumentations()
        dep_mock.assert_called_with(ep_mock.dist)
        ep_mock.load.assert_called_once()
        instrumentor_mock.instrument.assert_not_called()
        logger_mock.warning.assert_called_once()

    @patch.dict(
        "os.environ",
        {
            "EXPORTER_ENV_VAR": "custom_exporter1,azure_monitor_opentelemetry_exporter,custom_exporter2"
        },
    )
    @patch("azure.monitor.opentelemetry._configure.iter_entry_points")
    def test_extra_exporters(self, iter_mock):
        ep_mock1 = Mock()
        ep_mock1.name = "custom_exporter1"
        exp_mock1 = Mock()
        ep_mock1.load.return_value = exp_mock1
        ep_mock_azmon = Mock()
        ep_mock_azmon.name = "azure_monitor_opentelemetry_exporter"
        exp_mock_azmon = Mock()
        ep_mock_azmon.load.return_value = exp_mock_azmon
        ep_mock2 = Mock()
        ep_mock2.name = "custom_exporter2"
        exp_mock2 = Mock()
        ep_mock2.load.return_value = exp_mock2
        iter_mock.return_value = (ep_mock_azmon, ep_mock2, ep_mock1)
        exporter_entry_point_group = "exporter_entry_point_group"
        self.assertEquals(
            _get_extra_exporters(
                exporter_entry_point_group, "EXPORTER_ENV_VAR"
            ),
            [exp_mock2(), exp_mock1()],
        )
