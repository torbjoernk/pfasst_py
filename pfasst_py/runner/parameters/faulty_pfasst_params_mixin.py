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
            'reset': FaultyResetParameter()
        })

    def add_reset(self, np, proc, self_step, iteri):
        if self.tend.value and self.dt.value and self.num_iters.value:
            nsteps = self.tend.value / self.dt.value

            step = (self_step - 1) * np + proc
            if step > nsteps:
                _log.warning("Reset point in step %s of proc %s will not trigger as only %s steps will be computed."
                             % (self_step, proc, nsteps))

            self.reset.add_reset((proc, step, iteri))

        else:
            _log.error("'tend', 'dt' and 'num_iters' must be present as well as number procs.")
            raise RuntimeError("'tend', 'dt' and 'num_iters' must be present as well as number procs.")

    @property
    def reset(self):
        return self._params['reset']
