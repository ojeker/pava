import importlib.resources
import shutil
from unittest import TestCase
import logging
from pathlib import PurePath, Path
import os.path

from pavalib.util import util
import tempfile

log = logging.getLogger(__name__)


class Test(TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)

    def test_filename_from_url_ok(self):
        base = 'https://github.com/ojeker/pava-jre/raw/main/v11/'
        file = 'OpenJDK11U-jre_x64_linux_hotspot_11.0.22_7.tar.gz'

        file2 = util.filename_from_url(base + file)
        log.debug('filename: {}'.format(file2))
        self.assertEqual(file, file2)

    def test_copy_chunked_ok(self):
        base = 'https://raw.githubusercontent.com/ojeker/pava/main/res_mock/'
        file = 'app.java'

        with tempfile.TemporaryDirectory() as td:
            util.copy_chunked(
                base + file,
                PurePath(td)
            )
            expected = PurePath(td).joinpath(file)
            self.assertTrue(os.path.isfile(expected), "File '{}' was not downloaded".format(expected))

    def test_unpack_to_dir_tar(self):
        dir_created = self._unpack_creates_dir('test_res', 'tarred.tar')
        self.assertTrue(dir_created, 'dir for file "tarred.tar not created')

    def test_unpack_to_dir_zip(self):
        dir_created = self._unpack_creates_dir('test_res', 'zipped.zip')
        self.assertTrue(dir_created, 'dir for file "zipped.zip not created')

    def test_unpack_to_dir_tar_xz(self):
        dir_created = self._unpack_creates_dir('test_res', 'tarred.tar.xz')
        self.assertTrue(dir_created, 'dir for file "tarred.tar.xz not created')

    @classmethod
    def _unpack_creates_dir(cls, res_anchor: str, file_name: str):
        dir_created = False
        fptr = importlib.resources.files(res_anchor).joinpath(file_name)
        with tempfile.TemporaryDirectory() as tdir:
            tdir = Path(tdir)
            archive = tdir.joinpath(file_name)
            with importlib.resources.as_file(fptr) as res_file:
                shutil.copy2(res_file, archive)
            util.unpack_to_archive_dir(archive)
            dir_created = tdir.joinpath(archive.stem).is_dir()
        return dir_created
