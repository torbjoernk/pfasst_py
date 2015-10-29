# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging
import os
import subprocess as sp

from pfasst_py.runner.executable import Executable

_log = logging.getLogger(__name__)


class Runner(object):
    def __init__(self, *args, **kwargs):
        self._exe = None

    def run(self, additional_args=None, cwd=None):
        if self.exe:
            cmd = self.exe.build_cmd_line(additional_args=additional_args)

            if cwd is None:
                cwd = os.getcwd()

            try:
                _log.info("Executing '%s' ..." % cmd)
                proc = sp.run(cmd, cwd=cwd, stdout=sp.PIPE, stderr=sp.PIPE, shell=True, universal_newlines=True, check=True)
            except sp.CalledProcessError as err:
                _log.error("Command '%s' failed: %s" % (cmd, err))
                raise RuntimeError("Command '%s' failed: %s" % (cmd, err))

            _log.info("Finished.")

            if proc.stderr != "":
                _log.warning("Process put something on stderr: %s" % proc.stderr)

            return proc.stdout.strip().split('\n')
        else:
            _log.error("No executable given.")
            raise RuntimeError("No executable given.")

    @property
    def exe(self):
        return self._exe

    @exe.setter
    def exe(self, value):
        if isinstance(value, Executable):
            self._exe = value
        else:
            _log.error("Runner requires an Executable: %s" % type(Executable))
            raise ValueError("Runner requires an Executable: %s" % type(Executable))
