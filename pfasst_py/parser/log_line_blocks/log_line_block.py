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
        self._model = None

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
                return self._start_block_line_callback(match)
        else:
            _log.warning("Given line is not correctly parsed: %s" % line)
        return False

    def to_model(self):
        self._parse_to_model()
        return self._model

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
        return True

    def _start_block_line_callback(self, match):
        return True

    def _parse_to_model(self):
        pass
