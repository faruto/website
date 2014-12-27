#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

"""
Ideas: 
https://github.com/jantman/blog/blob/master/pelicanconf.py
http://moparx.com/2014/04/adding-search-capabilities-within-your-pelican-powered-site-using-tipue-search/

"""

# Overall site-wide settings
# --------------------------
AUTHOR = u'Spyder Development Team'
SITENAME = u'Spyder IDE'
#DISQUS_SITENAME = 'spyder'
#GOOGLE_ANALYTICS = 'UA-2718127-2'
#GA_DOMAIN = 'jasonantman.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'

DEFAULT_CATEGORY = "Miscellaneous"

# Theme
# -----
THEME = 'theme-bootstrap3/'
BOOTSTRAP_THEME = 'cosmo'

# Content / Files
# ---------------
OUTPUT_PATH = 'output/'

IGNORE_FILES = ['.#*']

#PATH = 'content/'
#PAGE_PATHS = ['pages']
#PAGE_EXCLUDES = []
#ARTICLE_PATHS = ['content/blog']
#ARTICLE_EXCLUDES = ['pages',]

SITEMAP_SAVE_AS = 'sitemap.xml'

STATIC_PATHS = [
    'CNAME',
    'GFX',
    'extra/favicon.ico',
    'extra/robots.txt',
    'extra/googleea75ea27535d4ffe.html',
    'images',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'static/googleea75ea27535d4ffe.html': {'path': 'googleea75ea27535d4ffe.html'},
}

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
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

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
