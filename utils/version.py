import re


class Version(object):

    def __init__(self, version_label: str):
        pattern_version = re.compile('([0-9]*)\.([0-9]*)(-([0-9a-f]{40}))?', re.IGNORECASE)
        result = pattern_version.search(version_label)
        if result is None:
            self.major = None
            self.minor = None
            self.build = None
            self.is_dev = True
        else:
            _parts = result.groups()
            self.major = int(_parts[0])
            self.minor = int(_parts[1])
            self.build = _parts[3]
            self.is_dev = False

    def __str__(self):
        if self.is_dev:
            return "Dev Version"
        if self.build:
            return "{x.major}.{x.minor} - {x.build}".format(x=self)
        return "{x.major}.{x.minor}".format(x=self)

    def __eq__(self, other):
        if self.is_dev:
            return other.is_dev
        return self.major == other.major and self.minor == other.minor

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if self.is_dev:
            return False
        if self.major > other.major:
            return False
        if self.major == other.major:
            return self.minor < other.minor
        return True

    def __gt__(self, other):
        if self.is_dev:
            return not other.is_dev
        if self.major < other.major:
            return False
        if self.major == other.major:
            return self.minor > other.minor
        return True

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __hash__(self):
        if self.is_dev:
            return 0
        if self.build:
            return int(self.build, 16)
        return(hash((self.major, self.minor)))

