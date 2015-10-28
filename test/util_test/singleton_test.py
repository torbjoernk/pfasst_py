# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import unittest

from pfasst_py.util.singleton import Singleton


class SingletonTest(unittest.TestCase):
    def test_as_decorator(self):
        @Singleton
        class Foo(object):
            pass

        foo1 = Foo.instance()
        self.assertIsInstance(foo1, Foo)

    def test_cannot_instantiate_directly(self):
        @Singleton
        class Foo(object):
            pass

        with self.assertRaises(TypeError):
            Foo()
