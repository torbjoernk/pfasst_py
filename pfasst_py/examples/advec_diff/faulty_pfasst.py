# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.examples.example import Example
from pfasst_py.runner.parameters.faulty_pfasst_params_mixin import FaultyPfasstParamsMixin
from pfasst_py.examples.advec_diff.advec_diff import AdvecDiffExecutable
from pfasst_py.runner.executable import MPIExec
from pfasst_py.runner.runner import Runner
from pfasst_py.runner.wrapper import Wrapper

_log = logging.getLogger(__name__)


class AdvecDiffFaultyPfasstExample(Example, FaultyPfasstParamsMixin):
    def __init__(self, *args, **kwargs):
        super(AdvecDiffFaultyPfasstExample, self).__init__(*args, **kwargs)

        self.use_default_exe()

    def use_default_exe(self):
        if self.directory:
            try:
                mpi = Wrapper(MPIExec())
                mpi.wrapped = AdvecDiffExecutable(exe=(self.directory / 'advec_diff_faulty_pfasst'))
                self.runner = Runner(mpi)
            except ValueError as err:
                _log.error("Cannot create Executable for example: %s" % err)
        else:
            _log.warning("Example directory not set. Cannot find executable.")
