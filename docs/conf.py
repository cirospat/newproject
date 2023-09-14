# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys, os

# il 13 sett 2023 copiando da https://github.com/readthedocs/sphinx_rtd_theme/blob/master/docs/conf.py ho dato questa configurazione
import re

# il 13 sett 2023 copiando da https://github.com/readthedocs/sphinx_rtd_theme/blob/master/docs/conf.py ho dato questa configurazione
from sphinx_rtd_theme import __version__ as theme_version
from sphinx_rtd_theme import __version_full__ as theme_version_full

# dal conf.py di tansignari 
import recommonmark
from recommonmark.transform import AutoStructify


on_rtd = os.environ.get('READTHEDOCS') == 'True'

sys.path.append(os.path.abspath(os.pardir))

__version__ = '1.0'



# -- General configuration -----------------------------------------------------

# source_suffix = '.rst' eliminato dal conf.py di tansignari #
master_doc = 'index'
project = 'Ciro Spataro'
copyright = '= licenza CC BY Cirospat'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

extlinks = {}



# -- Options for HTML output ---------------------------------------------------

# html_theme = 'default'   (eliminato il 13 sett 2023 in quanto la parte grafica di RTD si era rotta
# il 13 sett 2023 copiando da https://github.com/readthedocs/sphinx_rtd_theme/blob/master/docs/conf.py ho dato questa configurazione
html_theme = 'sphinx_rtd_theme'

html_static_path = ['static']

def setup(app):
    # overrides for wide tables in RTD theme
    app.add_stylesheet('theme_overrides.css') # path relative to static
  
# dal conf.py di tansignari 
from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

source_suffix = ['.rst', '.md']

extensions = ['sphinx.ext.ifconfig','sphinx_markdown_tables']

# per le extensions guarda anche https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html


"""
  You might want to uncomment the “latex_documents = []” if you use CKJ characters in your document.
  Because the pdflatex raises exception when generate Latex documents with CKJ characters.
"""
#latex_documents = []

# latex_logo = "static/cirospat.jpg"    
# html_logo = "static/cirospat.jpg"
latex_logo = "static/ciro.jpeg"
html_logo = "static/ciro.jpeg"



# Adding Custom CSS or JavaScript to a Sphinx Project: al seguente link ci sono esempi
# https://docs.readthedocs.io/en/latest/guides/adding-custom-css.html

templates_path = ['_templates']
