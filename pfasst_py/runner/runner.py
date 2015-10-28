# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging
import subprocess as sp

from pfasst_py.util.fileutils import get_exe_path
from pfasst_py.runner.parameters import ParamsMixin

_log = logging.getLogger(__name__)


class Runner(ParamsMixin):
    def __init__(self, exe=None):
        super(Runner, self).__init__()
        self._exe = None

        if exe:
            self.exe = exe

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

    def run(self, additional_args=None):
        cmd = self.build_cmd_line(additional_args)

        try:
            _log.info("Executing '%s' ..." % cmd)
            proc = sp.run(cmd, stdout=sp.PIPE, stderr=sp.PIPE, shell=True, universal_newlines=True, check=True)
        except sp.CalledProcessError as err:
            _log.error("Command '%s' failed: %s" % (cmd, err))
            raise RuntimeError("Command '%s' failed: %s" % (cmd, err))

        _log.info("Finished.")

        if proc.stderr != "":
            _log.warning("Process put something on stderr: %s" % proc.stderr)

        return proc.stdout.strip().split('\n')

    @property
    def exe(self):
        return self._exe

    @exe.setter
    def exe(self, value):
        self._exe = get_exe_path(value)
