# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.parser.log_line_blocks.time_step_block import TimeStepLogLinesBlock
from pfasst_py.parser.log_line_blocks.iterations_block import IterationLogLinesBlock
from pfasst_py.parser.log_line import LogLine

_log = logging.getLogger(__name__)


class Parser(object):
    def __init__(self):
        self._lines = None
        self._time_steps = []

    def parse(self, lines):
        if isinstance(lines, str):
            lines = lines.strip().split('\n')

        if isinstance(lines, list):
            if not self.lines:
                self._lines = []

            for line in lines:
                logline = LogLine(line)
                if len(logline.message.value) > 0:
                    self.lines.append(LogLine(line))

    def parse_blocks(self):
        if self.lines:
            for line in self.lines:
                if TimeStepLogLinesBlock().is_start_of_block(line):
                    self.time_steps.append(TimeStepLogLinesBlock([line]))
                elif len(self.time_steps) > 0:
                    self.time_steps[-1].append_line(line)
                    if IterationLogLinesBlock().is_start_of_block(line):
                        self.time_steps[-1].iterations.append(IterationLogLinesBlock([line]))
                    elif len(self.time_steps[-1].iterations) > 0:
                        self.time_steps[-1].iterations[-1].append_line(line)
                _log.debug("")
        else:
            _log.error("Lines required for parsing into Time Step Blocks.")
            raise RuntimeError("Lines required for parsing into Time Step Blocks.")

    @property
    def lines(self):
        return self._lines

    @property
    def time_steps(self):
        return self._time_steps
