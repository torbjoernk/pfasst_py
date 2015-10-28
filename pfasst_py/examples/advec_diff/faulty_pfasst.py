# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.examples.example import Example
from pfasst_py.runner.parameters import FaultyPfasstParamsMixin

_log = logging.getLogger(__name__)


class AdvecDiffFaultyPfasstExample(Example, FaultyPfasstParamsMixin):
    def __init__(self, exe):
        super(AdvecDiffFaultyPfasstExample, self).__init__(exe)

    def add_reset(self, proc, self_step, iteri):
        if isinstance(proc, int):
            proc = (proc, )
        if isinstance(self_step, int):
            self_step = (self_step, )
        if isinstance(iteri, int):
            iteri = (iteri, )

        assert(len(proc) == len(self_step) == len(iteri))

        if 'tend' in self._args.keys() \
                and 'dt' in self._args.keys() \
                and 'num_iters' in self._args.keys() \
                and self._runner.is_mpi \
                and self._runner.np:
            tend = self._args['tend']
            dt = self._args['dt']
            num_iters = self._args['num_iters']
            np = self._runner.np
            nsteps = tend / dt
            resets = []

            for i in range(0, len(proc)):
                step = (self_step[i] - 1) * np + proc[i]
                resets += (proc, step, iteri[i])

            # self.add_parameter('reset', ','.join(['-'.join(reset) for reset in resets]))

        else:
            _log.error("'tend', 'dt' and 'num_iters' must be present as well as number procs.")
            raise RuntimeError("'tend', 'dt' and 'num_iters' must be present as well as number procs.")
