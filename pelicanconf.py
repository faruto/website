#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

"""
Ideas:
------
https://github.com/jantman/blog/blob/master/pelicanconf.py
http://moparx.com/2014/04/adding-search-capabilities-within-your-pelican-powered-site-using-tipue-search/
https://github.com/dreikanter/markdown-grid

Look and feel inspiration:
--------------------------
https://www.jetbrains.com/pycharm/
http://ninja-ide.org/
http://nl.mathworks.com/products/matlab/
http://www.rstudio.com/
http://brackets.io/

domain config:
--------------
https://help.github.com/articles/my-custom-domain-isn-t-working/

"""

# Overall site-wide settings
# --------------------------
AUTHOR = u'Spyder Development Team'
SITENAME = u'Spyder IDE'
DISQUS_SITENAME = 'spyder-ide'
#GOOGLE_ANALYTICS = 'UA-2718127-2'
#GA_DOMAIN = 'jasonantman.com'
SITEURL = ''

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'


# Theme settings
# --------------
# based on https://github.com/DandyDev/pelican-bootstrap3
THEME = 'theme'
BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_THEME = 'spacelab'

# theme specific settings
# -----------------------
HIDE_SIDEBAR = False
SHOW_ARTICLE_AUTHOR = True
SITELOGO = 'images/spyder.png' 
SITELOGO_SIZE = '20px' 
HIDE_SITENAME = False
CUSTOM_CSS = 'static/custom.css'
DISPLAY_BREADCRUMBS = False
PYGMENTS_STYLE = 'tango'


# Content / Files
# ---------------
PATH = 'content'
OUTPUT_PATH = 'output/'
IGNORE_FILES = ['.#*']
PAGE_PATHS = ['pages']
PAGE_EXCLUDES = []
ARTICLE_PATHS = ['blog']
#ARTICLE_EXCLUDES = ['pages',]

DEFAULT_CATEGORY = 'miscelaneous'
SITEMAP_SAVE_AS = 'sitemap.xml'

STATIC_PATHS = [
    'CNAME',
    'images',
    'extra/favicon.ico',
    'extra/robots.txt',
    'extra/custom.css'
#    'GFX',
#    'extra/googleea75ea27535d4ffe.html',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/custom.css': {'path': 'static/custom.css'}
    #'static/googleea75ea27535d4ffe.html': {'path': 'googleea75ea27535d4ffe.html'},
}

DIRECT_TEMPLATES = (
    'index',
    'tags',
    'categories',
    'archives',
    'sitemap',
    'search'
)

# Menu configuration
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
#    ('Home', '/'),
    ('Features', '/features/'),
    ('Documentation', 'https://pythonhosted.org/spyder/'),
#    ('Documentation', '/docs/'),
    ('Plugins', '/plugins/'),
    ('Contribute', '/contribute/'),
    ('Support', '/support/'),
    ('Blog', '/blog/'),
#    ('Resources', '/resources/'),
#    ('Archives', '/archives.html'),
#    ('Tags', '/tags.html'),
#    ('Category1', 'category/category1.html'),
#    ('Category2', 'category/category2.html'),
)

# URL settings
# ------------
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'categories/{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tags/{slug}/index.html'
TAG_SAVE_AS = TAG_URL
TAGS_URL = 'tags.html'
TAGS_SAVE_AS = TAGS_URL
INDEX_SAVE_AS = 'blog/index.html'

# fix this... not working?
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'



# Plugins
# -------
PLUGIN_PATHS = ['plugins', 'pelican-plugins']
PLUGINS = ['tipue_search']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
#    ('Twitter', 'http://twitter.com/Spyder_IDE'),
#    ('Python.org', 'http://python.org/'),
#    ('Jinja2', 'http://jinja.pocoo.org/'),
#    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
