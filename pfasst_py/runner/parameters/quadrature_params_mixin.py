# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.runner.parameters.params_mixin import ParamsMixin
from pfasst_py.util.parameter import ValueParameter

_log = logging.getLogger(__name__)


class QuadratureParamsMixin(ParamsMixin):
    def __init__(self):
        super(QuadratureParamsMixin, self).__init__()
        self._params.update({
            'num_nodes': ValueParameter(long='num_nodes')
        })

    @property
    def num_nodes(self):
        return self._params['num_nodes']
