# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <>
"""
import pathlib

from pfasst_py.examples.advec_diff.advec_diff import AdvecDiffFaultyPfasstExecutable
from pfasst_py.runner.executable import MPIExec
from pfasst_py.runner.wrapper import Wrapper
from pfasst_py.runner.runner import Runner

example_dir = pathlib.Path('/home/t.klatt/projects/PFASST/build_mpi/examples/advec_diff')
exe_file = 'advec_diff_faulty_pfasst'

exe = AdvecDiffFaultyPfasstExecutable(exe=(example_dir / exe_file))
exe.abs_res_tol.value = 1e-10
exe.dt.value = 0.05
exe.tend.value = 0.2
exe.num_iters.value = 10
exe.nocolor.toggle()

print(exe.build_cmd_line())

mpi = MPIExec()
mpi.np.value = 4

wrapper = Wrapper()
wrapper.exe = mpi
wrapper.wrapped = exe

print(wrapper.build_cmd_line())

runner = Runner()
runner.exe = wrapper
runner.run()

print(runner.stdout_lines)
