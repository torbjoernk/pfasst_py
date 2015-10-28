# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import shutil
import sys
import unittest

from pfasst_py.runner.wrapper_mixin import WrapperMixin


class MPIMixinTest(unittest.TestCase):
    def setUp(self):
        self.obj = WrapperMixin()

    def test_has_wrapper_executable(self):
        self.assertIsNone(self.obj.wrapper)

    def test_setting_wrapper_takes_abs_path(self):
        self.obj.wrapper = sys.executable
        self.assertTrue(self.obj.wrapper.samefile(sys.executable))

    def test_setting_wrapper_via_PATH_lookup(self):
        self.obj.wrapper = 'python'
        self.assertTrue(self.obj.wrapper.samefile(shutil.which('python')))

    def test_setting_wrapper_fails_for_unknown(self):
        with self.assertRaises(ValueError):
            self.obj.wrapper = 'not_an_exe'
