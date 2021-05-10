# ISTD Student Board Website

This website aims to document student initiatives and resources for the ISTD student board. Adding new pages is easy, just follow this guide!

## Contributing

If you found a mistake in the site, please [raise an issue on Github](https://github.com/OpenSUTD/ISTD/issues).

If you wish to add new pages, or change the look of the site, please raise PR with the following guide.

## Adding content-only pages with Markdown

With the help of [Jekyll](https://jekyllrb.com/), adding new pages is as simple as creating a new Markdown file.

What to do:
- Fork this repository.
- Create a new markdown file with the appropriate file name and path.
  - If you create a file `mypage.md` in the _root_ directory of this project, your page will be accessible at `istd.opensutd.org/mypage.html`
  - If you create a file named `mystuff/index.md`, your page will be accessible at `istd.opensutd.org/mystuff`
  - If you create a file named `mystuff/somestuff.md`, your page will be accessible at `istd.opensutd.org/mystuff/somestuff.html`.
- Open a Pull Request to merge your changes into this main repository. We will review your changes and merge if it is appropiate.

Note that this allows you to only add content-only pages, with little to no control over the rest of the page (header, footer) but this should suffice for most use cases.

## Previewing your changes before you submit your PR

It is highly recommended to develop locally on your computer to preview the changes before you submit your PR to us. To do so:

- Follow the Ruby + RubyGems + Jekyll install guide [here](https://jekyllrb.com/docs/installation/)
- Install [Bundler](https://bundler.io/) and add to PATH
- Clone _your fork of the repository_ to your computer
- `bundler install` in the root of the project.

## Adding custom CSS to your page

We made 3 ways to include CSS using [front matter]() on your markdown file:

- "Global" CSS: Use the `css:` front matter in your markdown file to include a list of files from the `assets/css` directory, without the file extensions. This directory is usually reserved for site-wide stylesheets.
- "Local" CSS: Use the `local_css:` front matter to include a list of files from the same directory as your page. Usually used if you need "one-off" stylesheets.
- Remote CSS: Use the `remote_css` to load remote stylesheets served over a CDN, such as Font Awesome.

You can create normal CSS files, or use SCSS. Jekyll automatically compiles `.scss` files **that begin with a front matter declaration**.


### Totally custom pages
If you need a totally custom page, just upload the full .HTML file. It will not inherit any styles or templates.
