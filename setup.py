from setuptools import setup

setup(
    name='rsslogger',
    version='0.1',
    scripts = ['src/rsslogger'],
    install_requires = ['PyRSS2Gen>=1.1', 'feedparser>=5.1.3'],

    # PyPi stuff
    author = 'George Nikolopoulos',
    author_email = 'georges.nikolopoulos@gmail.com',
    description = 'Log messages to an rss feed file',
    license = 'GPLv3',
    keywords = 'loggging RSS',
    url = 'https://github.com/geonik/rsslogger',
)
