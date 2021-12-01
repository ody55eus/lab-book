# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# -- Project information -----------------------------------------------------

project = 'Lab Book'
copyright = '2020, Jonathan Pieper'
author = 'Jonathan Pieper'

# The full version, including alpha/beta/rc tags
version = '0.3'
release = '0.3.0rc'

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

rst_epilog = """
.. |sa| replace:: signal analyzer
.. |spa| replace:: spectrumanalyzer
.. |ana| replace:: Ana
.. |LabBook| replace:: Lab Book

"""
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'recommonmark',
    'nbsphinx',
             ]

nbsphinx_allow_errors = True

todo_include_todos = True

autoclass_content = 'both'
add_module_names = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Number figures, tables and code-blocks are automatically if they have a caption. 
# The numref role is enabled. Obeyed so far only by HTML and LaTeX builders. Default is False.
numfig = True
numfig_format = {'figure':'Fig. %s',
                 'table':'Table %s',
                 'code-block':'Listing %s',
                 'section':'Section'}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# 'alabaster', "classic", 'sphinxdoc', 'traditional', 'nature', 'haiku', 'pyramid', 'bizstyle'
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_favicon = 'favicon.ico'

html_sidebars = {
   '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
   'using/windows': ['windowssidebar.html', 'searchbox.html'],
}
