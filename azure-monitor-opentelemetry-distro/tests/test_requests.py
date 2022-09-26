import unittest

from opentelemetry.instrumentation.requests import RequestsInstrumentor


class TestRequestsInstrumentation(unittest.TestCase):
    def test_instrument(self):
        try:
            RequestsInstrumentor().instrument()
        except Exception as ex:  # pylint: disable=broad-except
            print(ex)
            self.fail(
                f"Unexpected exception raised when instrumenting {RequestsInstrumentor.__name__}"
            )

