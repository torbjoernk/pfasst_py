# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
# from itertools import chain
import logging

from pfasst_py.runner.runner import Runner
from pfasst_py.runner.parameters import GlobalParamsMixin

_log = logging.getLogger(__name__)


class Example(Runner, GlobalParamsMixin):
    def __init__(self, exe=None):
        super(Example, self).__init__(exe)
