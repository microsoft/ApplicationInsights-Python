# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# -------------------------------------------------------------------------

from azure.monitor.events.extension._events import track_event

from ._version import VERSION

__all__ = [
    "track_event",
]
__version__ = VERSION
