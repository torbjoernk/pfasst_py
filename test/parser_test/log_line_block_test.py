# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import unittest

from pfasst_py.parser.log_line_block import LogLineBlock, TimeStepLogLinesBlock
from pfasst_py.parser.log_line import LogLine


class LogLineBlockTest(unittest.TestCase):
    def setUp(self):
        self.obj = LogLineBlock()

    def test_can_take_initial_list_of_lines(self):
        obj = LogLineBlock([LogLine('a log line', auto_parse=False), LogLine('a log line', auto_parse=False)])
        self.assertEqual(len(obj.lines), 2)

    def test_can_append_new_lines(self):
        self.assertEqual(len(self.obj.lines), 0)
        self.obj.append_line(LogLine('a log line', auto_parse=False))
        self.assertEqual(len(self.obj.lines), 1)

    def test_denies_non_log_lines(self):
        with self.assertRaises(ValueError):
            self.obj.append_line('not a log line')

    def test_has_prop_lines(self):
        self.assertIsInstance(self.obj.lines, list)


class TimeStepLogLinesBlockTest(unittest.TestCase):
    def setUp(self):
        self.obj = TimeStepLogLinesBlock()
        self.first_line = LogLine('22:10:08,03 [SDC       , INFO ] Time Step 1 of 1')
        self.second_line = LogLine('22:10:08,03 [SDC       , INFO ] SDC Prediction step')
        self.debug_line = LogLine('22:10:08,03 [SWEEPER   , DEBUG ] some debug message')

    def test_is_log_lines_block(self):
        self.assertTrue(issubclass(TimeStepLogLinesBlock, LogLineBlock))

    def test_accepts_start_of_time_step_only_if_empty(self):
        self.assertEqual(len(self.obj.lines), 0)

        with self.assertRaises(ValueError):
            self.obj.append_line(self.second_line)

        self.obj.append_line(self.first_line)
        self.assertEqual(len(self.obj.lines), 1)

        with self.assertRaises(ValueError):
            self.obj.append_line(self.first_line)

    def test_start_of_time_step_must_match_certain_criteria(self):
        with self.assertRaises(ValueError):
            self.obj.append_line(self.debug_line)

    def test_accepts_other_lines_only_if_non_empty(self):
        with self.assertRaises(ValueError):
            self.obj.append_line(self.second_line)

        self.obj.append_line(self.first_line)
        self.obj.append_line(self.second_line)
        self.assertEqual(len(self.obj.lines), 2)

    def test_has_prop_time_step(self):
        self.assertIsNone(self.obj.time_step)
        self.obj.append_line(self.first_line)
        self.assertEqual(self.obj.time_step, 1)

    def test_has_prop_total_steps(self):
        self.assertIsNone(self.obj.total_steps)
        self.obj.append_line(self.first_line)
        self.assertEqual(self.obj.total_steps, 1)
