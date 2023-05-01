# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from logging import NOTSET, getLogger
from os import environ
from typing import Dict

from azure.monitor.opentelemetry._constants import (
    DISABLE_LOGGING_ARG,
    DISABLE_METRICS_ARG,
    DISABLE_TRACING_ARG,
    EXCLUDE_INSTRUMENTATIONS_ARG,
    INSTRUMENTATION_CONFIG_ARG,
    LOGGER_NAME_ARG,
    LOGGING_EXPORT_INTERVAL_MS_ARG,
    LOGGING_LEVEL_ARG,
    METRIC_READERS_ARG,
    SAMPLING_RATIO_ARG,
    TRACING_EXPORT_INTERVAL_MS_ARG,
    VIEWS_ARG,
)
from azure.monitor.opentelemetry._types import ConfigurationValue
from opentelemetry.sdk.environment_variables import OTEL_TRACES_SAMPLER_ARG
from opentelemetry.environment_variables import OTEL_LOGS_EXPORTER, OTEL_METRICS_EXPORTER, OTEL_TRACES_EXPORTER

_INVALID_FLOAT_MESSAGE = "Value of %s must be a float. Defaulting to %s: %s"


# Speced out but unused by OTel SDK as of 1.15.0
LOGGING_EXPORT_INTERVAL_MS_ENV_VAR = "OTEL_BLRP_SCHEDULE_DELAY"
# TODO: remove when sampler uses env var instead
SAMPLING_RATIO_ENV_VAR = OTEL_TRACES_SAMPLER_ARG


_logger = getLogger(__name__)


def _get_configurations(**kwargs) -> Dict[str, ConfigurationValue]:
    configurations = {}

    for key, val in kwargs.items():
        configurations[key] = val

    _default_exclude_instrumentations(configurations)
    _default_disable_logging(configurations)
    _default_disable_metrics(configurations)
    _default_disable_tracing(configurations)
    _default_logging_level(configurations)
    _default_logger_name(configurations)
    _default_logging_export_interval_ms(configurations)
    _default_metric_readers(configurations)
    _default_views(configurations)
    _default_sampling_ratio(configurations)
    _default_tracing_export_interval_ms(configurations)
    _default_instrumentation_config(configurations)

    # TODO: remove when validation added to BLRP
    if configurations[LOGGING_EXPORT_INTERVAL_MS_ARG] <= 0:
        raise ValueError(
            "%s must be positive." % LOGGING_EXPORT_INTERVAL_MS_ARG
        )

    return configurations


def _default_exclude_instrumentations(configurations):
    if EXCLUDE_INSTRUMENTATIONS_ARG not in configurations:
        configurations[EXCLUDE_INSTRUMENTATIONS_ARG] = []


def _default_disable_logging(configurations):
    if DISABLE_LOGGING_ARG not in configurations:
        default = False
        if OTEL_LOGS_EXPORTER in environ:
            if environ[OTEL_LOGS_EXPORTER].lower().strip() == "none":
                default = True
        configurations[DISABLE_LOGGING_ARG] = default


def _default_disable_metrics(configurations):
    if DISABLE_METRICS_ARG not in configurations:
        default = False
        if OTEL_METRICS_EXPORTER in environ:
            if environ[OTEL_METRICS_EXPORTER].lower().strip() == "none":
                default = True
        configurations[DISABLE_METRICS_ARG] = default


def _default_disable_tracing(configurations):
    if DISABLE_TRACING_ARG not in configurations:
        default = False
        if OTEL_TRACES_EXPORTER in environ:
            if environ[OTEL_TRACES_EXPORTER].lower().strip() == "none":
                default = True
        configurations[DISABLE_TRACING_ARG] = default


def _default_logging_level(configurations):
    if LOGGING_LEVEL_ARG not in configurations:
        configurations[LOGGING_LEVEL_ARG] = NOTSET


def _default_logger_name(configurations):
    if LOGGER_NAME_ARG not in configurations:
        configurations[LOGGER_NAME_ARG] = ""


def _default_logging_export_interval_ms(configurations):
    if LOGGING_EXPORT_INTERVAL_MS_ARG not in configurations:
        configurations[LOGGING_EXPORT_INTERVAL_MS_ARG] = 5000


def _default_metric_readers(configurations):
    if METRIC_READERS_ARG not in configurations:
        configurations[METRIC_READERS_ARG] = []


def _default_views(configurations):
    if VIEWS_ARG not in configurations:
        configurations[VIEWS_ARG] = ()


# TODO: remove when sampler uses env var instead
def _default_sampling_ratio(configurations):
    if SAMPLING_RATIO_ARG not in configurations:
        default = 1.0
        if SAMPLING_RATIO_ENV_VAR in environ:
            try:
                default = float(environ[SAMPLING_RATIO_ENV_VAR])
            except ValueError as e:
                _logger.error(
                    _INVALID_FLOAT_MESSAGE
                    % (SAMPLING_RATIO_ENV_VAR, default, e)
                )
        configurations[SAMPLING_RATIO_ARG] = default


def _default_tracing_export_interval_ms(configurations):
    if TRACING_EXPORT_INTERVAL_MS_ARG not in configurations:
        configurations[TRACING_EXPORT_INTERVAL_MS_ARG] = None


def _default_instrumentation_config(configurations):
    if INSTRUMENTATION_CONFIG_ARG not in configurations:
        configurations[INSTRUMENTATION_CONFIG_ARG] = {}
