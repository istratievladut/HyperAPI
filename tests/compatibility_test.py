import unittest
from collections import namedtuple


SessionCls = namedtuple('SessionCls', ['version'])


class RoutesTestCase(unittest.TestCase):

    def setUp(self):
        from tests.data.dummy_resource import TestResource

        self.route_compatible = TestResource.RouteCompatible

        self.resourceCls = TestResource

    # def test_route_none(self):
    #     self.session = SessionCls(version='2.9')
    #     resource = self.resourceCls(session=self.session, watcher=None)
    #     self.assertFalse(hasattr(resource, self.route_compatible.get_route_name()))

    # def test_route_base(self):
    #     self.session = SessionCls(version='3.0')
    #     resource = self.resourceCls(session=self.session, watcher=None)
    #     self.assertTrue(hasattr(resource, self.route_compatible.get_route_name()))

    # def test_route_args(self):
    #     self.session = SessionCls(version='3.1')
    #     resource = self.resourceCls(session=self.session, watcher=None)
    #     self.assertTrue(hasattr(resource, self.route_compatible.get_route_name()))

    # def test_route_convert(self):
    #     self.session = SessionCls(version='3.2')
    #     resource = self.resourceCls(session=self.session, watcher=None)
    #     self.assertTrue(hasattr(resource, self.route_compatible.get_route_name()))

    # def test_route_removed(self):
    #     self.session = SessionCls(version='3.3')
    #     resource = self.resourceCls(session=self.session, watcher=None)
    #     self.assertFalse(hasattr(resource, self.route_compatible.get_route_name()))
