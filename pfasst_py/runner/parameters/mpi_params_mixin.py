# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.runner.parameters.params_mixin import ParamsMixin
from pfasst_py.util.parameter import ValueParameter

_log = logging.getLogger(__name__)


class MPIParamsMixin(ParamsMixin):
    def __init__(self):
        super(MPIParamsMixin, self).__init__()
        self._params.update({
            'np': ValueParameter(long='np')
        })
        self.np._long_dash = '-'

    @property
    def np(self):
        return self._params['np']
