"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import os
import unittest

from pfasst_py.examples.example import Example
from pfasst_py.runner.runner import Runner
from pfasst_py.runner.parameters import GlobalParamsMixin


class ExampleTest(unittest.TestCase):
    def setUp(self):
        self.obj = Example()

    def test_example_is_runner(self):
        self.assertTrue(issubclass(Example, Runner))

    def test_example_has_global_parameters(self):
        self.assertTrue(issubclass(Example, GlobalParamsMixin))

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
