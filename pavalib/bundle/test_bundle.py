from unittest import TestCase
import tempfile
from pathlib import PurePath

from pavalib.bundle.bundle import Bundle


class TestBundle(TestCase):
    def test_init_valid_ok(self):
        dic = {'distro': 'https://geo.so.ch/distro.jar', 'app': 'https://geo.so.ch/app.jar'}
        bundle = Bundle(dic)
        self.assertEqual(dic.get('distro'), bundle.distro)
        self.assertEqual(dic.get('app'), bundle.app)

    def test_init_invalid_throws(self):
        dic = {'distro': 'https..//geo.so.ch/distro.jar', 'app': 'https://geo.so.ch/app.jar'}
        self.assertRaises(AssertionError, lambda: Bundle(dic))

    def test_for_file_ok(self):
        filename = None
        with tempfile.NamedTemporaryFile() as fp:
            fp.write(b'{"distro": "https://geo.so.ch/distro.jar", "app": "https://geo.so.ch/app.jar"}')
            fp.flush()
            bundle = Bundle.for_file(PurePath(fp.name))
            self.assertEqual("https://geo.so.ch/distro.jar", bundle.distro)




"""
    def test_name_valid(self):
        name = "0-my_bundle__5"
        bundle = Bundle(name)
        self.assertEqual(name, bundle.name)

    def test_name_invalid(self):
        name = "my$bundle"
        self.assertRaises(BaseException, lambda: Bundle(name))
"""

