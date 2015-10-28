# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.util.parameter import ValueParameter, BoolParameter

_log = logging.getLogger(__name__)


class ParamsMixin(object):
    def __init__(self):
        self._params = {}

    def params_to_line(self):
        return ' '.join([str(value) for _, value in self._params.items()])


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


class QuadratureParamsMixin(ParamsMixin):
    def __init__(self):
        super(QuadratureParamsMixin, self).__init__()
        self._params.update({
            'num_nodes': ValueParameter(long='num_nodes')
        })

    @property
    def num_nodes(self):
        return self._params['num_nodes']


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


class SDCParamsMixin(GlobalParamsMixin, DurationParamsMixin, QuadratureParamsMixin, ToleranceParamsMixin):
    def __init__(self):
        super(SDCParamsMixin, self).__init__()


class MLSDCParamsMixin(SDCParamsMixin):
    def __init__(self):
        super(MLSDCParamsMixin, self).__init__()
        self._params.update({
            'coarse_factor': ValueParameter(long='coarse_factor')
        })

    @property
    def coarse_factor(self):
        return self._params['coarse_factor']


class PfasstParamsMixin(MLSDCParamsMixin):
    def __init__(self):
        super(PfasstParamsMixin, self).__init__()


class FaultyPfasstParamsMixin(PfasstParamsMixin):
    def __init__(self):
        super(FaultyPfasstParamsMixin, self).__init__()
        self._params.update({
            'reset': ValueParameter(long='reset')
        })

    @property
    def reset(self):
        return self._params['reset']
