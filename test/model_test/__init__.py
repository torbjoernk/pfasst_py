# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import datetime
import unittest

from pfasst_py.model.iteration import Iteration


class IterationTest(unittest.TestCase):
    def setUp(self):
        self.obj = Iteration()

    def test_has_prop_iteration_index(self):
        self.assertIsNone(self.obj.index)

        self.obj.index = 1
        self.assertEqual(self.obj.index, 1)

    def test_prop_index_must_be_zero_positive(self):
        with self.assertRaises(ValueError):
            self.obj.index = -1

    def test_prop_index_from_string(self):
        self.obj.index = '2'
        self.assertEqual(self.obj.index, 2)

    def test_has_prop_absolute_residual(self):
        self.assertIsNone(self.obj.abs_res)

        self.obj.abs_res = 0.12e-3
        self.assertEqual(self.obj.abs_res, 0.12e-3)

    def test_prop_absolute_residual_from_string(self):
        self.obj.abs_res = '0.12e-3'
        self.assertEqual(self.obj.abs_res, 0.12e-3)

    def test_prop_absolute_residual_invalid_types(self):
        with self.assertRaises(ValueError):
            self.obj.abs_res = ['not']

    def test_has_prop_relative_residual(self):
        self.assertIsNone(self.obj.rel_res)

        self.obj.rel_res = 0.12e-3
        self.assertEqual(self.obj.rel_res, 0.12e-3)

    def test_prop_relative_residual_from_string(self):
        self.obj.rel_res = '0.12e-3'
        self.assertEqual(self.obj.rel_res, 0.12e-3)

    def test_prop_relative_residual_invalid_types(self):
        with self.assertRaises(ValueError):
            self.obj.rel_res = ['not']

    def test_has_prop_timing(self):
        self.assertIsNone(self.obj.timing)
        self.obj.timing = datetime.timedelta()
        self.assertEqual(self.obj.timing, datetime.timedelta())

    def test_prop_timing_requires_timedelta(self):
        with self.assertRaises(ValueError):
            self.obj.timing = 0.2
