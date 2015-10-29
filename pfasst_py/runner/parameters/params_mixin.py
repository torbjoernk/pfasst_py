# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

_log = logging.getLogger(__name__)


class ParamsMixin(object):
    def __init__(self):
        self._params = {}

    def params_to_line(self):
        return ' '.join([str(value) for _, value in self._params.items()])
