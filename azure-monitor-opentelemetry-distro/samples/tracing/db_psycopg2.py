# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------
import psycopg2
from azure.monitor.opentelemetry.distro import configure_azure_monitor

# Configure Azure monitor collection telemetry pipeline
configure_azure_monitor(
    connection_string="<your-connection-string>",
    service_name="psycopg2_service_name",
    instrumentations=["psycopg2"],
    tracing_export_interval_millis=15000,
    disable_logging=True,
)

cnx = psycopg2.connect(database="test", user="<user>", password="<password>")
cursor = cnx.cursor()
cursor.execute("INSERT INTO test_tables (test_field) VALUES (123)")
cursor.close()
cnx.close()
