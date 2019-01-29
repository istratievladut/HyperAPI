class Version(object):

    def __init__(self, version_label: str):
        try:
            result = [int(v) for v in version_label.strip().split('.')]
        except Exception:
            result = None
        if result is None:
            self.major = None
            self.minor = None
            self.patch = None
            self.is_dev = True
        else:
            self.major = result[0]
            self.minor = 0 if len(result) == 1 else result[1]
            self.patch = 0 if len(result) == 2 else result[2]
            self.is_dev = False

    def __str__(self):
        if self.is_dev:
            return "Dev Version"
        return "{x.major}.{x.minor}.{x.patch}".format(x=self)

    def __eq__(self, other):
        if self.is_dev:
            return other.is_dev
        return self.major == other.major and self.minor == other.minor and self.patch == other.patch

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if self.is_dev:
            return False
        if self.major > other.major:
            return False
        if self.major == other.major:
            if self.minor > other.minor:
                return False
            if self.minor == other.minor:
                return self.patch < other.patch
        return True

    def __gt__(self, other):
        if self.is_dev:
            return not other.is_dev
        if self.major < other.major:
            return False
        if self.major == other.major:
            if self.minor < other.minor:
                return False
            if self.minor == other.minor:
                return self.patch > other.patch
        return True

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __hash__(self):
        if self.is_dev:
            return 0
        return(hash((self.major, self.minor, self.patch)))
