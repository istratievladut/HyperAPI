from abc import ABCMeta, abstractproperty
import inspect
from HyperAPI.hdp_api.routes.base.route_base import Route


class Resource(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        """The resource name as defined in the API schema"""
        return "Resource Name"

    def __init__(self, session, watcher=None):
        self.session = session
        self._routes = {}
        for _route in (_m[1] for _m in inspect.getmembers(self.__class__) if inspect.isclass(_m[1]) and issubclass(_m[1], Route)):
            _routeInstance = _route(session, watcher=watcher)
            _routeName = _route.get_route_name()
            self.__setattr__(_routeName, _routeInstance)
            self._routes[_routeName] = _routeInstance

    def __iter__(self):
        for _r in self._routes.values():
            yield _r

    @property
    def help(self):
        for _r in self._routes.values():
            _r.help

    def __repr__(self):
        return '{} <{}>'.format(self.__class__.__name__, id(self))
