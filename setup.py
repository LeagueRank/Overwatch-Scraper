from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-overwatchprofile-scraper',
    version='1.0.5',
    description='A python Overwatch Profile scraper that doesn\'t suck',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LeagueRank/Overwatch-Scraper',
    author='David Horn',
    author_email='david@leaguerank.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2'
    ],
    install_requires=[
        'bs4',
        'requests',
        'requests[security]'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)
