# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

from typing import Any, Dict


def get_configurations(**kwargs) -> Dict[str, Any]:
    configurations = {}

    for key, val in kwargs.items():
        configurations[key] = val

    return configurations

# TODO: Add env var configuration
