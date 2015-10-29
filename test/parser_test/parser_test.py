# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import unittest

from pfasst_py.parser.parser import Parser
from test.helper import read_data_file


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.obj = Parser()

    def test_parses_non_mpi_file(self):
        filecontent = read_data_file('no_mpi_log.log')
        self.obj.parse(filecontent)
        self.assertEqual(len(self.obj.lines), 62)
