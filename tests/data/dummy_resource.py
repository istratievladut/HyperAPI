from HyperAPI.hdp_api.routes import Resource, Route


class TestResource(Resource):
    name = "TestResource"
    available_since = "1.0"
    removed_since = "4.0"

    class RouteAvailable(Route):
        name = "Route Available"
        httpMethod = Route.GET
        path = "/route/available"
        available_since = "3.1"

    class RouteFuture(Route):
        name = "Route Future"
        httpMethod = Route.GET
        path = "/route/future"
        available_since = "3.2"

    class RouteRemoved(Route):
        name = "Route Removed"
        httpMethod = Route.GET
        path = "/route/removed"
        removed_since = "3.2"

    class RouteCompatible(Route):
        name = "Route Compatible 3.0"
        httpMethod = Route.GET
        path = "/route/compatible/v0"
        available_since = "3.0"
        removed_since = "3.1"

    # RouteCompatible.reroute_to(name="Route Compatible 3.1", path="/route/compatible/v1", httpMethod=Route.POST, available_since="3.1", removed_since="3.2")
    # RouteCompatible.reroute_to(name="Route Compatible 3.2", available_since="3.2", removed_since="3.3")
