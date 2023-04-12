# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Интеграция Artix-УНФ'
copyright = '2023, PashkovKV'
author = 'PashkovKV'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser','sphinx.ext.todo',]



templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'sphinx_material'
#html_theme = 'sphinx_rtd_theme'
html_theme = 'bizstyle'
#html_theme = 'classic'
#html_theme = 'agogo'
#html_theme = 'haiku'
#html_theme = 'sphinxdoc'
#html_theme = 'sizzle'
#html_theme = 'sphinx_book_theme'

html_static_path = ['_static']


#import sphinx_redactor_theme
#html_theme = 'sphinx_redactor_theme'
#html_theme_path = [sphinx_redactor_theme.get_html_theme_path()]

#import sphinx_adc_theme
#html_theme = 'sphinx_adc_theme'
#html_theme_path = [sphinx_adc_theme.get_html_theme_path()]

#import sphinx_theme_pd
#html_theme = 'sphinx_theme_pd'
#html_theme_path = [sphinx_theme_pd.get_html_theme_path()]

#import sphinx_pdj_theme
#html_theme = 'sphinx_pdj_theme'
#html_theme_path = [sphinx_pdj_theme.get_html_theme_path()]


html_theme_options = {
    'base_url': 'http://bashtage.github.io/sphinx-material/',
    'repo_url': 'https://github.com/krugersu/Global/',
    'repo_name': 'Global',
    'html_minify': True,
    'css_minify': True,
    'nav_title': 'Интеграция Artix-УНФ',
    'logo_icon': '&#xe869',
    'globaltoc_depth': 2,
    # Set the color and the accent color
    'color_primary': 'green',
    'color_accent': 'light-green',
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,

}

html_sidebars = {
    "**": [ "globaltoc.html","searchbox.html"]
}

#"logo-text.html",

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}


# Display todos by setting to True
todo_include_todos = True

html_show_sphinx = False



# -- Options for LaTeX output ---------------------------------------------

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
# author, documentclass [howto, manual, or own class]).
latex_documents = [
(
u'Olaya Alvarez', 'manual'),
]
