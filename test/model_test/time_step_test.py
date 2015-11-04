# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import unittest

from pfasst_py.model.time_step import TimeStep
from pfasst_py.model.iteration import Iteration


class TimeStepTest(unittest.TestCase):
    def setUp(self):
        self.obj = TimeStep()

    def test_has_prop_time_step_index(self):
        self.assertIsNone(self.obj.index)
        self.obj.index = 1
        self.assertEqual(self.obj.index, 1)
    
    def test_prop_index_must_be_zero_positive(self):
        with self.assertRaises(ValueError):
            self.obj.index = -1

    def test_prop_index_from_string(self):
        self.obj.index = '2'
        self.assertEqual(self.obj.index, 2)

    def test_prop_index_invalid_types(self):
        with self.assertRaises(ValueError):
            self.obj.index = ['not']

    def test_has_prop_total_steps(self):
        self.assertIsNone(self.obj.total_steps)
        self.obj.total_steps = 1
        self.assertEqual(self.obj.total_steps, 1)

    def test_prop_total_steps_must_be_zero_positive(self):
        with self.assertRaises(ValueError):
            self.obj.total_steps = -1

    def test_prop_total_steps_from_string(self):
        self.obj.total_steps = '2'
        self.assertEqual(self.obj.total_steps, 2)

    def test_prop_total_steps_invalid_types(self):
        with self.assertRaises(ValueError):
            self.obj.total_steps = ['not']

    def test_has_prop_iterations(self):
        self.assertListEqual(self.obj.iterations, [])

        self.obj.iterations.append(Iteration())
        self.obj.iterations.append(Iteration())
        self.assertEqual(len(self.obj.iterations), 2)

    def test_prop_iterations_asserts_iteration_types(self):
        self.obj.iterations.append(Iteration())
        self.obj.iterations.append('not')
        with self.assertRaises(RuntimeError):
            _ = self.obj.iterations
