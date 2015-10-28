# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import sys
import unittest

from pfasst_py.runner.runner import Runner
from pfasst_py.util.parameter import ValueParameter


class RunnerTest(unittest.TestCase):
    def setUp(self):
        self.obj = Runner(sys.executable)

    def test_takes_executable(self):
        self.assertTrue(self.obj.exe.samefile(sys.executable))

    def test_ensures_presents_of_executable(self):
        with self.assertRaises(ValueError):
            Runner('not/an/exe')

    def test_builds_cmd_line_without_args(self):
        self.assertEqual(self.obj.build_cmd_line(), sys.executable)

    def test_builds_cmd_line_with_arguments(self):
        self.assertEqual(self.obj.build_cmd_line(['--arg']), "%s --arg" % (sys.executable, ))

        self.assertEqual(self.obj.build_cmd_line([ValueParameter(long='long', value='value')]),
                         "%s --long value" % (sys.executable, ))

    def test_builds_cmd_requires_exe(self):
        self.obj._exe = None
        with self.assertRaises(RuntimeError):
            self.obj.build_cmd_line()

    def test_runs_with_arbitrary_arguments(self):
        with self.assertLogs('pfasst_py') as cptr:
            output = self.obj.run(['-c "import sys; print(sys.version_info)"'])
        self.assertRegex(' '.join(cptr.output), 'Executing')
        self.assertRegex(' '.join(cptr.output), 'Finished')

    def test_returns_list_of_stdout_lines(self):
        output = self.obj.run(['-c "import sys; print(sys.version_info)"'])
        self.assertEqual(output, [str(sys.version_info)])
