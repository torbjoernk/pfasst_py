# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.runner.executable import Executable

_log = logging.getLogger(__name__)


class Wrapper(Executable):
    def __init__(self, *args, **kwargs):
        super(Wrapper, self).__init__(*args, **kwargs)

        self._wrapped = None

        if 'wrapped' in kwargs:
            self.wrapped = kwargs['wrapped']

    def build_cmd_line(self, additional_args=None):
        line = self.exe.build_cmd_line(additional_args=additional_args)

        if self.wrapped:
            line += " " + self.wrapped.build_cmd_line(additional_args=additional_args)
        else:
            _log.warning("No wrapped executable defined.")

        return line

    @property
    def exe(self):
        return self._exe

    @exe.setter
    def exe(self, value):
        if isinstance(value, Executable):
            self._exe = value
        else:
            self._exe = Executable(exe=value)

    @property
    def wrapped(self):
        return self._wrapped

    @wrapped.setter
    def wrapped(self, value):
        if isinstance(value, Executable):
            self._wrapped = value
        else:
            _log.error("Wrapped executable must be an Executable: %s" % type(value))
            raise ValueError("Wrapped executable must be an Executable: %s" % type(value))
