import unittest

try:
    from test.support import run_unittest
except ImportError:
    from test.test_support import run_unittest

import applicationinsights_tests

def test_main():
    run_unittest(
            applicationinsights_tests.TestTelemetryClient.TestTelemetryClient,
            applicationinsights_tests.channel_tests.TestTelemetryChannel.TestTelemetryChannel,
            applicationinsights_tests.channel_tests.TestTelemetryContext.TestTelemetryContext,
            applicationinsights_tests.channel_tests.TestTelemetrySender.TestTelemetrySender,
            applicationinsights_tests.channel_tests.contracts_tests.TestApplicationContext,
            applicationinsights_tests.channel_tests.contracts_tests.TestDeviceContext,
            applicationinsights_tests.channel_tests.contracts_tests.TestEventTelemetry,
            applicationinsights_tests.channel_tests.contracts_tests.TestExceptionTelemetry,
            applicationinsights_tests.channel_tests.contracts_tests.TestExceptionTelemetryDetails,
            applicationinsights_tests.channel_tests.contracts_tests.TestExceptionTelemetryStackFrame,
            applicationinsights_tests.channel_tests.contracts_tests.TestLocationContext,
            applicationinsights_tests.channel_tests.contracts_tests.TestMessageTelemetry,
            applicationinsights_tests.channel_tests.contracts_tests.TestMetricTelemetry,
            applicationinsights_tests.channel_tests.contracts_tests.TestMetricTelemetryDataPoint,
            applicationinsights_tests.channel_tests.contracts_tests.TestOperationContext,
            applicationinsights_tests.channel_tests.contracts_tests.TestPageViewTelemetry,
            applicationinsights_tests.channel_tests.contracts_tests.TestPageViewTelemetryPerf,
            applicationinsights_tests.channel_tests.contracts_tests.TestRemoteDependencyTelemetry,
            applicationinsights_tests.channel_tests.contracts_tests.TestRequestTelemetry,
            applicationinsights_tests.channel_tests.contracts_tests.TestSessionContext,
            applicationinsights_tests.channel_tests.contracts_tests.TestTelemetryEnvelope,
            applicationinsights_tests.channel_tests.contracts_tests.TestTelemetryEnvelopeData,
            applicationinsights_tests.channel_tests.contracts_tests.TestUserContext)

if __name__ == '__main__':
    test_main()