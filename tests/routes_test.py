import unittest
from collections import namedtuple


SessionCls = namedtuple('SessionCls', ['version'])


class RoutesTestCase(unittest.TestCase):

    def setUp(self):
        from tests.data.dummy_resource import TestResource

        self.route_available = TestResource.RouteAvailable
        self.route_future = TestResource.RouteFuture
        self.route_removed = TestResource.RouteRemoved

        self.resourceCls = TestResource

    def test_route_availability(self):
        self.assertFalse(self.route_available.is_available('3.0'))
        self.assertTrue(self.route_available.is_available('3.1'))
        self.assertTrue(self.route_available.is_available('3.2'))

        self.assertFalse(self.route_future.is_available('3.0'))
        self.assertFalse(self.route_future.is_available('3.1'))
        self.assertTrue(self.route_future.is_available('3.2'))

        self.assertTrue(self.route_removed.is_available('3.0'))
        self.assertTrue(self.route_removed.is_available('3.1'))
        self.assertFalse(self.route_removed.is_available('3.2'))

    # def test_route_not_available(self):
    #     self.session = SessionCls(version='3.0')
    #     resource = self.resourceCls(session=self.session, watcher=None)
    #     self.assertFalse(hasattr(resource, self.route_available.get_route_name()))
    #     self.assertFalse(hasattr(resource, self.route_future.get_route_name()))
    #     self.assertTrue(hasattr(resource, self.route_removed.get_route_name()))

    # def test_route_created(self):
    #     self.session = SessionCls(version='3.1')
    #     resource = self.resourceCls(session=self.session, watcher=None)
    #     self.assertTrue(hasattr(resource, self.route_available.get_route_name()))
    #     self.assertFalse(hasattr(resource, self.route_future.get_route_name()))
    #     self.assertTrue(hasattr(resource, self.route_removed.get_route_name()))

    # def test_route_removed(self):
    #     self.session = SessionCls(version='3.2')
    #     resource = self.resourceCls(session=self.session, watcher=None)
    #     self.assertTrue(hasattr(resource, self.route_available.get_route_name()))
    #     self.assertTrue(hasattr(resource, self.route_future.get_route_name()))
    #     self.assertFalse(hasattr(resource, self.route_removed.get_route_name()))
