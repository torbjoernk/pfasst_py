# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.parser.parser import Parser

_log = logging.getLogger(__name__)


class Analyzer(object):
    def __init__(self, parser=None):
        self._parser = None

        if parser:
            self.parser = parser

    def analyze(self):
        if self.parser is None:
            _log.error("Parser must be present for analyzation.")
            raise RuntimeError("Parser must be present for analyzation.")

    @property
    def parser(self):
        return self._parser

    @parser.setter
    def parser(self, value):
        if isinstance(value, Parser):
            self._parser = value
        else:
            _log.error("Parser must be a valid Parser: %s" % type(value))
            raise ValueError("Parser must be a valid Parser: %s" % type(value))
