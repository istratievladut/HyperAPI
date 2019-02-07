import random
import re


class RoutePathInvalidException(Exception):
    def __init__(self, name, value, path, validator):
        self.path = path
        self.name = name
        self.value = value
        self.validator = validator

    def __str__(self):
        return 'Route path invalid : {}={} ({})\n\t{}'.format(self.name, self.value, self.validator.__class__.__name__, self.path)


class RouteCompatibilityFailed(Exception):
    pass


class RouteConsistencyException(Exception):
    pass


class ValidatorObjectID(object):
    """(str) A 24 hex digit MongoDB ObjectID."""
    @staticmethod
    def __call__(value):
        return re.match('[0-9a-z]{24}', '{}'.format(value)) is not None

    @staticmethod
    def getRandom():
        return ''.join(random.choices('0123456789abcdef', k=24))


class ValidatorAny(object):
    """(any) Any object except None and empty string."""
    @staticmethod
    def __call__(value):
        if value is None:
            return False
        if isinstance(value, str) and not value.strip():
            return False
        return True

    @staticmethod
    def getRandom():
        return ''.join(random.choices('0123456789abcdef', k=24))


class ValidatorInt(object):
    """(int) An Integer Value."""
    @staticmethod
    def __call__(value):
        return isinstance(value, int)

    @staticmethod
    def getRandom():
        return random.randint(0, 100)
