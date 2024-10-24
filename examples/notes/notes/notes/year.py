from pathlib import Path

from renderables import Renderable
from .note import Note


class Year(Renderable):
    def __init__(self, site, number, weeks=[]):
        self.site = site
        self.number = int(number)
        self.weeks = weeks

    @classmethod
    def from_folder(cls, site, folder):
        folder = Path(folder)
        number = folder.stem
        year = cls(site, number)

        notes = [Note.from_file(site, year.number, file) for file in folder.glob("*.md")]

        year.notes = list(sorted(notes, key=lambda note: -note.month))

        return year

    @property
    def updated(self):
        return self.years[0].notes[0].date
