from collections import namedtuple

import requests

from .codes import stats

try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup


Metric = namedtuple('Metric', ['hero', 'value'])


class MetricByHero(object):
    def __init__(self, data, parser):
        self.data = []
        for hero in data:
            self.data.append(Metric(
                hero=hero.find('div', {'class': 'title'}).text,
                value=parser(hero.find('div', {'class': 'description'}).text)
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
        for group in stats:
            metrics[group] = {}
            for key in stats[group]:
                metrics[group][key] = list(
                    MetricByHero(
                        self.soup.find(
                            "div",
                            {"id": stats[group][key]['parent_id']}
                        ).find(
                            "div",
                            {"data-category-id": stats[group][key]['selector']}
                        ).find_all(
                            "div",
                            {"class": "bar-text"}
                        ),
                        stats[group][key].get('value_parser', lambda x: x)
                    )
                )
        return metrics

    def load(self):
        self.html = requests.get(self.profile_url()).text.encode('utf-8')
        self.soup = BeautifulSoup(self.html, 'html.parser')
