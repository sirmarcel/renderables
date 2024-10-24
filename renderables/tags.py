import yaml

from .renderable import Renderable


class Tag:
    def __init__(self, name, title, emoji, slug):
        self.name = name
        self.title = title
        self.emoji = emoji
        self.slug = slug


class Tags(Renderable):
    def __init__(self, site, tags=[]):
        self.site = site
        self.tags = tags

    @property
    def by_name(self):
        return {tag.name: tag for tag in self.tags}

    def __getitem__(self, key):
        return self.by_name.get(key, None)

    def __len__(self):
        return len(self.by_name.keys())

    def to_str(self):
        if len(self) > 0:
            emojis = " ".join([tag.emoji for tag in self.tags])
            return f"({emojis})"
        else:
            return ""

    def get_tags(self, args):
        filtered = []

        for a in args:
            res = self[a]
            if res is not None:
                filtered.append(res)

        return Tags(self.site, tags=filtered)

    @classmethod
    def from_file(cls, site, file):
        with open(file, "r") as stream:
            raw_tags = yaml.safe_load(stream)
        tags = [Tag(**d) for d in raw_tags]
        return cls(site, tags)
