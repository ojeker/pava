from os.path import expanduser
from pathlib import PurePath


class Pava:
    _version = 0
    _dir_prefix = ".pava"

    @property
    def home_path(self):
        home = PurePath(expanduser("~"))
        pava = home.joinpath(self.homedir_name)
        return pava

    @property
    def homedir_name(self):
        return "{}_v{}".format(self._dir_prefix, self._version)


pava = Pava()
