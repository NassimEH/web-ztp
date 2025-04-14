import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'ZTP Manager'
copyright = '2024, ZTP Manager Team'
author = 'ZTP Manager Team'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'sphinx_design',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_book_theme'
html_theme_options = {
    'repository_url': 'https://github.com/yourusername/ztp-manager',
    'use_repository_button': True,
    'use_edit_page_button': True,
    'use_issues_button': True,
    'use_download_button': True,
    'home_page_in_toc': True,
    'show_navbar_depth': 2,
    'show_toc_level': 2,
    'logo_only': True,
}

html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']

html_logo = '_static/logo.png'
html_favicon = '_static/favicon.ico'

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_type_aliases = None 