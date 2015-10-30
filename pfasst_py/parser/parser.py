# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.parser.log_line import LogLine
from pfasst_py.parser.log_line_block import TimeStepLogLinesBlock, IterationLogLinesBlock

_log = logging.getLogger(__name__)


class Parser(object):
    BLOCK_TYPES = {
        'time_steps': TimeStepLogLinesBlock,
        'iterations': IterationLogLinesBlock
    }

    def __init__(self):
        self._lines = None
        self._blocks = {block: [] for block in self.BLOCK_TYPES.keys()}

    def parse(self, lines):
        if isinstance(lines, str):
            lines = lines.strip().split('\n')

        if isinstance(lines, list):
            if not self.lines:
                self._lines = []

            for line in lines:
                self.lines.append(LogLine(line))

    def parse_blocks(self):
        for block in self.BLOCK_TYPES.keys():
            self._parse_block(block)

    def _parse_block(self, block_type):
        if self.lines:
            for line in self.lines:
                if self.BLOCK_TYPES[block_type]().is_start_of_block(line):
                    self.__getattribute__(block_type).append(self.BLOCK_TYPES[block_type]([line]))
                elif len(self._blocks[block_type]) > 0:
                    self.__getattribute__(block_type)[-1].append_line(line)
        else:
            _log.error("Lines required for parsing into Time Step Blocks.")
            raise RuntimeError("Lines required for parsing into Time Step Blocks.")

    @property
    def lines(self):
        return self._lines

    @property
    def time_steps(self):
        return self._blocks.get('time_steps', [])

    @property
    def iterations(self):
        return self._blocks.get('iterations', [])
