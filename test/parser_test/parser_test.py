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
        self.filecontent = read_data_file('no_mpi_log.log')

    def test_parses_non_mpi_file(self):
        self.obj.parse(self.filecontent)
        self.assertEqual(len(self.obj.lines), 84)

    def test_parse_blocks(self):
        self.assertListEqual(self.obj.time_steps, [])
        self.obj.parse(self.filecontent)
        self.obj.parse_blocks()
        self.assertEqual(len(self.obj.time_steps), 2)
        self.assertEqual(len(self.obj.time_steps[0].iterations), 9)
