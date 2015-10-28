# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import unittest

from pfasst_py.runner.mpi_runner import MPIRunner
from pfasst_py.runner.wrapper_mixin import WrapperMixin


class MPIRunnerTest(unittest.TestCase):
    def setUp(self):
        self.obj = MPIRunner()

    def test_is_wrapper_mixin(self):
        self.assertTrue(issubclass(MPIRunner, WrapperMixin))

    def test_has_num_procs(self):
        self.assertIsNone(self.obj.np)
        self.obj.np = 3
        self.assertEqual(self.obj.np, 3)

    def test_validates_setting_of_num_procs(self):
        with self.assertRaises(ValueError):
            self.obj.np = 0
        with self.assertRaises(ValueError):
            self.obj.np = ''

    def test_build_cmd_line(self):
        self.obj.wrapper = 'python'
