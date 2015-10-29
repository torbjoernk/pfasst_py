# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging

from pfasst_py.runner.parameters.global_params_mixin import GlobalParamsMixin
from pfasst_py.runner.parameters.duration_params_mixin import DurationParamsMixin
from pfasst_py.runner.parameters.quadrature_params_mixin import QuadratureParamsMixin
from pfasst_py.runner.parameters.tolerance_params_mixin import ToleranceParamsMixin

_log = logging.getLogger(__name__)


class SDCParamsMixin(GlobalParamsMixin, DurationParamsMixin, QuadratureParamsMixin, ToleranceParamsMixin):
    def __init__(self):
        super(SDCParamsMixin, self).__init__()
