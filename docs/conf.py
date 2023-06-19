# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import os
import sys
import datetime

sys.path.insert(0, os.path.abspath(".."))

try:
    # Inject mock modules so that we can build the
    # documentation without having the real stuff available
    from mock import Mock

    to_be_mocked = [
        'micropython',
        'machine',
    ]
    for module in to_be_mocked:
        sys.modules[module] = Mock()
        print("Mocked '{}' module".format(module))

    import micropython_sht4x
except ImportError:
    raise SystemExit("eeprom has to be importable")

# -- General configuration ------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_immaterial",
]

autodoc_preserve_defaults = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "MicroPython": ("https://docs.micropython.org/en/latest/", None),
}

# autodoc_mock_imports = ["digitalio", "busio"]
autoclass_content = "both"
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
# General information about the project.
project = "MicroPython sht4x Library"
creation_year = "2023"
current_year = str(datetime.datetime.now().year)
year_duration = (
    current_year
    if current_year == creation_year
    else creation_year + " - " + current_year
)
copyright = year_duration + "Jose D. Montoya"
author = "Jose D. Montoya"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "1.0"
# The full version, including alpha/beta/rc tags.
release = "1.0"

language = "en"
autoclass_content = "both"
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".env",
    "requirements.txt",
]

default_role = "any"
add_function_parentheses = True
pygments_style = "sphinx"
todo_include_todos = False
todo_emit_warnings = False
napoleon_numpy_docstring = False
html_baseurl = "https://micropython-sht4x.readthedocs.io/"
rst_prolog = """
.. role:: python(code)
   :language: python
   :class: highlight
.. default-literal-role:: python
"""
html_theme = "sphinx_immaterial"

html_theme_options = {
    "features": [
        "search.share",
    ],
    # Set the color and the accent color
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "purple",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "purple",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ],
    # Set the repo location to get a badge with stats
    "repo_url": "https://github.com/jposada202020/MicroPython_SHT4X/",
    "repo_name": "MicroPython SHT4X",
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/jposada202020/MicroPython_SHT4X",
        },
        {
            "icon": "fontawesome/brands/python",
            "link": "https://pypi.org/project/micropython-sht4x/",
        },
        {
            "name": "MicroPython Downloads",
            "icon": "octicons/download-24",
            "link": "https://micropython.org",
        },
    ],
}
html_favicon = "_static/favicon.ico"

# Output file base name for HTML help builder.
htmlhelp_basename = "MicroPython_Sht4x_Librarydoc"

sphinx_immaterial_custom_admonitions = [
    {
        "name": "warning",
        "color": (255, 66, 66),
        "icon": "octicons/alert-24",
        "override": True,
    },
    {
        "name": "note",
        "icon": "octicons/pencil-24",
        "override": True,
    },
    {
        "name": "seealso",
        "color": (255, 66, 252),
        "icon": "octicons/eye-24",
        "title": "See Also",
        "override": True,
    },
    {
        "name": "hint",
        "icon": "material/school",
        "override": True,
    },
    {
        "name": "tip",
        "icon": "material/school",
        "override": True,
    },
    {
        "name": "important",
        "icon": "material/school",
        "override": True,
    },
]
python_type_aliases = {
    "DigitalInOut": "digitalio.DigitalInOut",
}

object_description_options = [
    ("py:.*", dict(generate_synopses="first_sentence")),
]
# Set link name generated in the top bar.
html_title = "MicroPython SHT4X"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = ["extra_css.css"]


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "MicroPython_sht4x_Library.tex",
        "MicroPython sht4x Library Documentation",
        author,
        "manual",
    ),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        "MicroPython_sht4x_Library",
        "MicroPython sht4x Library Documentation",
        [author],
        1,
    ),
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "MicroPython_sht4x_Library",
        "MicroPython sht4x Library Documentation",
        author,
        "MicroPython_sht4x_Library",
        "One line description of project.",
        "Miscellaneous",
    ),
]
