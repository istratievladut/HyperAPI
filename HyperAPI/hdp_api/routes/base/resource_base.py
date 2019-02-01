from abc import ABCMeta, abstractproperty
import inspect
from HyperAPI.hdp_api.routes.base.route_base import Route
from HyperAPI.utils.version import Version


class Resource(object):
    __metaclass__ = ABCMeta
    available_since = 0
    remove_since = None

    @abstractproperty
    def name(self):
        """The resource name as defined in the API schema"""
        return "Resource Name"

    def __init__(self, session, watcher=None):
        self.session = session
        self._routes = {}
        for _route in (_m[1] for _m in inspect.getmembers(self.__class__) if inspect.isclass(_m[1]) and issubclass(_m[1], Route)):
            if _route.is_available(self.session.version):
                _routeInstance = _route(session, watcher=watcher)
                _routeName = _route.get_route_name()
                self.__setattr__(_routeName, _routeInstance)
                self._routes[_routeName] = _routeInstance

    def __iter__(self):
        for _r in self._routes.values():
            yield _r

    @classmethod
    def is_available(cls, version):
        _check_version = Version(version)
        return Version(cls.available_since) <= _check_version and Version(cls.removed_since) > _check_version

    @property
    def __doc__(self):
        return '\n'.join(_r.help for _r in self._routes.values())

    @property
    def help(self):
        print(self.__doc__)

    def __repr__(self):
        return '{} <{}>'.format(self.__class__.__name__, id(self))
