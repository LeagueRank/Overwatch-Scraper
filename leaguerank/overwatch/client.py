from collections import namedtuple

import requests

try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup

from .codes import by_hero


Metric = namedtuple('Metric', ['name', 'hero', 'value'])


class MetricByHero(object):
    def __init__(self, name, data):
        self.data = []
        for hero in data:
            self.data.append(Metric(
                name=name,
                hero=hero.find('div', {'class': 'title'}).text,
                value=hero.find('div', {'class': 'description'}).text
            ))

    def __iter__(self):
        return self.data.__iter__()


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

    def metrics(self):
        metrics = {}
        for key in by_hero:
            metrics[key] = list(MetricByHero(key, self.soup.find(
                "div",
                {"data-category-id": by_hero[key]}
                ).find_all("div", {"class": "bar-text"})))
        return metrics

    def load(self):
        self.html = requests.get(self.profile_url()).text.encode('utf-8')
        self.soup = BeautifulSoup(self.html, 'html.parser')
