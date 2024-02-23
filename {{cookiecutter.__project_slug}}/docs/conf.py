# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import datetime
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '{{cookiecutter.__project_slug}}'
copyright = f'{datetime.datetime.now().year}, {{cookiecutter.author}}'
author = '{{cookiecutter.author}}'

from importlib.metadata import version as get_version
release: str = get_version(project)
# for example take major/minor
version: str = ".".join(release.split('.')[:2])


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'sphinx.ext.autodoc',
  'sphinx.ext.autosummary',
	'sphinx.ext.viewcode',  # Add a link to the Python source code for classes, functions etc.
	'numpydoc',# numpy style docstring parser
	'myst_parser',
	"sphinx_autodoc_typehints"
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_theme_options = {
  # Navbar
  "github_url": "",
  "navbar_end": ["navbar-icon-links"],
  # General config
  "collapse_navigation": True,
}