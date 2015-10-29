# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging
import re

from pfasst_py.parser.log_components import TimestampComponent, LoggerComponent, LevelComponent, RankComponent, \
    MessageComponent

_log = logging.getLogger(__name__)


class LogLine(object):
    COMPONENTS = {
        'timestamp': TimestampComponent,
        'logger': LoggerComponent,
        'level': LevelComponent,
        'rank': RankComponent,
        'message': MessageComponent
    }
    LINE_MATCHER_MPI = re.compile("^%s\s\[%s\s*,\s%s\s*,\s%s\s*\]\s%s$"
                                  % (TimestampComponent.REGEX, LoggerComponent.REGEX, LevelComponent.REGEX,
                                     RankComponent.REGEX, MessageComponent.REGEX))
    LINE_MATCHER_NO_MPI = re.compile("^%s\s\[%s\s*,\s%s\s*\]\s%s$"
                                     % (TimestampComponent.REGEX, LoggerComponent.REGEX, LevelComponent.REGEX,
                                        MessageComponent.REGEX))

    def __init__(self, line, auto_parse=True):
        self._raw = None
        self.auto_parse = auto_parse
        self._components = {}

        self.raw = line

    @property
    def timestamp(self):
        return self._components.get('timestamp', None)

    @property
    def logger(self):
        return self._components.get('logger', None)

    @property
    def level(self):
        return self._components.get('level', None)

    @property
    def rank(self):
        return self._components.get('rank', None)

    @property
    def message(self):
        return self._components.get('message', None)

    @property
    def raw(self):
        return self._raw

    @raw.setter
    def raw(self, value):
        self._raw = value
        if self.auto_parse:
            self._parse()

    def _parse(self):
        # noinspection PyTypeChecker
        mpi_match = self.LINE_MATCHER_MPI.match(self.raw)
        if mpi_match:
            self._populate_components(mpi_match.groupdict())
        else:
            # noinspection PyTypeChecker
            nompi_match = self.LINE_MATCHER_NO_MPI.match(self.raw)
            if nompi_match:
                self._populate_components(nompi_match.groupdict())
            else:
                _log.warning("Log line could not be parsed: '%s'" % self.raw)

    def _populate_components(self, groupdict):
        for comp, match in groupdict.items():
            self._components.update({comp: self.COMPONENTS[comp](match)})
