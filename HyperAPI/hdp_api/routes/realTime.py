from HyperAPI.hdp_api.routes import Resource, Route
from HyperAPI.hdp_api.routes.base.version_management import available_since


class RealTime(Resource):
    name = "realTimeSocket"

    @available_since("3.6")
    class _getRealTimeSettings(Route):
        name = "getRealTimeSettings"
        httpMethod = Route.GET
        path = "/realTimeSocket"
