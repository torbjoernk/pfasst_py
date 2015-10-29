# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import datetime
import unittest

from pfasst_py.parser.log_line import LogLine


class LogLineTest(unittest.TestCase):
    def setUp(self):
        self.msg_normal = "13:51:15,37 [PFASST    , INFO , MPI    0] PFASST Prediction step"
        self.msg_no_text = "13:51:15,37 [PFASST    , INFO , MPI    0] "
        self.msg_no_mpi = "13:51:15,37 [SDC       , INFO ] PFASST Prediction step"
        self.msg_no_mpi_no_text = "13:51:15,37 [SDC       , INFO ] "

    def test_parse_mpi_line_with_message(self):
        obj = LogLine(self.msg_normal)
        self.assertEqual(obj.timestamp.value, datetime.time(13, 51, 15, 37))
        self.assertEqual(obj.logger.value, 'PFASST')
        self.assertEqual(obj.level.value, 'INFO')
        self.assertEqual(obj.rank.value, '0')
        self.assertEqual(obj.message.value, 'PFASST Prediction step')

    def test_parse_mpi_line_without_message(self):
        obj = LogLine(self.msg_no_text)
        self.assertEqual(obj.timestamp.value, datetime.time(13, 51, 15, 37))
        self.assertEqual(obj.logger.value, 'PFASST')
        self.assertEqual(obj.level.value, 'INFO')
        self.assertEqual(obj.rank.value, '0')
        self.assertEqual(obj.message.value, '')

    def test_parse_non_mpi_line_with_message(self):
        obj = LogLine(self.msg_no_mpi)
        self.assertEqual(obj.timestamp.value, datetime.time(13, 51, 15, 37))
        self.assertEqual(obj.logger.value, 'SDC')
        self.assertEqual(obj.level.value, 'INFO')
        self.assertIsNone(obj.rank)
        self.assertEqual(obj.message.value, 'PFASST Prediction step')

    def test_parse_non_mpi_line_without_message(self):
        obj = LogLine(self.msg_no_mpi_no_text)
        self.assertEqual(obj.timestamp.value, datetime.time(13, 51, 15, 37))
        self.assertEqual(obj.logger.value, 'SDC')
        self.assertEqual(obj.level.value, 'INFO')
        self.assertIsNone(obj.rank)
        self.assertEqual(obj.message.value, '')
