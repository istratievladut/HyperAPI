from abc import ABCMeta, abstractproperty
import warnings
import time
from HyperAPI.hdp_api.routes.base.validators import ValidatorObjectID, ValidatorAny, ValidatorInt, RoutePathInvalidException, RouteCompatibilityFailed
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
    _convert_args = None

    VALIDATOR_OBJECTID = ValidatorObjectID()
    VALIDATOR_ANY = ValidatorAny()
    VALIDATOR_INT = ValidatorInt()

    __reroute_class__ = False

    @classmethod
    def get_route_name(cls):
        return cls.__name__.lower().replace('_', '')

    @classmethod
    def reroute_to(cls, name=None, httpMethod=None, path=None, path_keys=None, convert_args=None, available_since=None, removed_since=None):

        def default_convert(**args):
            return args

        properties = {
            'name': name or cls.name,
            'httpMethod': httpMethod or cls.httpMethod,
            'path': path or cls.path,
            '_path_keys': path_keys or cls._path_keys,
            'available_since': available_since or cls.removed_since,
            'removed_since': removed_since or None,
            '_convert_args': convert_args or default_convert,
            '__reroute_class__': True,
        }

        # Creating a new class name for the compatibility route
        _cmp_class_name = '{}_{}_{}'.format(cls.__name__, properties.get('available_since'), properties.get('removed_since')).replace('.', '')
        # Dynamically creating a new class definition for the route
        try:
            _cmp_route = type(_cmp_class_name, (Route,), properties)
            cls._compatibility_routes.append(_cmp_route)
        except Exception:
            _message = f"Unable to create compatibility version of the route '{cls.get_route_name()}' for versions {properties.get('available_since', 'N/A')} to {properties.get('removed_since', 'N/A')}."
            warnings.warn(_message, stacklevel=0)

    @classmethod
    def is_available(cls, version):
        _check_version = Version(version)
        if Version(cls.available_since) <= _check_version and Version(cls.removed_since) > _check_version:
            return True
        elif cls.__reroute_class__:
            return False
        else:
            return any(_r.is_available(version) for _r in cls._compatibility_routes)

    @abstractproperty
    def name(self):
        """The Route key (not name) as defined in the API schema"""
        return "Route Name"

    @abstractproperty
    def httpMethod(self):
        """The Route http method as defined in the API schema"""
        return "http Method"

    @abstractproperty
    def path(self):
        """The Route path as defined in the API schema"""
        return "Route Path"

    @classmethod
    def get_redirection_fct(cls, session, watcher):
        if cls.is_available(session.version):
            return cls.__direct_call__
        else:
            for _cmp_route in cls._compatibility_routes:
                if _cmp_route.is_available(session.version):
                    return lambda self, **kwargs: _cmp_route(session, watcher).__call__(**_cmp_route._convert_args(**kwargs))
            raise RouteCompatibilityFailed('Unable to create the route version compatible')

    def __init__(self, session, watcher=None):
        self.session = session
        self._watcher = watcher

        self.__routed_call__ = self.get_redirection_fct(session, watcher)

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
