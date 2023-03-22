# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from json import loads
from logging import NOTSET
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
from opentelemetry.sdk.environment_variables import (
    OTEL_LOG_LEVEL,
    OTEL_TRACES_SAMPLER_ARG,
)

_CONFIGURATION_ENV_VAR_PREFIX = "APPLICATIONINSIGHTS_"


def _get_env_var_name(arg):
    return _CONFIGURATION_ENV_VAR_PREFIX + arg.upper()


EXCLUDE_INSTRUMENTATIONS_ENV_VAR = _get_env_var_name(
    EXCLUDE_INSTRUMENTATIONS_ARG
)
DISABLE_LOGGING_ENV_VAR = _get_env_var_name(DISABLE_LOGGING_ARG)
DISABLE_METRICS_ENV_VAR = _get_env_var_name(DISABLE_METRICS_ARG)
DISABLE_TRACING_ENV_VAR = _get_env_var_name(DISABLE_TRACING_ARG)
# Speced out but unused by OTel SDK as of 1.15.0
LOGGING_LEVEL_ENV_VAR = OTEL_LOG_LEVEL
LOGGER_NAME_ENV_VAR = _get_env_var_name(LOGGER_NAME_ARG)
# Speced out but unused by OTel SDK as of 1.15.0
LOGGING_EXPORT_INTERVAL_MS_ENV_VAR = "OTEL_BLRP_SCHEDULE_DELAY"
# TODO: leave as private until env var configuration logic is designed
_METRIC_READERS_ENV_VAR = _get_env_var_name(METRIC_READERS_ARG)
_VIEWS_ENV_VAR = _get_env_var_name(VIEWS_ARG)
# TODO: remove when sampler uses env var instead
SAMPLING_RATIO_ENV_VAR = OTEL_TRACES_SAMPLER_ARG
INSTRUMENTATION_CONFIG_ENV_VAR = _get_env_var_name(INSTRUMENTATION_CONFIG_ARG)


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
        default = []
        if EXCLUDE_INSTRUMENTATIONS_ENV_VAR in environ:
            default = loads(environ[EXCLUDE_INSTRUMENTATIONS_ENV_VAR])
        configurations[EXCLUDE_INSTRUMENTATIONS_ARG] = default


def _default_disable_logging(configurations):
    if DISABLE_LOGGING_ARG not in configurations:
        default = False
        if DISABLE_LOGGING_ENV_VAR in environ:
            default = bool(environ[DISABLE_LOGGING_ENV_VAR])
        configurations[DISABLE_LOGGING_ARG] = default


def _default_disable_metrics(configurations):
    if DISABLE_METRICS_ARG not in configurations:
        default = False
        if DISABLE_METRICS_ENV_VAR in environ:
            default = bool(environ[DISABLE_METRICS_ENV_VAR])
        configurations[DISABLE_METRICS_ARG] = default


def _default_disable_tracing(configurations):
    if DISABLE_TRACING_ARG not in configurations:
        default = False
        if DISABLE_TRACING_ENV_VAR in environ:
            default = bool(environ[DISABLE_TRACING_ENV_VAR])
        configurations[DISABLE_TRACING_ARG] = default


def _default_logging_level(configurations):
    if LOGGING_LEVEL_ARG not in configurations:
        default = NOTSET
        if LOGGING_LEVEL_ENV_VAR in environ:
            default = int(environ[LOGGING_LEVEL_ENV_VAR])
            # TODO: Match OTel env var usage when it is determined.
        configurations[LOGGING_LEVEL_ARG] = default


def _default_logger_name(configurations):
    if LOGGER_NAME_ARG not in configurations:
        default = ""
        if LOGGER_NAME_ENV_VAR in environ:
            default = environ[LOGGER_NAME_ENV_VAR]
        configurations[LOGGER_NAME_ARG] = default


def _default_logging_export_interval_ms(configurations):
    if LOGGING_EXPORT_INTERVAL_MS_ARG not in configurations:
        default = 5000
        if LOGGING_EXPORT_INTERVAL_MS_ENV_VAR in environ:
            default = int(environ[LOGGING_EXPORT_INTERVAL_MS_ENV_VAR])
        configurations[LOGGING_EXPORT_INTERVAL_MS_ARG] = default


# TODO: Design metric readers env var usage
def _default_metric_readers(configurations):
    if METRIC_READERS_ARG not in configurations:
        default = []
        if _METRIC_READERS_ENV_VAR in environ:
            default = loads(environ[_METRIC_READERS_ENV_VAR])
        configurations[METRIC_READERS_ARG] = default


# TODO: Design views env var usage
def _default_views(configurations):
    if VIEWS_ARG not in configurations:
        # TODO tuple or list
        default = []
        if _VIEWS_ENV_VAR in environ:
            default = loads(environ[_VIEWS_ENV_VAR])
        configurations[VIEWS_ARG] = default


# TODO: remove when sampler uses env var instead
def _default_sampling_ratio(configurations):
    if SAMPLING_RATIO_ARG not in configurations:
        default = 1.0
        if SAMPLING_RATIO_ENV_VAR in environ:
            default = float(environ[SAMPLING_RATIO_ENV_VAR])
        configurations[SAMPLING_RATIO_ARG] = default


def _default_tracing_export_interval_ms(configurations):
    if TRACING_EXPORT_INTERVAL_MS_ARG not in configurations:
        configurations[TRACING_EXPORT_INTERVAL_MS_ARG] = None


def _default_instrumentation_config(configurations):
    if INSTRUMENTATION_CONFIG_ARG not in configurations:
        default = {}
        if INSTRUMENTATION_CONFIG_ENV_VAR in environ:
            default = loads(environ[INSTRUMENTATION_CONFIG_ENV_VAR])
        configurations[INSTRUMENTATION_CONFIG_ARG] = default
