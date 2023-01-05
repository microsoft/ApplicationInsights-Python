# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from typing import Any, Dict


def get_configurations(**kwargs) -> Dict[str, Any]:
    configurations = {}

    # In-code configurations take priority
    configurations["connection_string"] = kwargs.get("connection_string")
    configurations["disable_tracing"] = kwargs.get("disable_tracing")
    configurations["service_name"] = kwargs.get("service_name", "")
    configurations["service_namespace"] = kwargs.get("service_namespace", "")
    configurations["service_instance_id"] = kwargs.get("service_instance_id", "")
    configurations["service_version"] = kwargs.get("service_version", "")

    # TODO: Support addtional env vars configurations
    # if configurations.get("disable_tracing") is None:
    #     configurations["disable_tracing"] = False

    return configurations
