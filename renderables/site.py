import yaml

from pathlib import Path
import datetime

from .tags import Tags
from .plan import Plan
from .environments import Environments


class Site:
    def __init__(self, folder):
        self.folder = Path(folder)

        with open(self.folder / "config.yaml") as stream:
            self.config = yaml.safe_load(stream)

        self.title = self.config["title"]
        self.url = self.config["url"]
        self.description = self.config.get("description", "")

        self.plan = Plan(self)
        self.environments = Environments(self)

    def render(self):
        self.plan.prepare()
        self._render()
