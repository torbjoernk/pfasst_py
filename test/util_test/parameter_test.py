# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import unittest

from pfasst_py.util.parameter import Parameter, ValueParameter, BoolParameter


class ParameterTest(unittest.TestCase):
    def setUp(self):
        self.long = 'long'
        self.short = 'l'
        self.obj = Parameter(short=self.short, long=self.long)

    def test_has_short_name(self):
        self.assertEqual(self.obj.short, self.short)

    def test_has_long_name(self):
        self.assertEqual(self.obj.long, self.long)

    def test_requires_long_or_short_name(self):
        with self.assertRaises(ValueError):
            Parameter()
        Parameter(short='s')
        Parameter(long='long')

    def test_short_name_must_be_one_long(self):
        with self.assertRaises(ValueError):
            Parameter(short='')
        with self.assertRaises(ValueError):
            Parameter(short='not')

    def test_long_name_must_be_longer_one(self):
        with self.assertRaises(ValueError):
            Parameter(long='')
        with self.assertRaises(ValueError):
            Parameter(long='s')

    def test_formats_as_long(self):
        self.assertEqual(self.obj.as_long(), "--long")

    def test_formats_as_short(self):
        self.assertEqual(self.obj.as_short(), "-l")

    def test_str_is_long(self):
        self.assertEqual(str(self.obj), self.obj.as_long())


class ValueParameterTest(unittest.TestCase):
    def setUp(self):
        self.long = 'long'
        self.short = 'l'
        self.value = 3
        self.obj = ValueParameter(short=self.short, long=self.long, value=self.value)

    def test_is_parameter(self):
        self.assertTrue(issubclass(ValueParameter, Parameter))

    def test_has_value(self):
        self.assertEqual(self.obj.value, self.value)

    def test_can_set_value(self):
        self.assertEqual(self.obj.value, 3)
        self.obj.value = 5
        self.assertEqual(self.obj.value, 5)

    def test_formats_as_long(self):
        self.assertEqual(self.obj.as_long(), "--long 3")

    def test_formats_to_empty_without_value(self):
        self.obj.value = None
        self.assertEqual(self.obj.as_long(), "")
        self.assertEqual(self.obj.as_short(), "")

    def test_formats_as_short(self):
        self.assertEqual(self.obj.as_short(), "-l 3")

    def test_str_is_long(self):
        self.assertEqual(str(self.obj), self.obj.as_long())


class BoolParameterTest(unittest.TestCase):
    def setUp(self):
        self.long = 'long'
        self.short = 'l'
        self.obj = BoolParameter(short=self.short, long=self.long)

    def test_has_flag(self):
        self.assertFalse(self.obj.enabled)
        self.obj.enabled = True
        self.assertTrue(self.obj.enabled)

    def test_flag_only_boolean(self):
        with self.assertRaises(ValueError):
            self.obj.enabled = 'not bool'

    def test_can_toggle_state(self):
        self.assertFalse(self.obj.enabled)
        self.obj.toggle()
        self.assertTrue(self.obj.enabled)

    def test_formats_as_long(self):
        self.assertEqual(self.obj.as_long(), "")

        self.obj.enabled = True
        self.assertEqual(self.obj.as_long(), "--long")

    def test_formats_as_short(self):
        self.assertEqual(self.obj.as_short(), "")

        self.obj.enabled = True
        self.assertEqual(self.obj.as_short(), "-l")

    def test_str_is_long(self):
        self.assertEqual(str(self.obj), self.obj.as_long())
