# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import datetime
import logging

_log = logging.getLogger(__name__)


class Iteration(object):
    def __init__(self):
        self._index = None
        self._rel_res = None
        self._abs_res = None
        self._timing = None

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        if isinstance(value, int):
            if value >= 0:
                self._index = value
            else:
                _log.error("Invalid value for iteration index: %s" % value)
                raise ValueError("Invalid value for iteration index: %s" % value)
        elif isinstance(value, str):
            self.index = int(value)
        else:
            _log.error("Invalid type for index: %s (%s)" % (type(value), value))
            raise ValueError("Invalid type for index: %s (%s)" % (type(value), value))

    @property
    def rel_res(self):
        return self._rel_res

    @rel_res.setter
    def rel_res(self, value):
        if isinstance(value, str):
            self.rel_res = float(value)
        elif isinstance(value, float):
            self._rel_res = value
        else:
            _log.error("Invalid type for rel_res: %s (%s)" % (type(value), value))
            raise ValueError("Invalid type for rel_res: %s (%s)" % (type(value), value))

    @property
    def abs_res(self):
        return self._abs_res

    @abs_res.setter
    def abs_res(self, value):
        if isinstance(value, str):
            self.abs_res = float(value)
        elif isinstance(value, float):
            self._abs_res = value
        else:
            _log.error("Invalid type for abs_res: %s (%s)" % (type(value), value))
            raise ValueError("Invalid type for abs_res: %s (%s)" % (type(value), value))

    @property
    def timing(self):
        return self._timing

    @timing.setter
    def timing(self, value):
        if isinstance(value, datetime.timedelta):
            self._timing = value
        else:
            _log.error("Invalid type for timing: %s (%s)" % (type(value), value))
            raise ValueError("Invalid type for timing: %s (%s)" % (type(value), value))

    def __str__(self):
        return "Iteration[%s, abs_res=%s, rel_res=%s, timing=%s]"\
               % (self.index, self.abs_res, self.rel_res, self.timing)
