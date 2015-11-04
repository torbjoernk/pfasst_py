# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import datetime
import unittest

from pfasst_py.parser.log_components import LogComponent, TimestampComponent, LoggerComponent, LevelComponent, \
    RankComponent, MessageComponent


class LogComponentTest(unittest.TestCase):
    def test_has_regex(self):
        self.assertIsInstance(LogComponent.REGEX, str)

    def test_has_prop_value(self):
        obj = LogComponent('raw value')
        self.assertEqual(obj.value, 'raw value')


class TimestampComponentTest(unittest.TestCase):
    def setUp(self):
        self.raw = '04.11.2015 13:51:15,37'

    def test_is_log_component(self):
        self.assertTrue(issubclass(TimestampComponent, LogComponent))

    def test_parses_timestamp_string(self):
        obj = TimestampComponent(self.raw)
        self.assertIsInstance(obj.value, datetime.datetime)

    def test_fails_on_wrongly_formatted_timestamp(self):
        with self.assertRaises(ValueError):
            TimestampComponent('not a timestamp')


class LoggerComponentTest(unittest.TestCase):
    def setUp(self):
        self.raw = 'PFASST'

    def test_is_log_component(self):
        self.assertTrue(issubclass(LoggerComponent, LogComponent))


class LevelComponentTest(unittest.TestCase):
    def setUp(self):
        self.raw_normal = 'INFO'
        self.raw_verbose = 'VERB1'

    def test_is_log_component(self):
        self.assertTrue(issubclass(LevelComponent, LogComponent))


class RankComponentTest(unittest.TestCase):
    def setUp(self):
        self.raw_mpi = 'MPI    2'
        self.raw_no_mpi = ''

    def test_is_log_component(self):
        self.assertTrue(issubclass(RankComponent, LogComponent))
