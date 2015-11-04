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

    def __str__(self):
        return str(self.value)


class TimestampComponent(LogComponent):
    REGEX = '(?P<timestamp>[0-9.]*\s[0-9:,]*)'

    TIME_COMP_MATCHER = re.compile('^(?P<day>[0-9]{2})\.(?P<month>[0-9]{2})\.(?P<year>[0-9]{4})\s(?P<hour>[0-9]{2}):(?P<min>[0-9]{2}):(?P<sec>[0-9]{2}),(?P<msec>[0-9]*)$')

    def __init__(self, value):
        super(TimestampComponent, self).__init__(value)

    def _parse(self, raw):
        match = self.TIME_COMP_MATCHER.match(raw)
        if match:
            comp = match.groupdict()
            msec_digits = len(comp['msec'])
            return datetime.datetime(int(comp['year']), int(comp['month']), int(comp['day']), int(comp['hour']), int(comp['min']), int(comp['sec']), int(comp['msec']) * pow(10, 6 - msec_digits))
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
