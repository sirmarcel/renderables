from pathlib import Path
import shutil
from itertools import chain

from mako.template import Template
from mako.lookup import TemplateLookup


class Environments:
    def __init__(self, site):

        self.environments = {
            f.stem: TemplateLookup(directories=[f])
            for f in (site.folder / "environments").glob("*")
        }

    def __getitem__(self, attr):
        return self.environments[attr]
