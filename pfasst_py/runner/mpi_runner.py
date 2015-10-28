# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.runner.runner import Runner
from pfasst_py.runner.wrapper_mixin import WrapperMixin

_log = logging.getLogger(__name__)


class MPIRunner(Runner, WrapperMixin):
    def __init__(self, *args, **kwargs):
        super(MPIRunner, self).__init__(*args, **kwargs)
        self._np = None

    def build_cmd_line(self, args=None):
        cmd = super(MPIRunner, self).build_cmd_line(args)
        if self.wrapper:
            if self.np:
                return "%s -np %s %s" % (self.wrapper.as_posix(), self.np, cmd)
            else:
                _log.error("MPI-Wrapper defined but not number procs.")
                raise RuntimeError("MPI-Wrapper defined but not number procs.")
        else:
            _log.debug("MPI-Wrapper not defined. Using base cmd line.")
        return cmd

    @property
    def np(self):
        return self._np

    @np.setter
    def np(self, value):
        if isinstance(value, int) and value > 0:
            self._np = value
        else:
            _log.error("np must be an int larger 0: %s (%s)" % (value, type(value)))
            raise ValueError("np must be an int larger 0: %s (%s)" % (value, type(value)))
