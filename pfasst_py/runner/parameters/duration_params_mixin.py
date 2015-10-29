# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging
from pfasst_py.runner.parameters.params_mixin import ParamsMixin
from pfasst_py.util.parameter import ValueParameter

_log = logging.getLogger(__name__)


class DurationParamsMixin(ParamsMixin):
    def __init__(self):
        super(DurationParamsMixin, self).__init__()
        self._params.update({
            'dt': ValueParameter(long='dt'),
            'tend': ValueParameter(long='tend'),
            'num_steps': ValueParameter(long='num_steps'),
            'num_iters': ValueParameter(long='num_iters')
        })

    @property
    def dt(self):
        return self._params['dt']

    @property
    def tend(self):
        return self._params['tend']

    @property
    def num_steps(self):
        return self._params['num_steps']

    @property
    def num_iters(self):
        return self._params['num_iters']
