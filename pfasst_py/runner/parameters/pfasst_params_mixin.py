# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.runner.parameters.mlsdc_params_mixin import MLSDCParamsMixin

_log = logging.getLogger(__name__)


class PfasstParamsMixin(MLSDCParamsMixin):
    def __init__(self):
        super(PfasstParamsMixin, self).__init__()
