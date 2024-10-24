# `examples/tabs/`

This is a stripped down version of the code that powers [tabs.marcel.computer](https://tabs.marcel.computer), a minimal link blog written with `renderables`. The idea is that one makes a `.yaml` file for every week of the year, containing some links. They are then rendered as a list, with associated tags, and an Atom feed. That's it!

- `site/` contains the *content* of the page, i.e., the `environments/` (i.e. the "recipe" of how to render certain items), the `plan/` (roughly, the template for the overall page), and `years/`, the place where all the actual content goes. Some additional `.yaml` config files are provided.
- `tabslog/` contains the library code to actually make the site

Use: `python main.py` will yield a built bage in `site/_build`. Happy hacking!