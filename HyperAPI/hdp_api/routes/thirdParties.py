from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class ThirdParties(Resource):
    name = "3rdParties"
    available_since = "1.0"
    removed_since = None
    unavailable_on = ["2.0", "3.0.2"]

    class _get3rdPartiesSettings(Route):
        name = "get3rdPartiesSettings"
        httpMethod = Route.GET
        path = "/3rdparties"
