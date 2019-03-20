class DummySession(object):
    # Class simulating a session
    def __init__(self, version):
        self.version = version

    def request(self, httpMethod, path, **kwargs):
        kwargs.update({'httpMethod': httpMethod, 'path': path})
        return kwargs
