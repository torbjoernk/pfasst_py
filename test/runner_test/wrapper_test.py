# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import sys
import unittest

from pfasst_py.runner.wrapper import Wrapper
from pfasst_py.runner.executable import Executable


class WrapperTest(unittest.TestCase):
    def setUp(self):
        self.obj = Wrapper()

    def test_is_executable(self):
        self.assertIsInstance(self.obj, Executable)

    def test_takes_executable_as_wrapper(self):
        self.obj.wrapped = Executable(exe=sys.executable)
        self.assertTrue(self.obj.wrapped.exe.samefile(sys.executable))

        self.obj = Wrapper(wrapped=Executable(exe=sys.executable))
        self.assertTrue(self.obj.wrapped.exe.samefile(sys.executable))

    def test_denies_non_executables_as_wrapped(self):
        with self.assertRaises(ValueError):
            self.obj.wrapped = 'not an Executable'

    def test_does_not_require_wrapped_executable(self):
        self.obj.exe = sys.executable
        with self.assertLogs('pfasst_py', level='WARNING') as cptr:
            self.assertEqual(self.obj.build_cmd_line(), sys.executable)
        self.assertRegex(''.join(cptr.output), 'No wrapped executable defined')

    def test_takes_commandline_from_wrapped(self):
        self.obj.exe = sys.executable
        self.obj.wrapped = Executable(exe=sys.executable)
        self.assertEqual(self.obj.build_cmd_line(), "%s %s" % (sys.executable, sys.executable))
