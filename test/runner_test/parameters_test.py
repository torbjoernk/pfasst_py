# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import unittest

from pfasst_py.util.parameter import BoolParameter, ValueParameter
from pfasst_py.runner.parameters import ParamsMixin, GlobalParamsMixin, DurationParamsMixin, QuadratureParamsMixin, \
    ToleranceParamsMixin, MPIParamsMixin, \
    SDCParamsMixin, MLSDCParamsMixin, PfasstParamsMixin, FaultyPfasstParamsMixin


class GlobalParamsMixinTest(unittest.TestCase):
    def setUp(self):
        self.obj = GlobalParamsMixin()

    def test_is_params_mixin(self):
        self.assertTrue(issubclass(GlobalParamsMixin, ParamsMixin))

    def test_has_prop_quiet(self):
        self.assertIsInstance(self.obj.quiet, BoolParameter)

    def test_has_prop_log_prefix(self):
        self.assertIsInstance(self.obj.log_prefix, ValueParameter)

    def test_has_prop_nocolor(self):
        self.assertIsInstance(self.obj.nocolor, BoolParameter)

    def test_params_to_line(self):
        self.obj.nocolor.toggle()
        self.assertRegex(self.obj.params_to_line(), "--nocolor")
        self.obj.quiet.toggle()
        self.assertRegex(self.obj.params_to_line(), "--nocolor")
        self.assertRegex(self.obj.params_to_line(), "--quiet")


class DurationParamsMixinTest(unittest.TestCase):
    def setUp(self):
        self.obj = DurationParamsMixin()

    def test_is_params_mixin(self):
        self.assertTrue(issubclass(GlobalParamsMixin, ParamsMixin))

    def test_has_prop_dt(self):
        self.assertIsInstance(self.obj.dt, ValueParameter)

    def test_has_prop_tend(self):
        self.assertIsInstance(self.obj.tend, ValueParameter)

    def test_has_prop_num_steps(self):
        self.assertIsInstance(self.obj.num_steps, ValueParameter)

    def test_has_prop_num_iters(self):
        self.assertIsInstance(self.obj.num_iters, ValueParameter)


class QuadratureParamsMixinTest(unittest.TestCase):
    def setUp(self):
        self.obj = QuadratureParamsMixin()

    def test_is_params_mixin(self):
        self.assertTrue(issubclass(GlobalParamsMixin, ParamsMixin))

    def test_has_prop_num_nodes(self):
        self.assertIsInstance(self.obj.num_nodes, ValueParameter)


class ToleranceParamsMixinTest(unittest.TestCase):
    def setUp(self):
        self.obj = ToleranceParamsMixin()

    def test_is_params_mixin(self):
        self.assertTrue(issubclass(GlobalParamsMixin, ParamsMixin))

    def test_has_prop_abs_res_tol(self):
        self.assertTrue(self.obj.abs_res_tol, ValueParameter)

    def test_has_prop_rel_res_tol(self):
        self.assertTrue(self.obj.rel_res_tol, ValueParameter)


class MPIParamsTest(unittest.TestCase):
    def setUp(self):
        self.obj = MPIParamsMixin()

    def test_is_wrapper_mixin(self):
        self.assertTrue(issubclass(MPIParamsMixin, ParamsMixin))

    def test_has_prop_num_procs(self):
        self.assertIsInstance(self.obj.np, ValueParameter)


class SDCParamsMixinTest(unittest.TestCase):
    def setUp(self):
        self.obj = SDCParamsMixin()

    def test_is_global_params_mixin(self):
        self.assertTrue(issubclass(SDCParamsMixin, GlobalParamsMixin))

    def test_is_duration_params_mixin(self):
        self.assertTrue(issubclass(SDCParamsMixin, DurationParamsMixin))

    def test_is_quadrature_params_mixin(self):
        self.assertTrue(issubclass(SDCParamsMixin, QuadratureParamsMixin))

    def test_is_tolerance_params_mixin(self):
        self.assertTrue(issubclass(SDCParamsMixin, ToleranceParamsMixin))


class MLSDCParamsMixinTest(unittest.TestCase):
    def setUp(self):
        self.obj = MLSDCParamsMixin()

    def test_is_sdc_params_mixin(self):
        self.assertTrue(issubclass(MLSDCParamsMixin, SDCParamsMixin))

    def test_has_prop_coarse_factor(self):
        self.assertIsInstance(self.obj.coarse_factor, ValueParameter)


class PfasstParamsMixinTest(unittest.TestCase):
    def setUp(self):
        self.obj = PfasstParamsMixin()

    def test_is_mlsdc_params_mixin(self):
        self.assertTrue(issubclass(PfasstParamsMixin, MLSDCParamsMixin))

    def test_is_mpi_params_mixin(self):
        self.assertTrue(issubclass(PfasstParamsMixin, MPIParamsMixin))


class FaultyPfasstMixinTest(unittest.TestCase):
    def setUp(self):
        self.obj = FaultyPfasstParamsMixin()

    def test_is_pfasst_params_mixin(self):
        self.assertTrue(FaultyPfasstParamsMixin, PfasstParamsMixin)

    def test_has_prop_reset(self):
        self.assertIsInstance(self.obj.reset, ValueParameter)

    def test_can_add_valid_reset_point(self):
        self.obj.tend.value = 1.0
        self.obj.dt.value = 0.1
        self.obj.np.value = 2
        self.obj.num_iters.value = 5
        self.obj.add_reset(1, 2, 3)

    def test_requires_other_variables_for_adding_reset_point(self):
        with self.assertRaises(RuntimeError):
            self.obj.add_reset(1, 2, 3)
