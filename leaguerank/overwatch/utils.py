from datetime import timedelta
import re


regex = re.compile(
    (r'((?P<hours>\d+?) hours?)?((?P<minutes>\d+?) minutes?)'
     r'?((?P<seconds>\d+?) seconds?)?'))


def parse_timespan(time_str):
    parts = regex.match(time_str)
    if not parts:
        return
    parts = parts.groupdict()
    time_params = {}
    for (name, param) in parts.iteritems():
        if param:
            time_params[name] = int(param)
    return timedelta(**time_params).total_seconds()


def parse_percent(s):
    n = s.split('%')[0]
    return float(n)/100
