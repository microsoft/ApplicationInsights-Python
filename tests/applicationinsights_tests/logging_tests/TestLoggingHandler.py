import unittest
import logging as pylogging

import sys, os, os.path
rootDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
if rootDirectory not in sys.path:
    sys.path.append(rootDirectory)

from applicationinsights import logging

class TestEnable(unittest.TestCase):
    def test_enable(self):
        handler1 = logging.enable('foo')
        self.assertIsNotNone(handler1)
        self.assertEqual('LoggingHandler', handler1.__class__.__name__)
        self.assertEqual('foo', handler1.client.context.instrumentation_key)
        handler2 = logging.enable('foo')
        self.assertEqual('LoggingHandler', handler2.__class__.__name__)
        self.assertEqual('foo', handler2.client.context.instrumentation_key)
        channel = MockChannel()
        handler3 = logging.enable('bar', telemetry_channel=channel)
        self.assertIsNotNone(handler1)
        self.assertEqual('LoggingHandler', handler3.__class__.__name__)
        self.assertEqual('bar', handler3.client.context.instrumentation_key)
        self.assertEqual(channel, handler3.client.channel)
        all_handlers = pylogging.getLogger().handlers
        self.assertIn(handler2, all_handlers)
        self.assertIn(handler3, all_handlers)
        pylogging.getLogger().removeHandler(handler2)
        pylogging.getLogger().removeHandler(handler3)

    def test_enable_raises_exception_on_no_instrumentation_key(self):
        self.assertRaises(Exception, logging.enable, None)


class TestLoggingHandler(unittest.TestCase):
    def test_construct(self):
        handler = logging.LoggingHandler('test')
        self.assertIsNotNone(handler)
        self.assertEqual('test', handler.client.context.instrumentation_key)

    def test_construct_raises_exception_on_no_instrumentation_key(self):
        self.assertRaises(Exception, logging.LoggingHandler, None)

    def test_log_works_as_expected(self):
        logger, sender, channel = self._setup_logger()

        expected = [
            (logger.debug, 'debug message', 'Microsoft.ApplicationInsights.Message', 'test', 'MessageData', 0, 'simple_logger - DEBUG - debug message'),
            (logger.info, 'info message', 'Microsoft.ApplicationInsights.Message', 'test', 'MessageData', 1, 'simple_logger - INFO - info message'),
            (logger.warn, 'warn message', 'Microsoft.ApplicationInsights.Message', 'test', 'MessageData', 2, 'simple_logger - WARNING - warn message'),
            (logger.error, 'error message', 'Microsoft.ApplicationInsights.Message', 'test', 'MessageData', 3, 'simple_logger - ERROR - error message'),
            (logger.critical, 'critical message', 'Microsoft.ApplicationInsights.Message', 'test', 'MessageData', 4, 'simple_logger - CRITICAL - critical message')
        ]

        for logging_function, logging_parameter, envelope_type, ikey, data_type, severity_level, message in expected:
            logging_function(logging_parameter)
            data = sender.data[0][0]
            sender.data = []
            self.assertEqual(envelope_type, data.name)
            self.assertEqual(ikey, data.ikey)
            self.assertEqual(data_type, data.data.base_type)
            self.assertEqual(message, data.data.base_data.message)
            self.assertEqual(severity_level, data.data.base_data.severity_level)
        
        channel.context.properties['foo'] = 'bar'
        channel.context.operation.id = 1001
        logger.info('info message')
        data = sender.data[0][0]
        self.assertEqual('bar', data.data.base_data.properties['foo'])
        self.assertEqual(1001, data.tags.get('ai.operation.id'))

    def test_log_exception_works_as_expected(self):
        logger, sender, _ = self._setup_logger()

        try:
            raise Exception('blah')
        except:
            logger.exception('some error')

        data = sender.data[0][0]
        self.assertEqual('Microsoft.ApplicationInsights.Exception', data.name)
        self.assertEqual('test', data.ikey)
        self.assertEqual('ExceptionData', data.data.base_type)
        self.assertEqual('blah', data.data.base_data.exceptions[0].message)

    def _setup_logger(self):
        logger = pylogging.getLogger('simple_logger')
        logger.setLevel(pylogging.DEBUG)

        handler = logging.LoggingHandler('test')
        handler.setLevel(pylogging.DEBUG)

        channel = handler.client.channel

        # mock out the sender
        sender = MockSynchronousSender()
        queue = channel.queue
        queue.max_queue_length = 1
        queue._sender = sender
        sender.queue = queue

        formatter = pylogging.Formatter('%(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger, sender, channel


class MockChannel:
    def flush(self):
        pass


class MockSynchronousSender:
    def __init__(self):
        self.send_buffer_size = 1
        self.data = []
        self.queue = None

    def send(self, data_to_send):
        self.data.append(data_to_send)
