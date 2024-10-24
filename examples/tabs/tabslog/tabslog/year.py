from pathlib import Path
from renderables import Renderable

from .week import Week


class Year(Renderable):
    def __init__(self, site, number, weeks=[]):
        super().__init__(site)

        self.site = site
        self.number = int(number)
        self.weeks = weeks

    @classmethod
    def from_folder(cls, site, folder):
        folder = Path(folder)
        number = folder.stem
        year = cls(site, number)

        weeks = [
            Week.from_file(site, year, file)
            for file in reversed(sorted(folder.glob("*.yaml")))
        ]

        year.weeks = weeks

        return year
