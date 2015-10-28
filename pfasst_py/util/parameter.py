# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

_log = logging.getLogger(__name__)


class Parameter(object):
    def __init__(self, *args, **kwargs):
        self._short = None
        self._long = None

        if 'long' in kwargs:
            if isinstance(kwargs['long'], str) and len(kwargs['long']) > 1:
                self._long = kwargs['long']
            else:
                _log.error("long cmd parameter must be longer than 1: %s" % kwargs['long'])
                raise ValueParameter("long cmd parameter must be longer than 1: %s" % kwargs['long'])

        if 'short' in kwargs:
            if isinstance(kwargs['short'], str) and len(kwargs['short']) == 1:
                self._short = kwargs['short']
            else:
                _log.error("short cmd parameter must be exactly 1 long: %s" % kwargs['short'])
                raise ValueParameter("short cmd parameter must be exactly 1 long: %s" % kwargs['short'])

        if not self.long and not self.short:
            _log.error("At least either short (%s) or long (%s) name must be specified." % (self.short, self.long))
            raise ValueError("At least either short (%s) or long (%s) name must be specified." % (self.short, self.long))

    def as_long(self):
        return "--%s" % self.long

    def as_short(self):
        return "-%s" % self.short

    @property
    def long(self):
        return self._long

    @property
    def short(self):
        return self._short

    def __str__(self):
        return self.as_long()


class ValueParameter(Parameter):
    def __init__(self, *args, **kwargs):
        super(ValueParameter, self).__init__(*args, **kwargs)
        self._value = None

        if 'value' in kwargs:
            self.value = kwargs['value']

    def as_long(self):
        if self.value:
            return "%s %s" % (super(ValueParameter, self).as_long(), self.value)
        else:
            _log.debug("ValueParameter '%s' has no value." % self.long)
            return ""

    def as_short(self):
        if self.value:
            return "%s %s" % (super(ValueParameter, self).as_short(), self.value)
        else:
            _log.debug("ValueParameter '%s' has no value." % self.long)
            return ""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val


class BoolParameter(Parameter):
    def __init__(self, *args, **kwargs):
        super(BoolParameter, self).__init__(*args, **kwargs)
        self._enabled = False

    def as_long(self):
        if self.enabled:
            return super(BoolParameter, self).as_long()
        else:
            return ""

    def as_short(self):
        if self.enabled:
            return super(BoolParameter, self).as_short()
        else:
            return ""

    def toggle(self):
        self.enabled = not self.enabled

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if isinstance(value, bool):
            self._enabled = value
        else:
            _log.error("Boolean parameter requires bool value: %s" % value)
            raise ValueError("Boolean parameter requires bool value: %s" % value)
