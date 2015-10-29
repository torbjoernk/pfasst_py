# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import os
import pathlib
import tempfile


def read_data_file(filename):
    filepath = pathlib.Path(__file__).absolute().parent /'data' / filename
    if filepath.exists():
        with open(filepath.as_posix(), mode='r') as fh:
            content = fh.read()
        return content
    else:
        raise OSError("Cannot find file: %s" % filepath.as_posix())


class TestDir(object):
    __test__ = False

    def __init__(self):
        self._tempdir = tempfile.TemporaryDirectory(prefix='pfasstpy-', suffix='-test')

    @property
    def tmpdir(self):
        return self._tempdir.name

    def create_testfile(self, filename=None, content=None):
        if filename:
            file = os.path.join(self.tmpdir, filename)
        else:
            fd, file = tempfile.mkstemp(dir=self.tmpdir, text=True)
            os.close(fd)

        if not content:
            content = "This is a Test file"

        with open(file, mode='w', encoding='UTF-8') as fh:
            fh.write(content)

        return file
