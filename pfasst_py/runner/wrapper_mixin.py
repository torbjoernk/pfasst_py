# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.util.fileutils import get_exe_path

_log = logging.getLogger(__name__)


class WrapperMixin(object):
    def __init__(self):
        self._wrapper = None

    @property
    def wrapper(self):
        return self._wrapper

    @wrapper.setter
    def wrapper(self, value):
        self._wrapper = get_exe_path(value)
        _log.debug("wrapper set: %s" % self.wrapper)
