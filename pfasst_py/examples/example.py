# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.runner.runner import Runner
from pfasst_py.runner.parameters import GlobalParamsMixin
from pfasst_py.util.fileutils import get_directory_path

_log = logging.getLogger(__name__)


class Example(Runner, GlobalParamsMixin):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self._directory = None
        if 'directory' in kwargs:
            self.directory = kwargs['directory']

    @property
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, value):
        self._directory = get_directory_path(value)
