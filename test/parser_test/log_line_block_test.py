# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import unittest

from pfasst_py.parser.log_line_block import LogLineBlock
from pfasst_py.parser.log_line import LogLine


TIME_STEP_START_LINE = LogLine('22:10:08,03 [SDC       , INFO ] Time Step 1 of 2')
ITERMEDIATE_LINE = LogLine('22:10:08,03 [SDC       , INFO ] SDC Prediction step')
ITER_START_LINE = LogLine('22:10:08,03 [SDC       , INFO ] Iteration 1')
DEBUG_LINE = LogLine('22:10:08,03 [SWEEPER   , DEBUG ] some debug message')


class LogLineBlockTest(unittest.TestCase):
    def setUp(self):
        self.obj = LogLineBlock()

    def test_can_take_initial_list_of_lines(self):
        obj = LogLineBlock([TIME_STEP_START_LINE])
        self.assertEqual(len(obj.lines), 1)

    def test_can_append_new_lines(self):
        self.assertEqual(len(self.obj.lines), 0)
        self.obj.append_line(TIME_STEP_START_LINE)
        self.assertEqual(len(self.obj.lines), 1)

    def test_denies_non_log_lines(self):
        with self.assertRaises(ValueError):
            self.obj.append_line('not a log line')

    def test_has_prop_lines(self):
        self.assertIsInstance(self.obj.lines, list)
