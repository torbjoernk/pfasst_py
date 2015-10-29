# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging
from pfasst_py.runner.parameters.params_mixin import ParamsMixin
from pfasst_py.util.parameter import ValueParameter, BoolParameter

_log = logging.getLogger(__name__)


class GlobalParamsMixin(ParamsMixin):
    def __init__(self):
        super(GlobalParamsMixin, self).__init__()
        self._params.update({
            'quiet': BoolParameter(long='quiet', short='q'),
            'log_prefix': ValueParameter(long='log_prefix'),
            'nocolor': BoolParameter(long='nocolor', short='c')
        })

    @property
    def quiet(self):
        return self._params['quiet']

    @property
    def log_prefix(self):
        return self._params['log_prefix']

    @property
    def nocolor(self):
        return self._params['nocolor']
