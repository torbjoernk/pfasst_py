# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import sys
import unittest

from pfasst_py.runner.runner import Runner
from pfasst_py.runner.executable import Executable


class RunnerTest(unittest.TestCase):
    def setUp(self):
        self.obj = Runner()

    def test_takes_executable(self):
        self.obj.exe = Executable()
        self.assertIsInstance(self.obj.exe, Executable)

    def test_ensures_type_of_executable(self):
        with self.assertRaises(ValueError):
            self.obj.exe = 'not an Executable'

    def test_runs_with_arbitrary_arguments(self):
        self.obj.exe = Executable(exe=sys.executable)
        with self.assertLogs('pfasst_py') as cptr:
            output = self.obj.run(['-c "import sys; print(sys.version_info)"'])
        self.assertRegex(' '.join(cptr.output), 'Executing')
        self.assertRegex(' '.join(cptr.output), 'Finished')

    def test_returns_list_of_stdout_lines(self):
        self.obj.exe = Executable(exe=sys.executable)
        output = self.obj.run(['-c "import sys; print(sys.version_info)"'])
        self.assertEqual(output, [str(sys.version_info)])

    def test_checks_return_status(self):
        self.obj.exe = Executable(exe='exit')
        with self.assertRaises(RuntimeError):
            self.obj.run('1')

    def test_checks_stderr(self):
        self.obj.exe = Executable(exe='echo')
        with self.assertLogs('pfasst_py', level='WARNING') as cptr:
            self.obj.run('"Hello" >&2')
        self.assertRegex(''.join(cptr.output), 'Process put something on stderr:')
