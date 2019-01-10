from HyperAPI.hdp_api.routes import Resource, Route


class ThirdParties(Resource):
    name = "3rdParties"

    class _get3rdPartiesSettings(Route):
        name = "get3rdPartiesSettings"
        httpMethod = Route.GET
        path = "/3rdparties"
