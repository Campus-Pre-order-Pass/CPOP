from datetime import timedelta, timezone


class Configuration(object):
    tz = timezone(timedelta(hours=+8))
