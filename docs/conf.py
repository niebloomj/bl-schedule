"""Sphinx configuration."""
from datetime import datetime


project = "BL Schedule"
author = "Baruch Niebloom"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
]
autodoc_typehints = "description"
html_theme = "furo"
