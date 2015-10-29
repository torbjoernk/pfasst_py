# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.runner.parameters.params_mixin import ParamsMixin
from pfasst_py.util.parameter import ValueParameter

_log = logging.getLogger(__name__)


class ToleranceParamsMixin(ParamsMixin):
    def __init__(self):
        super(ToleranceParamsMixin, self).__init__()
        self._params.update({
            'abs_res_tol': ValueParameter(long='abs_res_tol'),
            'rel_res_tol': ValueParameter(long='rel_res_tol')
        })

    @property
    def abs_res_tol(self):
        return self._params['abs_res_tol']

    @property
    def rel_res_tol(self):
        return self._params['rel_res_tol']
