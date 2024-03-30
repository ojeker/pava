from unittest import TestCase
from pavalib.pava import Pava


class TestPava(TestCase):
    def test_home_path(self):
        full_path = Pava().home_path.name
        self.assertTrue(full_path.endswith(Pava().homedir_name), "home_path must end with dir name. homedir: {}".format(full_path))
