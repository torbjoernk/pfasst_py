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

    def test_requires_parsed_lines_for_categorization(self):
        with self.assertRaises(RuntimeError):
            self.obj._categorize_lines()

    def test_categorizes_levels(self):
        filecontent = read_data_file('no_mpi_log.log')
        self.obj.parse(filecontent)
        self.assertEqual(len(self.obj.levels['DEBUG']), 8)
        self.assertEqual(len(self.obj.levels['WARN']), 8)
        self.assertEqual(len(self.obj.levels['INFO']), 46)

    def test_categorizes_loggers(self):
        filecontent = read_data_file('no_mpi_log.log')
        self.obj.parse(filecontent)
        self.assertEqual(len(self.obj.loggers['DEFAULT']), 9)
        self.assertEqual(len(self.obj.loggers['SDC']), 28)
        self.assertEqual(len(self.obj.loggers['SWEEPER']), 25)
