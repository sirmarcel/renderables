import yaml
import datetime
from renderables import Renderable

from .link import Link


class Week(Renderable):
    def __init__(self, site, year, number, links):
        super().__init__(site)

        self.year = year
        self.site = site
        self.number = int(number)

        self.links = [Link(site, **link_dict) for link_dict in links]

    @classmethod
    def from_file(cls, site, year, file):
        number = file.stem
        with open(file, "r") as stream:
            links = yaml.safe_load(stream)
        return cls(site, year, number, links)

    @property
    def date(self):
        year = self.year.number
        week = self.number
        return datetime.datetime.strptime(f"{year}-{week:02d}" + "-1", "%Y-%W-%w")
