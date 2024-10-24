class Renderable:
    def __init__(self, site):
        self.site = site
        self.environments = site.environments

    def render(self, environment):
        kind = self.__class__.__name__.lower()
        template = self.environments[environment].get_template(kind + ".html")
        return template.render_unicode(environment=environment, **{kind: self})
