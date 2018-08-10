from collections import namedtuple

import requests

from .errors import *
from .utils import parse_timespan, parse_percent

try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup


Metric = namedtuple('Metric', ['label', 'value'])


class OverwatchProfile(object):
    def __init__(self, username, platform, region):
        self.username = username
        self.platform = platform
        self.region = region

        self.load()

    def profile_url(self):
        return "{ROOT_URL}/career/{platform}/{region}/{username}".format(
            ROOT_URL="https://playoverwatch.com/en-us",
            platform=self.platform,
            region=self.region,
            username=self.username
        )

    def is_private(self):
        return self.soup.find(
            "p", {"class": "masthead-permission-level-text"}
            ).text == "Private Profile"

    def metric_lookup(self, guid):
        return self.soup.find('option', {'value': guid}).text

    def fuzzy_parse(self, s):
        if s.find('%') > -1:
            return parse_percent(s)
        if s.find(' ') > -1 or s.find(':') > -1:
            return parse_timespan(s)
        if s.find('-') > -1:
            return 0
        if s.find(',') > -1:
            return float(s.replace(',', ''))

        return float(s)

    def ascii_hero(self, s):
        if s.find('Torb') > -1:
            return 'Torbjorn'
        if s.find('cio') > -1:
            return 'Lucio'
        return s

    def portrait(self):
        return self.soup.find('img', {'class': 'player-portrait'})['src']

    def rank(self):
        return int(self.soup.find('div', {'class': 'competitive-rank'}).text)

    def endorsement_level(self):
        return int(self.soup.find('div', {'class': 'endorsement-level'}).text)

    def hero_metrics(self):
        if self.is_private():
            raise PrivateProfile()
        data = {}
        for category in self.soup.find_all(
                                    'div', {'data-js': 'career-category'}):
            d1 = {}
            for metric in category.find_all(
                                    'div', {'data-group-id': 'comparisons'}):
                name = self.metric_lookup(metric['data-category-id'])
                d1[name] = []
                for value in metric.find_all('div', {'class': 'bar-text'}):
                    d1[name].append(Metric(
                        label=self.ascii_hero(
                            value.find('div', {'class': 'title'}).text
                        ),
                        value=self.fuzzy_parse(
                            value.find('div', {'class': 'description'}).text
                        )
                    ))
            data[category['data-mode']] = d1
        if not len(data.keys()):
            raise NoData()
        return data

    def stats_metrics(self):
        if self.is_private():
            raise PrivateProfile()
        data = {}
        for category in self.soup.find_all(
                                    'div', {'data-js': 'career-category'}):
            d1 = {}
            for metric in category.find_all(
                                    'div', {'data-group-id': 'stats'}):
                name = self.ascii_hero(
                    self.metric_lookup(metric['data-category-id'])
                )
                d1[name] = []
                for tbody in metric.find_all('tbody'):
                    for value in tbody.find_all('tr'):
                        (label, val) = value.find_all('td')
                        d1[name].append(Metric(
                            label=label.text,
                            value=self.fuzzy_parse(val.text)
                        ))
            data[category['data-mode']] = d1
        if not len(data.keys()):
            raise NoData()
        return data

    def load(self):
        self.html = requests.get(self.profile_url()).text.encode('utf-8')
        self.soup = BeautifulSoup(self.html, 'html.parser')
