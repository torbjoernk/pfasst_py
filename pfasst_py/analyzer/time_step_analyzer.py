# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.analyzer.analyzer import Analyzer

_log = logging.getLogger(__name__)


class TimeStepAnalyzer(Analyzer):
    def __init__(self):
        super(TimeStepAnalyzer, self).__init__()

        self._time_steps = []

    def analyze(self):
        super(TimeStepAnalyzer, self).analyze()

        if len(self.parser.levels['INFO']) > 0:
            for info_line in self.parser.levels['INFO']:
                # TODO do something with the INFO line
                pass
        else:
            _log.error("No 'INFO' lines found in log.")
            raise RuntimeError("No 'INFO' lines found in log.")

    @property
    def time_steps(self):
        return self._time_steps
