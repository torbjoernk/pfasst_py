# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import os
import pathlib
import sys
import unittest

from pfasst_py.util.fileutils import get_exe_path, get_directory_path


class GetExePathTest(unittest.TestCase):
    def test_takes_absolute_path(self):
        p = get_exe_path(os.path.abspath(sys.executable))
        self.assertTrue(p.is_absolute())

    def test_takes_relative_and_returns_absolute(self):
        p = get_exe_path(os.path.relpath(sys.executable))
        self.assertTrue(p.is_absolute())

    def test_can_lookup_via_PATH(self):
        p = get_exe_path(pathlib.Path(sys.executable).name)
        self.assertTrue(p.is_absolute())

    def test_fails_for_non_existent_absolute_path(self):
        with self.assertRaises(ValueError):
            get_exe_path('/not/an/existent/absolute/path')


class GetDirectoryPathTest(unittest.TestCase):
    def test_takes_absolute_paths(self):
        self.assertTrue(get_directory_path(os.getcwd()).samefile(os.getcwd()))

    def test_converts_relative_paths(self):
        self.assertTrue(get_directory_path('.').samefile(os.getcwd()))

    def test_existence_of_directory(self):
        with self.assertRaises(ValueError):
            get_directory_path('/not/a/dir')

    def test_type_of_directory(self):
        with self.assertRaises(ValueError):
            get_directory_path(sys.executable)
