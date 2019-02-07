from abc import ABCMeta, abstractproperty
import time
import inspect
from HyperAPI.hdp_api.routes.base.validators import ValidatorObjectID, ValidatorAny, ValidatorInt
from HyperAPI.hdp_api.routes.base.validators import RoutePathInvalidException, RouteCompatibilityFailed, RouteConsistencyException
from HyperAPI.utils.version import Version
from requests.exceptions import HTTPError


class Route(object):
    __metaclass__ = ABCMeta
    GET = "GET"
    POST = "POST"

    available_since = 0
    removed_since = None

    _path_keys = {}
    _compatibility_routes = []

    VALIDATOR_OBJECTID = ValidatorObjectID()
    VALIDATOR_ANY = ValidatorAny()
    VALIDATOR_INT = ValidatorInt()

    @classmethod
    def get_route_name(cls):
        return cls.__name__.lower().replace('_', '')

    @classmethod
    def is_available(cls, version, compatiblity_mode=True):
        _check_version = Version(version)
        if Version(cls.available_since) <= _check_version and Version(cls.removed_since) > _check_version:
            return True

        if not compatiblity_mode:
            return False

        _compatibility_routes = list(_r for _r in cls.get_subroutes())
        return any(_r.is_available(version) for _r in _compatibility_routes)

    @abstractproperty
    def name(self):
        """The Route key (not name) as defined in the API schema"""
        return None

    @abstractproperty
    def httpMethod(self):
        """The Route http method as defined in the API schema"""
        return None

    @abstractproperty
    def path(self):
        """The Route path as defined in the API schema"""
        return None

    @classmethod
    def get_subroutes(cls):
        for _route in (_m[1] for _m in inspect.getmembers(cls) if inspect.isclass(_m[1]) and issubclass(_m[1], SubRoute)):
            yield _route

    @classmethod
    def check_routes_integrity(cls):
        sub_routes = sorted(cls.get_subroutes(), key=lambda x: x.available_since)
        sub_routes.insert(0, cls)

        for _n, _route in enumerate(sub_routes):
            if _route.removed_since <= _route.available_since:
                raise RouteConsistencyException('Route removed before availability')
            if _n > 0:
                _previous = sub_routes[_n - 1]
                if _route.available_since != _previous.removed_since:
                    raise RouteConsistencyException('Break in route continuity')

    def __init__(self, session, watcher=None):
        self.session = session
        self._watcher = watcher

        if self.is_available(session.version, compatiblity_mode=False):
            self.__routed_call__ = self.__direct_call__
        else:
            for _route in self.get_subroutes():
                if _route.is_available(self.session.version):
                    _routeInstance = _route(session, watcher=watcher)
                    self.name = _route.name or self.name
                    self.path = _route.path or self.path
                    self._path_keys = _route._path_keys or self._path_keys
                    self.httpMethod = _route.httpMethod or self.httpMethod
                    self.available_since = _route.available_since or self.available_since
                    self.removed_since = _route.removed_since or self.removed_since
                    self.__routed_call__ = lambda self, **kwargs: _routeInstance.__call__(**_routeInstance._convert_args(**kwargs))
                    break
            else:
                raise RouteCompatibilityFailed('Unable to create the route version compatible')

    def __call__(self, **kwargs):
        return self.__routed_call__(self, **kwargs)

    def __direct_call__(self, **kwargs):
        formatter = dict.fromkeys(self._path_keys)
        for _path_key, _validator in self._path_keys.items():
            _value = kwargs.pop(_path_key, None)
            if not _validator(_value):
                raise RoutePathInvalidException(_path_key, _value, self.path, _validator)
            formatter[_path_key] = _value
        _path = self.path if self.path[0] != '/' else self.path[1:]
        _path = _path.format(**formatter)

        if self._watcher:
            self._watcher(str(self), kwargs.pop('info', 'call'))
            try:
                _result = self.session.request(self.httpMethod, _path, **kwargs)
                self._watcher(str(self), '200')
                return _result
            except HTTPError as HE:
                self._watcher(str(self), str(HE.response))
                raise
        return self.session.request(self.httpMethod, _path, **kwargs)

    def call_when(self, condition=lambda x: True, call=lambda x: None, step=1, timeout=500, **kwargs):
        _remaining = timeout

        if self._watcher:
            kwargs['info'] = 'call'

        while _remaining > 0:
            _remaining = _remaining - step
            time.sleep(step)
            _res = self.__call__(**kwargs)
            if condition(_res):
                return call(_res)
            elif kwargs.get('info', None) == 'call':
                kwargs['info'] = 'retry'
        if self._watcher:
            self._watcher(str(self), 'timeout')
        return None

    def wait_until(self, condition=lambda x: True, step=1, timeout=60, **kwargs):
        _remaining = timeout

        if self._watcher:
            kwargs['info'] = 'call'

        while _remaining > 0:
            _remaining = _remaining - step
            time.sleep(step)
            _res = self.__call__(**kwargs)
            if condition(_res):
                return _res
            elif kwargs.get('info', None) == 'call':
                kwargs['info'] = 'retry'

        if self._watcher:
            self._watcher(str(self), 'timeout')
        return None

    @property
    def __doc__(self):
        msg = 'Route {} [{}]'.format(self.name, self.httpMethod)
        msg += '\n{}'.format(self.path)
        for _k, _v in self._path_keys.items():
            msg += '\n{:>20} : {}'.format(_k, _v.__doc__)
        msg += '\n'
        return msg

    @property
    def help(self):
        print(self.__doc__)

    def __repr__(self):
        return '{} <{}> {}:{}'.format(self.get_route_name(), id(self), self.httpMethod, self.path)

    def __str__(self):
        return '{: >4}:{}'.format(self.httpMethod, self.path)


class SubRoute(Route):
    # Abstract properties are redefined so they are no longer mandatory for sub routes
    name = None
    httpMethod = None
    path = None

    def __init__(self, session, watcher=None):
        self.session = session
        self._watcher = watcher

    def __call__(self, **kwargs):
        return self.__direct_call__(**kwargs)

    @classmethod
    def is_available(cls, version):
        _check_version = Version(version)
        if Version(cls.available_since) <= _check_version and Version(cls.removed_since) > _check_version:
            return True
        return False

    @staticmethod
    def _convert_args(**kwargs):
        return kwargs
