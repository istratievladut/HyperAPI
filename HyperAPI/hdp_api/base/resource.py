from abc import ABCMeta, abstractproperty
import inspect
from HyperAPI.hdp_api.base.route import Route
from HyperAPI.utils.version import Version


class Resource(object):
    __metaclass__ = ABCMeta
    available_since = 0
    remove_since = None
    unavailable_on = []

    @abstractproperty
    def name(self):
        """The resource name as defined in the API schema"""
        return "Resource Name"

    def __init__(self, session, watcher=None):
        self.session = session
        self._routes = {}
        for _route in self._iter_routes_classes(self.session.version):
            _routeInstance = _route(session, watcher=watcher)
            _routeName = _route.get_route_name()
            self.__setattr__(_routeName, _routeInstance)
            self._routes[_routeName] = _routeInstance

    def __iter__(self):
        for _r in self._routes.values():
            yield _r

    @classmethod
    def _iter_routes_classes(cls, version):
        for _route in (_m[1] for _m in inspect.getmembers(cls) if inspect.isclass(_m[1]) and issubclass(_m[1], Route)):
            if _route.is_available(version):
                yield _route

    @classmethod
    def is_available(cls, version):
        _check_version = Version(version)
        return Version(cls.available_since) <= _check_version and Version(cls.removed_since) > _check_version and _check_version not in list(Version(_v) for _v in cls.unavailable_on)

    @classmethod
    def check_routes_integrity(cls):
        for _route in (_m[1] for _m in inspect.getmembers(cls) if inspect.isclass(_m[1]) and issubclass(_m[1], Route)):
            _route.check_routes_integrity()

    @property
    def __doc__(self):
        return '\n'.join(_r.help for _r in self._routes.values())

    @property
    def help(self):
        print(self.__doc__)

    def __repr__(self):
        return '{} <{}>'.format(self.__class__.__name__, id(self))
