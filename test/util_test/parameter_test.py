# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import unittest

from pfasst_py.util.parameter import Parameter, ValueParameter, \
    BoolParameter, IntegerParameter, FloatParameter, StringParameter, ListParameter, \
    FaultyResetParameter


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


class IntegerParameterTest(unittest.TestCase):
    def setUp(self):
        self.obj = IntegerParameter(long='int')

    def test_is_value_parameter(self):
        self.assertIsInstance(self.obj, ValueParameter)

    def test_denies_non_integer_values(self):
        with self.assertRaises(ValueError):
            self.obj.value = 'not an int'
        with self.assertRaises(ValueError):
            self.obj.value = 3.4

    def test_accepts_integers(self):
        self.obj.value = 42
        self.assertEqual(self.obj.value, 42)


class FloatParameterTest(unittest.TestCase):
    def setUp(self):
        self.obj = FloatParameter(long='float')

    def test_is_value_parameter(self):
        self.assertIsInstance(self.obj, ValueParameter)

    def test_denies_non_float_values(self):
        with self.assertRaises(ValueError):
            self.obj.value = 'not a float'
        with self.assertRaises(ValueError):
            self.obj.value = True

    def test_accepts_floats(self):
        self.obj.value = 42.21
        self.assertEqual(self.obj.value, 42.21)


class StringParameterTest(unittest.TestCase):
    def setUp(self):
        self.obj = StringParameter(long='string')

    def test_is_value_parameter(self):
        self.assertIsInstance(self.obj, ValueParameter)

    def test_denies_non_string_values(self):
        with self.assertRaises(ValueError):
            self.obj.value = 3
        with self.assertRaises(ValueError):
            self.obj.value = 42.1
        with self.assertRaises(ValueError):
            self.obj.value = False

    def test_accepts_integers(self):
        self.obj.value = 'valid value'
        self.assertEqual(self.obj.value, 'valid value')


class ListParameterTest(unittest.TestCase):
    def setUp(self):
        self.obj = ListParameter(long='list')

    def test_is_value_parameter(self):
        self.assertIsInstance(self.obj, ValueParameter)

    def test_denies_non_list_or_tuple_values(self):
        with self.assertRaises(ValueError):
            self.obj.value = 3
        with self.assertRaises(ValueError):
            self.obj.value = 'string'
        with self.assertRaises(ValueError):
            self.obj.value = True
        with self.assertRaises(ValueError):
            self.obj.value = 42.21

    def test_accepts_lists(self):
        self.obj.value = [1, 's']
        self.assertSequenceEqual(self.obj.value, [1, 's'])

    def test_accepts_tuples(self):
        self.obj.value = (1, 's')
        self.assertSequenceEqual(self.obj.value, (1, 's'))

    def test_formats_values(self):
        self.obj.value = [1, 's']
        self.assertEqual(self.obj.as_long(), "--list 1,s")

    def test_takes_custom_delimiter(self):
        self.obj.delimiter = '-'
        self.obj.value = [1, 's']
        self.assertEqual(self.obj.as_long(), "--list 1-s")

    def test_custom_delimiter_must_be_string(self):
        with self.assertRaises(ValueError):
            self.obj.delimiter = 3


class FaultyResetParameterTest(unittest.TestCase):
    def setUp(self):
        self.obj = FaultyResetParameter()

    def test_does_not_require_long_parameter(self):
        FaultyResetParameter()

    def test_is_list_parameter(self):
        self.assertIsInstance(self.obj, ListParameter)

    def test_add_single_reset_point(self):
        self.obj.add_reset('1-2-3')
        self.assertSequenceEqual(self.obj.value, ['1-2-3'])

        self.obj.add_reset((4, 5, 6))
        self.assertSequenceEqual(self.obj.value, ['1-2-3', '4-5-6'])

    def test_cannot_add_multiple_resets_at_once(self):
        with self.assertRaises(ValueError):
            self.obj.add_reset('1-2-3,5-6-7')

    def test_can_only_handle_str_and_list_or_tuple(self):
        with self.assertRaises(ValueError):
            self.obj.add_reset(3)

    def test_set_all_resets_at_once(self):
        self.obj.value = ['1-2-3', (4, 5, 6)]
        self.assertEqual(self.obj.value, ['1-2-3', '4-5-6'])

    def test_formats_command_line(self):
        self.obj.value = ['1-2-3', (4, 5, 6)]
        self.assertEqual(self.obj.as_long(), "--reset 1-2-3,4-5-6")
