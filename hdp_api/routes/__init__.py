from abc import ABCMeta, abstractproperty, abstractmethod
import inspect
import random
import re
import time
from requests.exceptions import HTTPError

class RoutePathInvalidException(Exception):
    def __init__(self, name, value, path, validator):
        self.path = path
        self.name = name
        self.value = value
        self.validator = validator

    def __str__(self):
        return 'Route path invalid : {}={} ({})\n\t{}'.format(self.name, self.value, self.validator.__class__.__name__, self.path)

class ValidatorObjectID(object):
    """(str) A 24 hex digit MongoDB ObjectID."""
    @staticmethod
    def __call__(value):
        return re.match('[0-9a-z]{24}','{}'.format(value)) is not None
    @staticmethod
    def getRandom():
        return ''.join(random.choices('0123456789abcdef', k=24))

class ValidatorAny(object):
    """(any) Any object except None and empty string."""
    @staticmethod
    def __call__(value):
        if value is None :
            return False
        if isinstance(value,str) and not value.strip() :
            return False
        return True
    @staticmethod
    def getRandom():
        return ''.join(random.choices('0123456789abcdef', k=24))

class ValidatorInt(object):
    """(int) An Integer Value."""
    @staticmethod
    def __call__(value):
        return isinstance(value,int)
    @staticmethod
    def getRandom():
        return random.randint(0,100)

class Route(object):
    __metaclass__ = ABCMeta
    GET = "GET"
    POST = "POST"
    _path_keys = {}

    VALIDATOR_OBJECTID = ValidatorObjectID()
    VALIDATOR_ANY = ValidatorAny()
    VALIDATOR_INT = ValidatorInt()

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

    def __init__(self,session, watcher=None):
        self.session = session
        self._watcher = watcher

    def __call__(self,**kwargs):
        formatter = dict.fromkeys(self._path_keys)
        for _path_key, _validator in self._path_keys.items():
            _value = kwargs.pop(_path_key,None)
            if not _validator(_value) :
                raise RoutePathInvalidException(_path_key, _value, self.path, _validator)
            formatter[_path_key] = _value
        _path = self.path if self.path[0] != '/' else self.path[1:]
        _path = _path.format(**formatter)

        if self._watcher:
            self._watcher(str(self),kwargs.pop('info','call'))
            try:
                _result = self.session.request(self.httpMethod, _path, **kwargs)
                self._watcher(str(self),'200')
                return _result
            except HTTPError as HE:
                self._watcher(str(self), str(HE.response))
                raise

        return self.session.request(self.httpMethod, _path, **kwargs)

    def call_when(self, condition=lambda x:True, call=lambda x: None, step=1, timeout=500, **kwargs):
        _remaining = timeout

        if self._watcher:
            kwargs['info'] = 'call'

        while _remaining > 0:
            _remaining = _remaining - step
            time.sleep(step)
            _res = self.__call__(**kwargs)
            if condition(_res) :
                return call(_res)
            elif kwargs.get('info', None) == 'call':
                kwargs['info'] = 'retry'


        if self._watcher:
            self._watcher(str(self),'timeout')
        return None

    def wait_until(self, condition=lambda x:True, step=1, timeout=60, **kwargs):
        _remaining = timeout

        if self._watcher:
            kwargs['info'] = 'call'

        while _remaining > 0:
            _remaining = _remaining - step
            time.sleep(step)
            _res = self.__call__(**kwargs)
            if condition(_res) :
                return _res
            elif kwargs.get('info', None) == 'call':
                kwargs['info'] = 'retry'

        if self._watcher:
            self._watcher(str(self),'timeout')
        return None

    @property
    def help(self):
        msg = 'Route {} [{}]'.format(self.name, self.httpMethod)
        msg += '\n{}'.format(self.path)
        for _k,_v in self._path_keys.items():
            msg += '\n{:>20} : {}'.format(_k,_v.__doc__)
        msg += '\n'
        print(msg)

    def __repr__(self):
        return '{} <{}> {}:{}'.format(self.__class__.__name__, id(self), self.httpMethod, self.path)

    def __str__(self):
        return '{: >4}:{}'.format(self.httpMethod, self.path)


class Resource(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        """The resource name as defined in the API schema"""
        return "Resource Name"

    def __init__(self,session, watcher=None):
        self.session = session
        self._routes = {}
        for _route in (_m[1] for _m in inspect.getmembers(self.__class__) if inspect.isclass(_m[1]) and issubclass(_m[1], Route)) :
            _routeInstance = _route(session, watcher=watcher)
            _routeName = _route.__name__.lower().replace('_','')
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
