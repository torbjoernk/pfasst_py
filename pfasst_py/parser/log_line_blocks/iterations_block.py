# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.parser.log_line_blocks.log_line_block import LogLineBlock

_log = logging.getLogger(__name__)


class IterationLogLinesBlock(LogLineBlock):
    def __init__(self, initial=None):
        super(IterationLogLinesBlock, self).__init__(initial)
        self._iteri = None

    def is_start_of_block(self, line):
        if line.level.value == 'INFO':
            return super(IterationLogLinesBlock, self).is_start_of_block(line)
        return False

    @property
    def iteri(self):
        return self._iteri

    @staticmethod
    def _block_start_pattern():
        return '^Iteration\s(?P<iteri>[0-9]*).*$'

    def _start_block_line_callback(self, match):
        self._iteri = int(match.group('iteri'))
        return True
