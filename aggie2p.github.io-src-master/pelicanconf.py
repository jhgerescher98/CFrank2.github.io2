#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Group 3'
SITENAME = 'TCMG 412-Group Three'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = 'pelican-chunk'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('TAMU Technology Mgmt', 'https://eahr.tamu.edu/academics/technology-management/'),)
         #('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Facebook', '#'),
          ('@TAMU Twitter', 'https://twitter.com/TAMU'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True