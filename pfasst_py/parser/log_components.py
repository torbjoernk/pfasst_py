# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import datetime
import logging
import re

_log = logging.getLogger(__name__)


class LogComponent(object):
    REGEX = ''

    def __init__(self, value):
        self._value = None

        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = self._validation(val)

    def _parse(self, raw):
        return raw

    def _validation(self, value):
        return self._parse(value)


class TimestampComponent(LogComponent):
    REGEX = '(?P<timestamp>[0-9:,]*)'

    TIME_COMP_MATCHER = re.compile('^(?P<hour>[0-9]*):(?P<min>[0-9]*):(?P<sec>[0-9]*),(?P<msec>[0-9]*)$')

    def __init__(self, value):
        super(TimestampComponent, self).__init__(value)

    def _parse(self, raw):
        match = self.TIME_COMP_MATCHER.match(raw)
        if match:
            comp = match.groupdict()
            return datetime.time(int(comp['hour']), int(comp['min']), int(comp['sec']), int(comp['msec']))
        else:
            _log.error("Cannot parse timestamp: '%s'" % raw)
            raise ValueError("Cannot parse timestamp: '%s'" % raw)


class LoggerComponent(LogComponent):
    REGEX = '(?P<logger>[A-Z]*)'

    def __init__(self, value):
        super(LoggerComponent, self).__init__(value)


class LevelComponent(LogComponent):
    REGEX = '(?P<level>[A-Z0-9]*)'

    def __init__(self, value):
        super(LevelComponent, self).__init__(value)


class RankComponent(LogComponent):
    REGEX = 'MPI\s*(?P<rank>[0-9]*)'

    def __init__(self, value):
        super(RankComponent, self).__init__(value)


class MessageComponent(LogComponent):
    REGEX = '(?P<message>.*)'

    def __init__(self, value):
        super(MessageComponent, self).__init__(value)
