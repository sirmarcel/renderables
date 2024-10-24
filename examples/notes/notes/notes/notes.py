from renderables import Site

from .year import Year
from .tags import Tags

class Notes(Site):
    def __init__(self, folder):
        super().__init__(folder)
        self.tags = Tags.from_file(self, self.folder / "tags.yaml")

        years = [
            Year.from_folder(self, f) for f in list((self.folder / "years").glob("*"))
        ]
        self.years = sorted(years, key=lambda year: -year.number)

        self.latest = self.years[0].notes[0]
        self.updated = self.latest.date


    def _render(self):
        self.plan.copy_folder("static")
        print("Copied static.\nRendering...")

        self.plan.render_template("index.html")
        self.plan.render_template("atom.xml")

        for year in self.years:
            for note in year.notes:
                self.plan.render_template(
                    "note.html", outfile=f"{note.location}/index.html", note=note
                )
