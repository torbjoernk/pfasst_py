# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.runner.parameters.sdc_params_mixin import SDCParamsMixin
from pfasst_py.util.parameter import ValueParameter

_log = logging.getLogger(__name__)


class MLSDCParamsMixin(SDCParamsMixin):
    def __init__(self):
        super(MLSDCParamsMixin, self).__init__()
        self._params.update({
            'coarse_factor': ValueParameter(long='coarse_factor')
        })

    @property
    def coarse_factor(self):
        return self._params['coarse_factor']
