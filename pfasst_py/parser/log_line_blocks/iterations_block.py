# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging
import re

from pfasst_py.parser.log_line_blocks.log_line_block import LogLineBlock
from pfasst_py.model.iteration import Iteration

_log = logging.getLogger(__name__)


class IterationLogLinesBlock(LogLineBlock):
    def __init__(self, initial=None):
        self._iteri = None
        super(IterationLogLinesBlock, self).__init__(initial)
        self._model = Iteration()

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

    def _parse_to_model(self):
        super(IterationLogLinesBlock, self)._parse_to_model()

        self._model.index = self.iteri
        data_re = re.compile('^.*\|abs\sresidual\|\s=\s(?P<abs_res>[0-9.e-]*)\s*\|rel\sresidual\|\s=\s(?P<rel_res>[0-9.e-]*).*$')
        t_start = None
        t_end = None

        for line in self.lines:
            if not t_start:
                t_start = line.timestamp.value
            match = data_re.match(line.message.value)
            if match:
                self._model.abs_res = match.group('abs_res')
                self._model.rel_res = match.group('rel_res')
            t_end = line.timestamp.value

        self._model.timing = t_end - t_start
