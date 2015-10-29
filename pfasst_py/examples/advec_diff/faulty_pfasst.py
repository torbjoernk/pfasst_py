# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.examples.example import Example
from pfasst_py.runner.parameters.faulty_pfasst_params_mixin import FaultyPfasstParamsMixin

_log = logging.getLogger(__name__)


class AdvecDiffFaultyPfasstExample(Example, FaultyPfasstParamsMixin):
    def __init__(self, exe):
        super(AdvecDiffFaultyPfasstExample, self).__init__(exe)
