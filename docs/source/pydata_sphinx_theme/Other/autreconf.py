# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys
from pathlib import Path
from typing import Any, Dict

from sphinx.application import Sphinx
from sphinx.locale import _

import pydata_sphinx_theme

sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Auto Apprentissage'
copyright = '2024, John GABARY'
author = 'John GABARY'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.autosummary',
    'sphinx.ext.extlinks',
    'sphinx.ext.graphviz',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.httpdomain',
    'numpydoc', 
    'sphinx_intl',
    'sphinx_tabs.tabs',
]

# Configuration pour la galerie Sphinx
#sphinx_gallery_conf = {
#    'examples_dirs': 'exemples',   # répertoire où se trouvent vos exemples
#    'gallery_dirs': 'auto_exemples',  # répertoire où la galerie sera générée
#    'filename_pattern': '^.+$',      # motifs de nom de fichier à inclure
#    'within_subsection_order': 'sphinx_gallery.sorting.bysource',  # ordre des fichiers dans les sections
#}

# Autres configurations...

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

#exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

exclude_patterns = []
language = 'fr'

#suppress_warnings = ['ref.ref']

# -- Options for HTML output -------------------------------------------------

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_logo = "_static/log.png"
html_favicon = "_static/log.png"
html_sourcelink_suffix = ""
html_last_updated_fmt = ""  # to reveal the build date in the pages meta


# Define the json_url for our version switcher.
#json_url = "https://pydata-sphinx-theme.readthedocs.io/en/latest/_static/switcher.json"

    
# -- sphinx_ext_graphviz options ---------------------------------------------

graphviz_output_format = "svg"
inheritance_graph_attrs = dict(
    rankdir="LR",
    fontsize=14,
    ratio="compress",
)

html_theme_options = {
    # "external_links": [
    #     {
    #         "url": "https://pydata.org",
    #         "name": "PyData Website",
    #     },
    #     {
    #         "url": "https://numfocus.org/",
    #         "name": "NumFocus",
    #     },
    #     {
    #         "url": "https://numfocus.org/donate",
    #         "name": "Donate to NumFocus",
    #     },
    #],
    "header_links_before_dropdown": 4,
    "icon_links": [
        {
            "name": "Twitter",
            "url": "https://twitter.com/PyData",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/JohnGAB7",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "facebook",
            "url": "https://www.facebook.com/NivekJGL/",
            "icon": "fa-brands fa-facebook",
        },
        {
            "name": "Instagram",
            "url": "https://pydata.org",
            "icon": "fa-brands fa-instagram",
        },
    ],
    # alternative way to set twitter and github header icons
    # "github_url": "https://github.com/pydata/pydata-sphinx-theme",
    # "twitter_url": "https://twitter.com/PyData",
    "logo": {
        "text": "AUTO APPRENTISSAGE",
        "image_dark": "_static/logo.svg",
    },
    "use_edit_page_button": True,
    "show_toc_level": 1,
    "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    # "show_nav_level": 2,
    "announcement": "Bienvenue sur ma page destinée à l'apprentissage de logiciel pour Data Scientist",
    "show_version_warning_banner": True,
    #"navbar_center": ["version-switcher", "navbar-nav"],
    # "navbar_start": ["navbar-logo"],
    # "navbar_end": ["theme-switcher", "navbar-icon-links"],
    # "navbar_persistent": ["search-button"],
    # "primary_sidebar_end": ["custom-template", "sidebar-ethical-ads"],
    # "article_footer_items": ["test", "test"],
    # "content_footer_items": ["test", "test"],
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-version"],
    "secondary_sidebar_items": {
        "**/*": ["page-toc", "edit-this-page", "sourcelink"],
        "examples/no-sidebar": [],
    },
    # "switcher": {
    #     "json_url": json_url,
    #     "version_match": version_match,
    #},
    # "back_to_top_button": False,
}


# -- Localization settings ---------------------------------------------------
locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.


# -- Extension configuration -------------------------------------------------

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Autodoc settings
autodoc_member_order = 'bysource'
autodoc_typehints = 'description'

# Todo settings
todo_include_todos = True

# MathJax settings
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'

# Intersphinx settings
#intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# Autosummary settings
autosummary_generate = True


# Graphviz settings
graphviz_output_format = 'svg'

# PlantUML settings
plantuml = 'java -jar /path/to/plantuml.jar'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp',
}

# -- Options for manual page output ------------------------------------------
# Define the main document file (typically index.rst)
master_doc = 'index'

man_pages = [
    (master_doc, 'Programmer avec Python', 'Nom du Projet Documentation',
     ['John GABARY'], 1)
]

# -- Options for Texinfo output ----------------------------------------------

texinfo_documents = [
    (master_doc, 'Programmer avec Python', 'Documentation',
     'John GABARY', 'Programmer avec Python', 'One line description of project.',
     'Miscellaneous')
]

# -- Options for Epub output -------------------------------------------------

epub_title = project
epub_exclude_files = ['search.html']

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp',
}

master_doc = 'index'  # Assurez-vous que cela pointe vers votre document principal
