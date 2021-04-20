import datetime

project = "sample-proj"
author = "matplotlib developers"

project = "Matplotlib third-party packages"
copyright = (
     f"2012 - {datetime.datetime.now().year} The Matplotlib development team"
 )

source_suffix = ['.rst']

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "pydata_sphinx_theme"
html_static_path = ["./_static"]
html_logo = "_static/logo2.svg"
html_theme_options = {
     "logo_link": "https://matplotlib.org/stable",
     "icon_links": [
         {
             "name": "gitter",
             "url": "https://gitter.im/matplotlib",
             "icon": "fab fa-gitter",
         },
         {
             "name": "discourse",
             "url": "https://discourse.matplotlib.org",
             "icon": "fab fa-discourse",
         },
         {
             "name": "GitHub",
             "url": "https://github.com/matplotlib/matplotlib",
             "icon": "fab fa-github-square",
         },
         {   "name": "twitter", 
             "url":"https://twitter.com/matplotlib/", 
             "icon":"fab fa-twitter-square",
         },
     ],
}
html_sidebars = {
    '**': ['localtoc.html']
}

