# `examples/notes/`

This is a stripped down version of the code that powers [notes.marcel.science](https://notes.marcel.science), a minimal technical blog written with `renderables`. One makes a `.md` file in a folder per year. You can only make a post a day!

Note: This example requires the `python-frontmatter` and `mistune` packages.

- `site/` contains the *content* of the page, i.e., the `environments/` (i.e. the "recipe" of how to render certain items), the `plan/` (roughly, the template for the overall page), and `years/`, the place where all the actual content goes. Some additional `.yaml` config files are provided.
- `notes/` contains the library code to actually make the site

Use: `python main.py` will yield a built bage in `site/_build`. Happy hacking!

