## Les Rendérables

### *a starting point for your very own static site generator*

`renderables` is a comically minimal python library that can serve as a starting point for writing one-off static site generators. (A static site generator is a program that generates a set of files that constitute a "static" website. Static websites are simply websites that don't make use of any programming on the side of the web server, so they're very simple and cheap to host, and easily portable.) Building on `renderables`, you can write [toy blogging engines](https://notes.marcel.science) or little [weekly link logs](https://tabs.marcel.computer), or do just about anything that requires outputting HTML, but is too weird to work with more fully featured static site generators. (Personally, I'm a big fan of [`jekyll`](https://jekyllrb.com) if you need something professional and mature. [`middleman`](https://middlemanapp.com) is also nice.)

With modern HTML and CSS, it's surprisingly straightforward to create beautiful websites, why not give it a try!

The `examples/` folder contains some starting points: The code that runs [tabs.marcel.computer](https://tabs.marcel.computer) (a small link blog) and the code that runs [notes.marcel.science](https://notes.marcel.science) (a small blog).

### Technical stuff

`renderables` is nothing you couldn't write yourself in about half a day of work. But maybe, using it can save you that half a day! At it's core, it's basically some scaffolding on top of the extremely powerful [`mako`](https://www.makotemplates.org) templating engine, of which I'm using about 1% of the features, and probably in entirely the wrong way.

`renderables` is built on the assumption that you have a `site` directory (name doesn't matter) that looks like this:

```
site
	/config.yaml
	/environments
		/some_name
			entry.html
			tag.html
			...
	/plan
		index.html
		something.html
		...
	(whatever other content you want to process goes here)

```

It then defines a `Site` class that you can subclass as needed, which takes this folder as initialisation argument. The `Site` in turn instantiates a `Plan` and `Environments`. The `Plan` represents the blueprint for building the page, and `Environments` is responsible for looking up templates. You can define a class hierarchy for your content as needed; things that need to appear on the website can subclass `Renderable`, which provides the following functionality: if `.render(some_name)` is called, `renderables` tries to find a `mako` template in `site/environments/some_name/classname.html`, and renders it, passing `classname=instance` as argument to `mako`'s rendering functionality.

I know this is a mouthful, but it basically means that you can define HTML representations of arbitrary classes that depend on context, i.e. a blog post can appear in a condensed form on your index page, and then in an expanded form when you actually view the post.

Calling `site.render()` will crate a `_build` directory in `site`, and do nothing else -- you'll have to implement a `site._render()` method yourself in a suitable subclass, and take care of actually getting content to render. `site.plan` exposes a `copy_folder` method to wholesale copy things from your `site` to `_build`, and `render_template` can be used to explicitly render a template. Good luck!

The `examples` folder shows how to create a weekly link blog like [`tabs.marcel.computer`](https://tabs.marcel.computer), and may be a lot more instructive than the above text. :-)

Good luck! Make your own website! Keep the internet weird! ‡

### Installation

`git clone` this repository, run `pip install -e .`. Start hacking!
