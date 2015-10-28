# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging
import os
import pathlib
import shutil

_log = logging.getLogger(__name__)


def get_exe_path(executable):
    path = pathlib.Path(executable)

    if path.is_absolute():
        _log.debug("given absolute path of executable")
    elif len(path.parts) == 1:
        _log.debug("resolving executable via PATH")
        try:
            path = pathlib.Path(shutil.which(executable))
        except TypeError:
            _log.error("Cannot resolve executable via PATH: %s" % executable)
            raise ValueError("Cannot resolve executable via PATH: %s" % executable)
    else:
        _log.debug("resolving relative path of executable")
        try:
            path = path.resolve()
        except FileNotFoundError:
            _log.error("Cannot resolve executable from relative path: %s" % executable)
            raise ValueError("Cannot resolve executable from relative path: %s" % executable)

    if path.exists() and os.access(path.as_posix(), os.X_OK):
        return path
    else:
        _log.error("Given executable not found or not executable: %s" % path.as_posix())
        raise ValueError("Given executable not found or not executable: %s" % path.as_posix())
