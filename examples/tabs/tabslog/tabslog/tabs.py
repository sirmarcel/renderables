import yaml
import datetime

from renderables import Site

from .tags import Tags
from .year import Year


class Tabs(Site):
    def __init__(self, folder):
        super().__init__(folder)

        self.tags = Tags.from_file(self, self.folder / "tags.yaml")
        years = [
            Year.from_folder(self, f) for f in list((self.folder / "years").glob("*"))
        ]
        self.years = sorted(years, key=lambda year: -year.number)

    def _render(self):
        self.plan.copy_folder("static", target="")
        print("Copied static.\nRendering...")

        self.plan.render_template("index.html")
        self.plan.render_template("atom.xml")

    @property
    def updated(self):
        year = self.years[0].number
        week = self.years[0].weeks[0].number

        return datetime.datetime.strptime(f"{year}-{week:02d}" + "-1", "%Y-%W-%w")
