from pathlib import Path
import shutil
from itertools import chain

from mako.template import Template
from mako.lookup import TemplateLookup


class Plan:
    def __init__(self, site):
        self.site = site
        self.folder = site.folder / "plan"
        self.lookup = TemplateLookup(directories=[self.folder])

    def prepare(self):
        print("Preparing build...")
        outfolder = self.site.folder / "_build"
        outfolder.mkdir(exist_ok=True)
        shutil.rmtree(outfolder)

        self.outfolder = outfolder

    def copy_folder(self, folder, target=None):
        if target is None:
            target = folder

        shutil.copytree(self.folder / folder, self.outfolder / target)

    def render_template(self, template, outfile=None, **kwargs):
        template_path = Path(template)
        template = self.lookup.get_template(str(template_path))
        if outfile is None:
            outfile = template_path
        else:
            outfile = Path(outfile)

        outfile = self.outfolder / outfile
        # ensure we can write the rendered result somewhere valid
        outfile.parents[0].mkdir(exist_ok=True, parents=True)

        with open(outfile, "wb") as f:
            f.write(template.render(site=self.site, **kwargs).encode("utf-8"))
