# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import sys
import unittest

from pfasst_py.runner.executable import Executable
from pfasst_py.util.parameter import ValueParameter


class ExecutableTest(unittest.TestCase):
    def setUp(self):
        self.obj = Executable()

    def test_denies_non_executables(self):
        with self.assertRaises(ValueError):
            self.obj.exe = 'not_an_exe'

    def test_takes_executable(self):
        self.obj = Executable(exe=sys.executable)
        self.obj.exe.samefile(sys.executable)

    def test_builds_commandline(self):
        self.obj.exe = sys.executable
        self.assertEqual(self.obj.build_cmd_line(), sys.executable)

    def test_builds_commandline_with_additional_args(self):
        self.obj.exe = sys.executable
        self.assertEqual(self.obj.build_cmd_line(additional_args='args'),
                         "%s args" % sys.executable)
        self.assertEqual(self.obj.build_cmd_line(additional_args=['some', 'args']),
                         "%s some args" % sys.executable)

    def test_builds_commandline_with_stored_params(self):
        self.obj._params.update({
            'arg': ValueParameter(long='arg', value=3)
        })
        self.obj.exe = sys.executable
        self.assertEqual(self.obj.build_cmd_line(),
                         "%s --arg 3" % sys.executable)

    def test_requires_exe_for_building_commandline(self):
        with self.assertRaises(RuntimeError):
            self.obj.build_cmd_line()
