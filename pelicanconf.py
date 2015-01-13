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

# --------------------------
# Overall site-wide settings
# --------------------------
AUTHOR = u'Spyder Development Team'
SITENAME = u'Spyder IDE'
SITEURL = ''
TIMEZONE = 'Europe/Amsterdam'
DEFAULT_LANG = u'en'
DEFAULT_CATEGORY = 'miscelaneous'

THEME = 'theme'

DEFAULT_PAGINATION = 5

# Analytics and comments
GOOGLE_ANALYTICS = 'UA-58106712-1'
#GA_DOMAIN = 'jasonantman.com'
DISQUS_SITENAME = 'spyder-ide'
#PIWIK_URL, PIWIK_SSL_URL, PIWIK_SITE_ID

# Template Settings
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Features', '/features/'),
    ('Documentation', 'https://pythonhosted.org/spyder/'),
#    ('Plugins', '/plugins/'),
    ('Support', '/support/'),
    ('Contribute', '/contribute/'),
    ('Blog', '/blog/'),
#    ('Resources', '/resources/'),
#    ('Archives', '/archives.html'),
#    ('Tags', '/tags.html'),
#    ('Category1', 'category/category1.html'),
#    ('Category2', 'category/category2.html'),
)
LINKS = (
#    ('Twitter', 'http://twitter.com/Spyder_IDE'),
#    ('Python.org', 'http://python.org/'),
#    ('Jinja2', 'http://jinja.pocoo.org/'),
#    ('You can modify those links in your config file', '#'),
)
# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# ----------------------------------
# bootstrap3 theme specific settings
# ----------------------------------
# based on https://github.com/DandyDev/pelican-bootstrap3

# Bootswatch and other Bootstrap 3 themes - http://bootswatch.com/
"""
BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_THEME = 'cosmo'
"""
BOOTSTRAP_THEME = 'spacelab'
#BOOTSTRAP_THEME = 'simplex'
HIDE_SIDEBAR = False
SHOW_ARTICLE_AUTHOR = True
SITELOGO = 'images/spyder.png' 
SITELOGO_SIZE = '75px' 
HIDE_SITENAME = False
CUSTOM_CSS = 'static/custom.css'
DISPLAY_BREADCRUMBS = True

# pygments styles
"""
PYGMENTS_STYLE = 'native'  # use the defined setup in bootswatch themes
PYGMENTS_STYLE = 'tango'
PYGMENTS_STYLE = 'autumn'
PYGMENTS_STYLE = 'borland'
PYGMENTS_STYLE = 'bw'
PYGMENTS_STYLE = 'colorful'
PYGMENTS_STYLE = 'default'
PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE = 'friendly'
PYGMENTS_STYLE = 'fruity'
PYGMENTS_STYLE = 'manni'
PYGMENTS_STYLE = 'monokai'
PYGMENTS_STYLE = 'murphy'
PYGMENTS_STYLE = 'native'
PYGMENTS_STYLE = 'pastie'
PYGMENTS_STYLE = 'perldoc'
PYGMENTS_STYLE = 'solarizeddark'
PYGMENTS_STYLE = 'solarizedlight'
PYGMENTS_STYLE = 'tango'
PYGMENTS_STYLE = 'trac'
PYGMENTS_STYLE = 'vim'
PYGMENTS_STYLE = 'vs'
PYGMENTS_STYLE = 'zenburn'
"""
PYGMENTS_STYLE = 'zenburn'


# Pagination
USE_PAGER = True

# Sidebar options
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_AUTHORS_ON_SIDEBAR = True
RECENT_POST_COUNT = 4

# ------------
# URL settings
# ------------
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{0}index.html'.format(ARTICLE_URL)

CATEGORIES_URL =  'categories/'  # from theme!!
CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = '{0}index.html'.format(CATEGORY_URL)
CATEGORIES_SAVE_AS = 'categories/index.html'

TAGS_URL = 'tags/'   # from theme!!
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = '{0}index.html'.format(TAG_URL)
TAGS_SAVE_AS = 'tags/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{0}index.html'.format(PAGE_URL)
INDEX_SAVE_AS = 'blog/index.html'

# fix this... not working?
AUTHORS_URL = 'author/'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)


YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/index.html'


# -----------------------
# Content / Files / Paths
# -----------------------
PATH = 'content'
OUTPUT_PATH = 'output/'
IGNORE_FILES = ['.#*']
PAGE_PATHS = ['pages']
PAGE_EXCLUDES = []
ARTICLE_PATHS = ['blog']
#ARTICLE_EXCLUDES = ['pages',]


SITEMAP_SAVE_AS = 'sitemap.xml'

STATIC_PATHS = [
    'CNAME',
    'images',
    'favicon.ico',
    'robots.txt',
    'static/custom.css'
#    'GFX',
#    'extra/googleea75ea27535d4ffe.html',
]

EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'},
    'static/robots.txt': {'path': 'robots.txt'},
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

# tag cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

# -------
# Plugins
# -------
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['tipue_search']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
