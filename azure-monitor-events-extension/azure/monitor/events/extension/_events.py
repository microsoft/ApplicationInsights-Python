# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from logging import INFO, LogRecord, getLogger
from typing import Dict, Optional

from opentelemetry.sdk._logs import LoggingHandler
from opentelemetry.util.types import Attributes

_APPLICATION_INSIGHTS_EVENT_MARKER_ATTRIBUTE = (
    "APPLICATION_INSIGHTS_EVENT_MARKER_ATTRIBUTE"
)
_event_logger = getLogger(__name__)
_event_logger.propagate = False


class _AzureMonitorOpenTelemetryEventHandler(LoggingHandler):
    @staticmethod
    def _get_attributes(record: LogRecord) -> Attributes:
        attributes = LoggingHandler._get_attributes(record)
        attributes[_APPLICATION_INSIGHTS_EVENT_MARKER_ATTRIBUTE] = True
        return attributes


class _AzureMonitorEventsExtension:
    _initialized = False

    def _initialize():
        if not _AzureMonitorEventsExtension._initialized:
            _event_logger.addHandler(_AzureMonitorOpenTelemetryEventHandler())
            _event_logger.setLevel(INFO)
            _AzureMonitorEventsExtension._initialized = True


def track_event(name: str, custom_dimensions: Optional[Dict[str, str]] = None):
    _AzureMonitorEventsExtension._initialize()
    _event_logger.info(name, extra=custom_dimensions)
