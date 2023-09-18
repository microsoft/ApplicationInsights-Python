# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
An example to show how to use the track_event api to send custom events to Application Insights.
"""
from azure.monitor.events.extension import track_event
from azure.monitor.opentelemetry import configure_azure_monitor

configure_azure_monitor()

# Use the track_event() api to send custom event telemetry
# Takes event name and custom dimensions
track_event("Test event", {"key1":"value1", "key2":"value2"})

input()
