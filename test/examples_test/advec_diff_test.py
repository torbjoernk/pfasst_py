# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import unittest

from pfasst_py.examples.advec_diff.advec_diff import AdvecDiffExecutable, AdvecDiffParamsMixin
from pfasst_py.runner.executable import Executable
from pfasst_py.runner.parameters import ParamsMixin
from pfasst_py.util.parameter import ValueParameter


class AdvecDiffParamsMixinTest(unittest.TestCase):
    def setUp(self):
        self.obj = AdvecDiffParamsMixin()

    def test_is_params_mixin(self):
        self.assertIsInstance(self.obj, ParamsMixin)

    def test_has_prop_nu(self):
        self.assertIsInstance(self.obj.nu, ValueParameter)

    def test_has_prop_vel(self):
        self.assertIsInstance(self.obj.vel, ValueParameter)


class AdvecDiffExecutableTest(unittest.TestCase):
    def setUp(self):
        self.obj = AdvecDiffExecutable()

    def test_is_executable(self):
        self.assertIsInstance(self.obj, Executable)
