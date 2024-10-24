import datetime
import frontmatter
import mistune

from renderables import Renderable


class Note(Renderable):
    def __init__(
        self,
        site,
        name="dummy",
        title="Dummy",
        content="",
        year=2021,
        month=1,
        day=1,
        tags=[],
    ):
        super().__init__(site)
        self.tags = site.tags.get_tags(tags)

        self.name = name
        self.title = title
        self.content_raw = content
        self.content_html = mistune.html(content)

        self.year = year
        self.month = month
        self.day = day
        self.date = datetime.date(year, month, day)

        self.location = f"{self.year}/{self.name}"

    @classmethod
    def from_file(cls, site, year, file):
        with open(file) as f:
            meta, content = frontmatter.parse(f.read())

        return cls(site, content=content, year=year, **meta)
