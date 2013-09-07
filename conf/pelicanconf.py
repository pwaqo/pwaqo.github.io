from __future__ import unicode_literals

THEME = 'youngeek-theme' 

# Basic

AUTHOR = 'Ricardo Ruiz'
SITENAME = "YounGeek"
SITEURL = 'http://localhost:8000'
TIMEZONE = "Europe/Madrid"

DEFAULT_CATEGORY = '/dev/random'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d de %B de %Y'

# Site

# Urls

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

CATEGORY_URL = 'cat/{slug}'
CATEGORY_SAVE_AS = 'cat/{slug}/index.html'

AUTHOR_URL = 'autor/{slug}'
AUTHOR_SAVE_AS = 'autor/{slug}/index.html'

USER_LOGO_URL = SITEURL + '/static/images/youngeek-logo.gif'

TAGLINE = "Geek & Pythonista"

DISQUS_SITENAME = "youngeek"
TWITTER_USERNAME = 'riki319'
GOOGLE_ANALYTICS = 'UA-16479483-10'
COLLAPSE_COMMENTS = False
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'


STATIC_PATHS = ["images"]
FILES_TO_COPY = (('extra/google53aa3b50d6efd909.html', 'google53aa3b50d6efd909.html'),('extra/favicon.ico', 'favicon.ico'))
