# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging
import re

from pfasst_py.parser.log_line import LogLine

_log = logging.getLogger(__name__)


class LogLineBlock(object):
    def __init__(self, initial=None):
        self._lines = []

        self._block_start_matcher = re.compile(self._block_start_pattern())

        if isinstance(initial, list):
            for l in initial:
                self.append_line(l)

    def append_line(self, line):
        if self._validate(line):
            self.lines.append(line)
        else:
            _log.error("Given line could not be validated: %s" % line)
            raise ValueError("Given line could not be validated: %s" % line)

    def is_start_of_block(self, line):
        if line.is_parsed:
            match = self._block_start_matcher.match(line.message.value)
            if match:
                _log.debug("Given line is the start of a new block: %s" % line)
                return self._start_block_line_callback(match)
            else:
                _log.debug("First line of Block must match pattern '%s': %s"
                           % (self._block_start_pattern(), line.message.value))
        else:
            _log.warning("Given line is not correctly parsed: %s" % line)
        return False

    @property
    def lines(self):
        return self._lines

    @staticmethod
    def _block_start_pattern():
        return ''

    def _validate(self, line):
        _log.debug("validating: %r" % line)
        if isinstance(line, LogLine):
            if len(self.lines) == 0:
                if self.is_start_of_block(line):
                    return True
                else:
                    _log.warning("First line of Block must match certain criteria: %s" % line)
            else:
                if self._is_block_line(line):
                    return True
                else:
                    _log.warning("Given line is start of a new Block: %s" % line)
        return False

    def _is_block_line(self, line):
        if self.is_start_of_block(line):
            return False
        _log.debug("Given line is a normal line in the block: %s" % line)
        return True

    def _start_block_line_callback(self, match):
        return True


class TimeStepLogLinesBlock(LogLineBlock):
    def __init__(self, initial=None):
        super(TimeStepLogLinesBlock, self).__init__(initial)
        self._time_step = None
        self._total_steps = None
        self.iterations = []

    def is_start_of_block(self, line):
        if line.level.value == 'INFO':
            return super(TimeStepLogLinesBlock, self).is_start_of_block(line)
        else:
            _log.debug("Level of first log line of time step block must be 'INFO': %s" % line.level.value)
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


class IterationLogLinesBlock(LogLineBlock):
    def __init__(self, initial=None):
        super(IterationLogLinesBlock, self).__init__(initial)
        self._iteri = None

    def is_start_of_block(self, line):
        if line.level.value == 'INFO':
            return super(IterationLogLinesBlock, self).is_start_of_block(line)
        else:
            _log.debug("Level of first log line of iteration block must be 'INFO': %s" % line.level.value)
            return False

    @property
    def iteri(self):
        return self._iteri

    @staticmethod
    def _block_start_pattern():
        return '^Iteration\s(?P<iteri>[0-9]*)$'

    def _start_block_line_callback(self, match):
        self._iteri = int(match.group('iteri'))
        return True
