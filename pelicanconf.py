#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH = 'content'

# Basic site info
AUTHOR = u'Daniel Zappala'
SITENAME = u'The Zappala Kitchen'
LOGO = 'cooking.png'
SITEURL = 'http://kitchen.zappala.org'

# Contact info
EMAIL = 'daniel.zappala<br>@gmail.com'
FACEBOOK_URL = 'https://www.facebook.com/daniel.zappala'
GOOGLEPLUS_URL = 'http://plus.google.com/114449822521576560110?prsrc=3'
TWITTER_URL = 'https://twitter.com/Daniel_Zappala'

LICENSE = '<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a>'

TIMEZONE = 'US/Mountain'
DEFAULT_LANG = u'en'

# Tag cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

# How to save pages
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
INDEX_SAVE_AS = 'index.html'

# Templates
DIRECT_TEMPLATES = ('index', 'tags', 'archives')

# Feeds
FEED_DOMAIN = SITEURL
TAG_FEED_ATOM = 'feeds/tag-%s.atom.xml'

# Misc
STATIC_PATHS = ['images','docs']
DEFAULT_PAGINATION = 10

# Theme
USER_LOGO_URL = "/images/zappala.jpg"
THEME = "themes/pelican-images"

# Plugins
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['assets','neighbors', 'summary']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
