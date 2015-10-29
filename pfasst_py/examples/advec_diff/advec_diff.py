# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.kaltt@fz-juelich.de>
"""
import logging

from pfasst_py.runner.executable import Executable
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


class AdvecDiffExecutable(Executable, AdvecDiffParamsMixin):
    def __init__(self, *args, **kwargs):
        super(AdvecDiffExecutable, self).__init__(*args, **kwargs)
