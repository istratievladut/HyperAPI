from HyperAPI.hdp_api.routes import Resource, Route


class ThirdParties(Resource):
    name = "3rdParties"
    available_since = "3.0"
    removed_since = None

    class _get3rdPartiesSettings(Route):
        name = "get3rdPartiesSettings"
        httpMethod = Route.GET
        path = "/3rdparties"
