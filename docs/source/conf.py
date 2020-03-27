# Configuration file for the Sphinx documentation builder.
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
from pathlib import Path
import warnings
from datetime import datetime
sys.setrecursionlimit(1500)
HERE = Path(__file__).parent
sys.path[:0] = [str(HERE.parent), str(HERE / 'extensions')]
import sphinx_bootstrap_theme
from recommonmark.parser import CommonMarkParser


def setup(app):
    app.add_stylesheet("style.css") # also can be a full URL
    app.add_stylesheet("animate.min.css") # also can be a full URL
    app.add_stylesheet("font-awesome.css") # also can be a full URL
    app.add_stylesheet("venobox.css") # also can be a full URL
    app.add_stylesheet("fontfamily.css") # also can be a full URL
    app.add_javascript("custom.js")
    app.add_javascript("main.js")
    app.add_javascript("animate.min.js")
    app.add_javascript("boostrap.bundle.min.js")
    app.add_javascript("font-awesome.js")
    app.add_javascript("hoverIntent.js")
    app.add_javascript("jquery.easing.min.js")
    app.add_javascript("jquery.min.js")
    app.add_javascript("superfish.min.js")
    app.add_javascript("validate.js")
    app.add_javascript("venobox.js")
    app.add_javascript("wow.min.js")
    app.add_config_value('markdown_parser_config', {
        'auto_toc_tree_section': 'Content',
        'enable_auto_doc_ref': True,
        'enable_auto_toc_tree': True,
        'enable_eval_rst': True,
        'enable_inline_math': True,
        'enable_math': True,
    }, True)

# -- Project information -----------------------------------------------------

project = 'Statistical Sauce'
copyright = '2020, Rahul Bhadani'
author = 'Rahul Bhadani'


# The full version, including alpha/beta/rc tags
release = '1.0'

# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.doctest', 'sphinx.ext.todo', 'sphinx.ext.coverage',
    'sphinx.ext.mathjax', 'sphinx.ext.ifconfig', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon', 'sphinx.ext.autosummary', 'sphinx_autodoc_typehints',  # needs to be after napoleon
    'sphinx_rtd_theme', 'recommonmark']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
# Path should be relative to the ``_static`` files directory.
html_logo = "../../violin.png"

html_favicon = "favicon.ico"

html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    'navbar_title': "Statistical Sauce",
    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Site",

    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "Page",

    # A list of tuples containing pages or urls to link to.
    # Valid tuples should be in the following forms:
    #    (name, page)                 # a link to a page
    #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
    #    (name, "http://example.com", True) # arbitrary absolute url
    # Note the "1" or "True" value above as the third argument to indicate
    # an arbitrary url.
    # 'navbar_links': [
    #     ("Examples", "examples"),
    #     ("Link", "http://example.com", True),
    # ],

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 2,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "nav",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing (default) or the name of a valid theme such
    # such as "cosmo" or "sandstone".
    #
    # Example themes:
    # * flatly
    # * sandstone (v3 only)
    # * united
    # * yeti (v3 only)
    'bootswatch_theme': "journal",

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    'bootstrap_version': "3",
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'statsuace.tex', u'Statistical Sauce',
     u'Rahul Bhadani', 'manual'),
]


