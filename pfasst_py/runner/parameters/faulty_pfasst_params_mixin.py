# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.runner.parameters.pfasst_params_mixin import PfasstParamsMixin
from pfasst_py.util.parameter import FaultyResetParameter

_log = logging.getLogger(__name__)


class FaultyPfasstParamsMixin(PfasstParamsMixin):
    def __init__(self):
        super(FaultyPfasstParamsMixin, self).__init__()
        self._params.update({
            'reset': FaultyResetParameter(long='reset')
        })

    @property
    def reset(self):
        return self._params['reset']
