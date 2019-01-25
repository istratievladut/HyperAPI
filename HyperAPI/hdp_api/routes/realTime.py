from HyperAPI.hdp_api.routes import Resource, Route


class RealTime(Resource):
    name = "realTimeSocket"

    class _getRealTimeSettings(Route):
        name = "getRealTimeSettings"
        httpMethod = Route.GET
        path = "/realTimeSocket"
