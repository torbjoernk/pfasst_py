# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.model.iteration import Iteration

_log = logging.getLogger(__name__)


class TimeStep(object):
    def __init__(self):
        self._iterations = []
        self._index = None
        self._total_steps = None

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        if isinstance(value, int):
            if value >= 0:
                self._index = value
            else:
                _log.error("Invalid value for time step index: %s" % value)
                raise ValueError("Invalid value for time step index: %s" % value)
        elif isinstance(value, str):
            self.index = int(value)
        else:
            _log.error("Invalid type for time step index: %s (%s)" % (type(value), value))
            raise ValueError("Invalid type for time step index: %s (%s)" % (type(value), value))

    @property
    def total_steps(self):
        return self._total_steps

    @total_steps.setter
    def total_steps(self, value):
        if isinstance(value, int):
            if value >= 0:
                self._total_steps = value
            else:
                _log.error("Invalid value for total time steps: %s" % value)
                raise ValueError("Invalid value for total time steps: %s" % value)
        elif isinstance(value, str):
            self.total_steps = int(value)
        else:
            _log.error("Invalid type for total time steps: %s (%s)" % (type(value), value))
            raise ValueError("Invalid type for total time steps: %s (%s)" % (type(value), value))

    @property
    def iterations(self):
        if all([isinstance(i, Iteration) for i in self._iterations]):
            return self._iterations
        else:
            _log.error("Not all iterations in time step are Iterations.")
            raise RuntimeError("Not all iterations in time step are Iterations.")
