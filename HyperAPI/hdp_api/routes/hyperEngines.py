from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class HyperEngines(Resource):
    name = "hyperEngines"
    available_since = "1.0"
    removed_since = None

    class _hyperenginesListUp(Route):
        name = "hyperenginesListUp"
        httpMethod = Route.GET
        path = "/hyperEngine/list"

    class _clusterInformation(Route):
        name = "clusterInformation"
        httpMethod = Route.GET
        path = "/hyperEngine/cluster"

    class _mongoLatency(Route):
        name = "mongoLatency"
        httpMethod = Route.GET
        path = "/hyperEngine/mongoLatency"

    class _nbInstances(Route):
        name = "nbInstances"
        httpMethod = Route.GET
        path = "/hyperEngine/nbInstances"
