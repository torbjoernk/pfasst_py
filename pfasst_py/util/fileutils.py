# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging
import os
import pathlib
import re
import shutil
import subprocess as sp

_log = logging.getLogger(__name__)


def get_exe_path(executable):
    path = pathlib.Path(executable)
    builtin = False

    if path.is_absolute():
        _log.debug("given absolute path of executable")
    elif len(path.parts) == 1:
        _log.debug("resolving executable via PATH")
        exepath = shutil.which(path.as_posix())
        if exepath is None:
            out = sp.run("type %s" % path.as_posix(), shell=True, universal_newlines=True, stdout=sp.PIPE, check=False).stdout.strip()
            if out == "%s is a shell builtin" % path.as_posix():
                _log.debug("%s is a shell built-in command" % executable)
                path = pathlib.Path(executable)
                builtin = True
            else:
                _log.error("Cannot resolve executable '%s': %s" % (executable, out))
                raise ValueError("Cannot resolve executable '%s': %s" % (executable, out))
        else:
            path = pathlib.Path(exepath)
    else:
        _log.debug("resolving relative path of executable")
        try:
            path = path.resolve()
        except FileNotFoundError:
            _log.error("Cannot resolve executable from relative path: %s" % executable)
            raise ValueError("Cannot resolve executable from relative path: %s" % executable)

    if builtin or (path.exists() and os.access(path.as_posix(), os.X_OK)):
        return path
    else:
        _log.error("Given executable not found or not executable: %s" % path.as_posix())
        raise ValueError("Given executable not found or not executable: %s" % path.as_posix())


def get_directory_path(directory):
    path = pathlib.Path(directory)

    if path.is_absolute():
        _log.debug("given directory is absolute path")
    else:
        _log.debug("resolving absolute path of directory from given relative path")
        path = path.resolve()

    if path.exists() and path.is_dir():
        return path
    else:
        _log.error("Given directory not found or not a directory: %s" % path.as_posix())
        raise ValueError("Given directory not found or not a directory: %s" % path.as_posix())
