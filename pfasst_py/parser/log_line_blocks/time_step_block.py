# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.parser.log_line_blocks.log_line_block import LogLineBlock
from pfasst_py.model.time_step import TimeStep

_log = logging.getLogger(__name__)


class TimeStepLogLinesBlock(LogLineBlock):
    def __init__(self, initial=None):
        super(TimeStepLogLinesBlock, self).__init__(initial)
        self._model = TimeStep()
        self._time_step = None
        self._total_steps = None
        self.iterations = []

    def is_start_of_block(self, line):
        if line.level.value == 'INFO':
            return super(TimeStepLogLinesBlock, self).is_start_of_block(line)
        return False

    @property
    def time_step(self):
        return self._time_step

    @property
    def total_steps(self):
        return self._total_steps

    @staticmethod
    def _block_start_pattern():
        return '^Time\sStep\s(?P<step>[0-9]*)\sof\s(?P<total>[0-9]*)$'

    def _start_block_line_callback(self, match):
        self._time_step = int(match.group('step'))
        self._total_steps = int(match.group('total'))
        return True

    def _parse_to_model(self):
        super(TimeStepLogLinesBlock, self)._parse_to_model()

        self._model.index = self.time_step
        self._model.total_steps = self.total_steps

        for iteration in self.iterations:
            self._model.iterations.append(iteration.to_model())
