# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.runner.runner import Runner
from pfasst_py.util.fileutils import get_directory_path

_log = logging.getLogger(__name__)


class Example(object):
    def __init__(self, *args, **kwargs):
        self._directory = None
        self._rundir = None
        self._runner = None

        if 'directory' in kwargs:
            self.directory = kwargs['directory']

        self._rundir = None
        if 'rundir' in kwargs:
            self.rundir = kwargs['rundir']

    def run(self, additional_args=None):
        if self.runner:
            self.runner.run(additional_args=additional_args, cwd=self.rundir)
        else:
            _log.error("No runner defined.")
            raise RuntimeError("No runner defined.")

    @property
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, value):
        self._directory = get_directory_path(value)

    @property
    def rundir(self):
        return self._rundir

    @rundir.setter
    def rundir(self, value):
        self._rundir = get_directory_path(value)

    @property
    def runner(self):
        return self._runner

    @runner.setter
    def runner(self, value):
        if isinstance(value, Runner):
            self._runner = value
        else:
            _log.error("Runner expected: %s" % type(value))
            raise ValueError("Runner expected: %s" % type(value))
