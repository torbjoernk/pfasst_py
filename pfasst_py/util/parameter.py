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
            return "%s %s" % (super(ValueParameter, self).as_long(), self._format_value())
        else:
            _log.debug("ValueParameter '%s' has no value." % self.long)
            return ""

    def as_short(self):
        if self.value:
            return "%s %s" % (super(ValueParameter, self).as_short(), self._format_value())
        else:
            _log.debug("ValueParameter '%s' has no value." % self.long)
            return ""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = self._validation(val)

    def _validation(self, value):
        return value

    def _format_value(self):
        return self.value


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


class IntegerParameter(ValueParameter):
    def __init__(self, *args, **kwargs):
        super(IntegerParameter, self).__init__(*args, **kwargs)

    def _validation(self, value):
        value = super(IntegerParameter, self)._validation(value)
        if isinstance(value, int):
            return value
        else:
            _log.error("Value '%s' is not an Integer: %s" % (value, type(value)))
            raise ValueError("Value '%s' is not an Integer: %s" % (value, type(value)))


class FloatParameter(ValueParameter):
    def __init__(self, *args, **kwargs):
        super(FloatParameter, self).__init__(*args, **kwargs)

    def _validation(self, value):
        value = super(FloatParameter, self)._validation(value)
        if isinstance(value, float):
            return value
        else:
            _log.error("Value '%s' is not a Float: %s" % (value, type(value)))
            raise ValueError("Value '%s' is not a Float: %s" % (value, type(value)))


class StringParameter(ValueParameter):
    def __init__(self, *args, **kwargs):
        super(StringParameter, self).__init__(*args, **kwargs)

    def _validation(self, value):
        value = super(StringParameter, self)._validation(value)
        if isinstance(value, str):
            return value
        else:
            _log.error("Value '%s' is not a String: %s" % (value, type(value)))
            raise ValueError("Value '%s' is not a String: %s" % (value, type(value)))


class ListParameter(ValueParameter):
    def __init__(self, *args, **kwargs):
        super(ListParameter, self).__init__(*args, **kwargs)
        self._delimiter = None

        self.delimiter = kwargs.get('delimiter', ',')

    @property
    def delimiter(self):
        return self._delimiter

    @delimiter.setter
    def delimiter(self, value):
        if isinstance(value, str):
            self._delimiter = value
        else:
            _log.error("List delimiter must be a String: %s" % type(value))
            raise ValueParameter("List delimiter must be a String: %s" % type(value))

    def _validation(self, value):
        value = super(ListParameter, self)._validation(value)
        if isinstance(value, (list, tuple)):
            return value
        else:
            _log.error("Value '%s' is not a List or Tuple: %s" % (value, type(value)))
            raise ValueError("Value '%s' is not a List or Tuple: %s" % (value, type(value)))

    def _format_value(self):
        return self._delimiter.join([str(v) for v in self.value])


class FaultyResetParameter(ListParameter):
    def __init__(self, *args, **kwargs):
        kwargs.update(long='reset', delimiter=',')
        if 'short' in kwargs:
            del kwargs['short']
        super(FaultyResetParameter, self).__init__(*args, **kwargs)

    def add_reset(self, reset):
        reset = self._validate_element(reset)
        if self.value is None:
            self._value = []
        self.value.append(reset)

    def _validation(self, value):
        value = super(FaultyResetParameter, self)._validation(value)
        validated = []
        for elem in value:
            validated.append(self._validate_element(elem))
        return validated

    @staticmethod
    def _validate_element(reset):
        if isinstance(reset, str):
            reset = reset.split('-')

        if isinstance(reset, (list, tuple)):
            if len(reset) == 3:
                return '-'.join([str(r) for r in reset])
            else:
                _log.error("Reset point must have exactly 3 values: %s" % reset)
                raise ValueError("Reset point must have exactly 3 values: %s" % reset)
        else:
            _log.error("Don't know how to deal with given reset point value: %s" % reset)
            raise ValueError("Don't know how to deal with given reset point value: %s" % reset)
