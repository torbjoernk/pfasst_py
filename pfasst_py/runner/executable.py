# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.util.fileutils import get_exe_path
from pfasst_py.runner.parameters import ParamsMixin, MPIParamsMixin

_log = logging.getLogger(__name__)


class Executable(ParamsMixin):
    def __init__(self, *args, **kwargs):
        super(Executable, self).__init__()
        self._exe = None

        if 'exe' in kwargs:
            self.exe = kwargs['exe']

    def build_cmd_line(self, additional_args=None):
        if self.exe:
            line = self.exe.as_posix()

            params = self.params_to_line()
            if params != "":
                line += " " + params

            if additional_args:
                if not isinstance(additional_args, (tuple, list)):
                    additional_args = (additional_args, )
                line += " " + ' '.join(str(a) for a in additional_args)

            return line
        else:
            _log.error("No executable defined.")
            raise RuntimeError("No executable defined.")

    @property
    def exe(self):
        return self._exe

    @exe.setter
    def exe(self, value):
        self._exe = get_exe_path(value)


class MPIExec(Executable, MPIParamsMixin):
    def __init__(self, *args, **kwargs):
        super(MPIExec, self).__init__(*args, **kwargs)

        try:
            self.exe = 'mpiexec'
        except ValueError:
            _log.warning("mpiexec not found in PATH")
