from datetime import timedelta
import re


regex1 = re.compile(
    (r'((?P<hours>\d+?) hours?)?((?P<minutes>\d+?) minutes?)'
     r'?((?P<seconds>\d+?) seconds?)?'))

regex2 = re.compile(
    (r'(((?P<hours>\d+?):)?((?P<minutes>\d+?):))'
     r'?(?P<seconds>\d+)'))


def parse_timespan(time_str):
    regex = regex1
    if time_str.find(' ') == -1:
        regex = regex2
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


if __name__ == "__main__":
    s = (
        '10:10:10',
        '50:21:01',
        '1',
        '02',
        '45 minutes',
        '1 hour',
        '1 minute',
        '1 second',
        '10:10',
        '1:10'
    )
    for t in s:
        print t
        parse_timespan(t)
