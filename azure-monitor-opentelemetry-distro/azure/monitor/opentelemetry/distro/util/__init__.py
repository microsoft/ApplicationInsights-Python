# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------
from os import environ
from typing import Any, Dict

def get_configurations(is_auto_instrumentation, **kwargs) -> Dict[str, Any]:
    configurations = {}

    # In-code configurations take priority
    if not is_auto_instrumentation:
        configurations["connection_string"] = kwargs.get("connection_string")
        configurations["disable_tracing"] = kwargs.get("disable_tracing")
        configurations["service_name"] = kwargs.get("service_name")
        configurations["service_namespace"] = kwargs.get("service_namespace")
        configurations["service_instance_id"] = kwargs.get("service_instance_id")
        configurations["service_version"] = kwargs.get("service_version")

    if configurations.get("connection_string") is None:
        configurations["connection_string"] = environ.get("connection_string")
    if configurations.get("disable_tracing") is None:
        # TODO: Env var config for disabling telemetry
        configurations["disable_tracing"] = False
    # TODO: Support addtional env vars configurations

    return configurations
