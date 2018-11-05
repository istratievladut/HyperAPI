from abc import ABCMeta, abstractproperty
import warnings
import time
from HyperAPI.hdp_api.routes.base.validators import ValidatorObjectID, ValidatorAny, ValidatorInt, RoutePathInvalidException
from requests.exceptions import HTTPError


class Route(object):
    __metaclass__ = ABCMeta
    GET = "GET"
    POST = "POST"
    _path_keys = {}

    VALIDATOR_OBJECTID = ValidatorObjectID()
    VALIDATOR_ANY = ValidatorAny()
    VALIDATOR_INT = ValidatorInt()

    deprecated_since = None
    available_since = None

    @classmethod
    def get_route_name(cls):
        return cls.__name__.lower().replace('_', '')

    @classmethod
    def add_redirection(cls, version, route_to, convert_to):
        if issubclass(route_to, cls):
            raise Exception('A route can not be redirected to itself')
        if not hasattr(cls, 'routing_table'):
            cls.routing_table = dict()
        cls.routing_table[version] = (route_to, convert_to)

    @classmethod
    def get_routing_table(cls):
        return getattr(cls, 'routing_table', {})

    @classmethod
    def has_redirections(cls):
        return len(cls.get_routing_table().keys())

    @classmethod
    def get_redirection_fct(cls, session, watcher):
        if not cls.has_redirections():
            return cls.__direct_call__
        else:
            # Getting the highest route version available
            _sorted_versions = sorted(cls.get_routing_table().keys(), reverse=True)
            _routing_version = next(filter(lambda v: session.version >= v, _sorted_versions), None)
            if _routing_version is None:
                return cls.__direct_call__
            else:
                cls_route_to, convert_to = cls.get_routing_table()[_routing_version]
                return lambda self, **kwargs: cls_route_to(session, watcher).__call__(**convert_to(**kwargs))

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

    def __init__(self, session, watcher=None):
        self.session = session
        self._watcher = watcher
        if self.deprecated_since is not None and self.session.version >= self.deprecated_since:
            _message = f"The route '{self.get_route_name()}' is deprecated since server version {self.deprecated_since}."
            warnings.warn(_message, stacklevel=0)

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
    def help(self):
        msg = 'Route {} [{}]'.format(self.name, self.httpMethod)
        msg += '\n{}'.format(self.path)
        for _k, _v in self._path_keys.items():
            msg += '\n{:>20} : {}'.format(_k, _v.__doc__)
        msg += '\n'
        print(msg)

    def __repr__(self):
        return '{} <{}> {}:{}'.format(self.get_route_name(), id(self), self.httpMethod, self.path)

    def __str__(self):
        return '{: >4}:{}'.format(self.httpMethod, self.path)
