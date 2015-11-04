# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import datetime
import unittest

from pfasst_py.parser.log_line_blocks.iterations_block import IterationLogLinesBlock
from pfasst_py.parser.log_line_blocks.log_line_block import LogLineBlock
from pfasst_py.parser.log_line import LogLine

TIME_STEP_START_LINE = LogLine('04.11.2015 22:10:08,03 [SDC       , INFO ] Time Step 1 of 2')
ITERMEDIATE_LINE = LogLine('04.11.2015 22:10:08,03 [SDC       , INFO ] SDC Prediction step')
ITER_START_LINE = LogLine('04.11.2015 08:08:09,2058 [SDC       , INFO ] Iteration 1')
ITER_CONTENT_LINE = LogLine('04.11.2015 08:08:10,7274 [SWEEPER   , INFO ]   t[3]=0.05000      |abs residual| = 4.31854e-03      |rel residual| = 2.13269e-03')
DEBUG_LINE = LogLine('04.11.2015 22:10:08,03 [SWEEPER   , DEBUG ] some debug message')


class IterationLogLinesBlockTest(unittest.TestCase):
    def setUp(self):
        self.obj = IterationLogLinesBlock()

    def test_is_log_lines_block(self):
        self.assertTrue(issubclass(IterationLogLinesBlock, LogLineBlock))

    def test_start_of_time_step_must_match_certain_criteria(self):
        with self.assertRaises(ValueError):
            self.obj.append_line(DEBUG_LINE)

    def test_accepts_start_of_time_step_only_if_empty(self):
        self.assertEqual(len(self.obj.lines), 0)

        with self.assertRaises(ValueError):
            self.obj.append_line(ITERMEDIATE_LINE)

        self.obj.append_line(ITER_START_LINE)
        self.assertEqual(len(self.obj.lines), 1)

        with self.assertRaises(ValueError):
            self.obj.append_line(ITER_START_LINE)

    def test_has_prop_iter_index(self):
        self.assertIsNone(self.obj.iteri)
        self.obj.append_line(ITER_START_LINE)
        self.assertEqual(self.obj.iteri, 1)

    def test_to_model(self):
        self.obj = IterationLogLinesBlock([ITER_START_LINE, ITER_CONTENT_LINE])
        self.assertEqual(self.obj.iteri, 1)
        model = self.obj.to_model()
        self.assertEqual(model.index, 1)
        self.assertEqual(model.timing, datetime.datetime(2015, 11, 4, 8, 8, 10, 727400) - datetime.datetime(2015, 11, 4, 8, 8, 9, 205800))
        self.assertEqual(model.abs_res, 4.31854e-3)
        self.assertEqual(model.rel_res, 2.13269e-3)
