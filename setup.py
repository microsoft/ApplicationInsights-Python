# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

import os

import setuptools

BASE_DIR = os.path.dirname(__file__)
VERSION_FILENAME = os.path.join(
    BASE_DIR, "src", "azure", "monitor", "opentelemetry", "distro", "version.py"
)
PACKAGE_INFO = {}
with open(VERSION_FILENAME, encoding="utf-8") as f:
    exec(f.read(), PACKAGE_INFO)

setuptools.setup(
    version=PACKAGE_INFO["__version__"],
)
