# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
from pfasst_py.util import log

import logging
import sys

_log = logging.getLogger('pfasst_py')

if not (sys.version_info.major >= 3 and sys.version_info.minor >= 5):
    _log.critical("At least Python 3.5.0 is required.")
    raise RuntimeError("At least Python 3.5.0 is required.")
