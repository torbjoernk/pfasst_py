"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import os
import unittest

from pfasst_py.examples.example import Example
from pfasst_py.runner.runner import Runner
from pfasst_py.runner.executable import Executable


class ExampleTest(unittest.TestCase):
    def setUp(self):
        self.obj = Example()

    def test_has_prop_directory(self):
        self.assertIsNone(self.obj.directory)

    def test_takes_valid_directories(self):
        self.obj.directory = os.getcwd()
        self.assertTrue(self.obj.directory.samefile(os.getcwd()))

        self.obj.directory = '.'
        self.assertTrue(self.obj.directory.samefile(os.getcwd()))

    def test_ensures_existence_of_directory(self):
        with self.assertRaises(ValueError):
            self.obj.directory = '/not/a/dir'

    def test_takes_directory_on_creation(self):
        obj = Example(directory=os.getcwd())
        self.assertTrue(obj.directory.samefile(os.getcwd()))

    def test_has_prop_rundir(self):
        self.assertIsNone(self.obj.rundir)

    def test_takes_valid_directories_as_rundir(self):
        self.obj.rundir = os.getcwd()
        self.assertTrue(self.obj.rundir.samefile(os.getcwd()))

        self.obj.rundir = '.'
        self.assertTrue(self.obj.rundir.samefile(os.getcwd()))

    def test_ensures_existence_of_rundir_directory(self):
        with self.assertRaises(ValueError):
            self.obj.rundir = '/not/a/dir'

    def test_takes_rundir_directory_on_creation(self):
        obj = Example(rundir=os.getcwd())
        self.assertTrue(obj.rundir.samefile(os.getcwd()))

    def test_has_runner(self):
        self.assertIsNone(self.obj.runner)

    def test_takes_runner(self):
        self.obj.runner = Runner()
        self.assertIsInstance(self.obj.runner, Runner)

    def test_denies_non_runners(self):
        with self.assertRaises(ValueError):
            self.obj.runner = 'not a runner'

    def test_runs_with_runner(self):
        self.obj.runner = Runner()
        self.obj.runner.exe = Executable(exe='echo')
        self.obj.run("Hello")

    def test_cannot_run_without_runner(self):
        with self.assertRaises(RuntimeError):
            self.obj.run()
