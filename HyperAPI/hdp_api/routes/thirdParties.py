from HyperAPI.hdp_api.routes import Resource, Route
from HyperAPI.hdp_api.routes.base.version_management import available_since


class ThirdParties(Resource):
    name = "3rdParties"

    @available_since('3.4')
    class _get3rdPartiesSettings(Route):
        name = "get3rdPartiesSettings"
        httpMethod = Route.GET
        path = "/3rdparties"
