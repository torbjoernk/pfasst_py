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

        if isinstance(initial, list):
            for l in initial:
                self.append_line(l)

    def append_line(self, line):
        if self._validate(line):
            self.lines.append(line)
        else:
            _log.error("LogLineBlock can only store LogLines: %s" % type(line))
            raise ValueError("LogLineBlock can only store LogLines: %s" % type(line))

    @property
    def lines(self):
        return self._lines

    def _validate(self, line):
        if isinstance(line, LogLine):
            return True
        return False


class TimeStepLogLinesBlock(LogLineBlock):
    TIME_STEP_BLOCK_START_PATTERN = '^Time\sStep\s(?P<step>[0-9]*)\sof\s(?P<total>[0-9]*)$'
    TIME_STEP_BLOCK_START_MATCHER = re.compile(TIME_STEP_BLOCK_START_PATTERN)

    def __init__(self, initial=None):
        super(TimeStepLogLinesBlock, self).__init__(initial)
        self._time_step = None
        self._total_steps = None

    @property
    def time_step(self):
        return self._time_step

    @property
    def total_steps(self):
        return self._total_steps

    def _validate(self, line):
        if super(TimeStepLogLinesBlock, self)._validate(line):
            if len(self.lines) == 0:
                if self._is_start_of_time_step_block(line):
                    return True
                else:
                    _log.warning("First line of Time Step Block must match certain criteria: %s" % line)
            else:
                if self._is_start_of_time_step_block(line):
                    _log.warning("Given line is start of a new Time Step Block: %s" % line)
                else:
                    return True
        return False

    def _is_start_of_time_step_block(self, line):
        if line.level.value == 'INFO':
            match = self.TIME_STEP_BLOCK_START_MATCHER.match(line.message.value)
            if match:
                self._time_step = int(match.group('step'))
                self._total_steps = int(match.group('total'))
                return True
            else:
                _log.debug("Message of first log line of time step block does not match pattern '%s': %s"
                           % (self.TIME_STEP_BLOCK_START_PATTERN, line.message.value))
        else:
            _log.debug("Level of first log line of time step block must be 'INFO': %s" % line.level.value)
        return False
