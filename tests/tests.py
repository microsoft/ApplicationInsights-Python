import unittest

try:
    from test.support import run_unittest
except ImportError:
    from test.test_support import run_unittest

import applicationinsights_tests

def test_main():
    run_unittest(
            applicationinsights_tests.TestTelemetryClient.TestTelemetryClient,
            applicationinsights_tests.channel_tests.TestAsynchronousQueue.TestAsynchronousQueue,
            applicationinsights_tests.channel_tests.TestAsynchronousSender.TestAsynchronousSender,
            applicationinsights_tests.channel_tests.TestQueueBase.TestQueueBase,
            applicationinsights_tests.channel_tests.TestSenderBase.TestSenderBase,
            applicationinsights_tests.channel_tests.TestSynchronousQueue.TestSynchronousQueue,
            applicationinsights_tests.channel_tests.TestSynchronousSender.TestSynchronousSender,
            applicationinsights_tests.channel_tests.TestTelemetryChannel.TestTelemetryChannel,
            applicationinsights_tests.channel_tests.TestTelemetryContext.TestTelemetryContext,
            applicationinsights_tests.channel_tests.contracts_tests.TestApplication,
            applicationinsights_tests.channel_tests.contracts_tests.TestData,
            applicationinsights_tests.channel_tests.contracts_tests.TestDataPoint,
            applicationinsights_tests.channel_tests.contracts_tests.TestDevice,
            applicationinsights_tests.channel_tests.contracts_tests.TestEnvelope,
            applicationinsights_tests.channel_tests.contracts_tests.TestEventData,
            applicationinsights_tests.channel_tests.contracts_tests.TestExceptionData,
            applicationinsights_tests.channel_tests.contracts_tests.TestExceptionDetails,
            applicationinsights_tests.channel_tests.contracts_tests.TestInternal,
            applicationinsights_tests.channel_tests.contracts_tests.TestLocation,
            applicationinsights_tests.channel_tests.contracts_tests.TestMessageData,
            applicationinsights_tests.channel_tests.contracts_tests.TestMetricData,
            applicationinsights_tests.channel_tests.contracts_tests.TestOperation,
            applicationinsights_tests.channel_tests.contracts_tests.TestPageViewData,
            applicationinsights_tests.channel_tests.contracts_tests.TestRemoteDependencyData,
            applicationinsights_tests.channel_tests.contracts_tests.TestRequestData,
            applicationinsights_tests.channel_tests.contracts_tests.TestSession,
            applicationinsights_tests.channel_tests.contracts_tests.TestStackFrame,
            applicationinsights_tests.channel_tests.contracts_tests.TestUser,
            applicationinsights_tests.logging_tests.TestApplicationInsightsHandler.TestApplicationInsightsHandler)

if __name__ == '__main__':
    test_main()