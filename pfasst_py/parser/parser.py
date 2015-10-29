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
        self._levels = {
            'DEBUG': [],
            'INFO': [],
            'WARN': [],
            'ERROR': [],
            'VERB1': [],
            'VERB2': [],
            'VERB3': [],
            'VERB4': [],
            'VERB5': [],
            'VERB6': [],
            'VERB7': [],
            'VERB8': [],
            'VERB9': [],
        }
        self._loggers = {}

    def parse(self, lines):
        if isinstance(lines, str):
            lines = lines.strip().split('\n')

        if isinstance(lines, list):
            if not self.lines:
                self._lines = []

            for line in lines:
                self.lines.append(LogLine(line))

            self._categorize_lines()

    @property
    def lines(self):
        return self._lines

    @property
    def levels(self):
        return self._levels

    @property
    def loggers(self):
        return self._loggers

    def _categorize_lines(self):
        if self.lines:
            for line in self.lines:
                level = line.level.value
                self.levels[level].append(line)

                logger = line.logger.value
                if logger not in self.loggers:
                    self.loggers.update({logger: []})
                self.loggers[logger].append(line)
        else:
            _log.error("No lines available.")
            raise RuntimeError("No lines available.")
