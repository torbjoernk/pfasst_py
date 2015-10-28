# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.kaltt@fz-juelich.de>
"""
import logging

from pfasst_py.examples.example import Example
from pfasst_py.runner.parameters import ParamsMixin
from pfasst_py.util.parameter import ValueParameter

_log = logging.getLogger(__name__)


class AdvecDiffParamsMixin(ParamsMixin):
    def __init__(self):
        super(AdvecDiffParamsMixin, self).__init__()
        self._params.update({
            'nu': ValueParameter(long='nu'),
            'vel': ValueParameter(long='vel')
        })

    @property
    def nu(self):
        return self._params['nu']

    @property
    def vel(self):
        return self._params['vel']


class AdvecDiff(Example, AdvecDiffParamsMixin):
    def __init__(self):
        super(AdvecDiff, self).__init__()
