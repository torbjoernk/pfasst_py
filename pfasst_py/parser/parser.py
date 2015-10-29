# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.parser.log_line import LogLine

_log = logging.getLogger(__name__)


class Parser(object):
    def __init__(self):
        self._lines = None

    def parse(self, lines):
        if isinstance(lines, str):
            lines = lines.strip().split('\n')

        if isinstance(lines, list):
            if not self.lines:
                self._lines = []

            for line in lines:
                self.lines.append(LogLine(line))
        else:
            _log.error("Parser requires lines: %s" % type(lines))
            raise ValueError("Parser requires lines: %s" % type(lines))

    @property
    def lines(self):
        return self._lines
