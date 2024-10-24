from renderables import Renderable


class Link(Renderable):
    def __init__(self, site, title, url, tags=[], via=None):
        super().__init__(site)

        self.tags = site.tags.get_tags(tags)
        self.title = title
        self.url = url
