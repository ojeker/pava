import re
import json
import validators
from pathlib import PurePath

class Bundle:

    @classmethod
    def for_file(cls, path: PurePath):
        dic = None
        with open(path, 'r', encoding='utf-8') as f:
            dic = json.load(f)
        return Bundle(dic)

    def __init__(self, data: dict):
        self.distro = data.get('distro')
        self.app = data.get('app')
        assert validators.url(self.distro), "distro must be a valid url"
        assert validators.url(self.app), "app must be a valid url"

    def load_to_cache(self):
        return None

    def _validate(self):
        return None

    def is_cached(self):
        return None


"""
    def validate(self):
        valid_name = bool(re.compile('^[A-Za-z0-9\-_]+$').match(self.name))
        assert valid_name, "Name must not contain special characters except '_' and '-'. Name: '{}'".format(self.name)

ablauf

Bundle configurieren (json)
bundle config laden
bundle distro und jar laden, falls noch nicht vorhanden

"""