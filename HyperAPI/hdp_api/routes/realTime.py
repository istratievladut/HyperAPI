from HyperAPI.hdp_api.routes import Resource, Route


class RealTime(Resource):
    name = "realTimeSocket"
    available_since = "3.0"
    removed_since = None

    class _getRealTimeSettings(Route):
        name = "getRealTimeSettings"
        available_since = '3.6'
        httpMethod = Route.GET
        path = "/realTimeSocket"
