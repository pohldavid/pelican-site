AUTHOR = 'dgp'
SITENAME = "DGP's Website"
SITESUBTITLE = "A Static Site &copy; 2023 David G. Pohl"
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# A list of tuples (Title, URL) for links to appear on the header.
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# A list of tuples (Title, URL) to appear in the “social” section.
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
#THEME = './themes/simple'
#THEME = './themes/elegant'
THEME = './themes/bootlex'
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = True

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
OUTPUT_RETENTION = []
# A list of tuples (Title, URL) for additional menu items to appear at the beginning of the main menu.
MENUITEMS = [('Menu Item 1','#'), ('Menu Item 2','#')]

