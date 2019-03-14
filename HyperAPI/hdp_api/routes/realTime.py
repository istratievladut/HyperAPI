from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class RealTime(Resource):
    name = "realTimeSocket"
    available_since = "3.4"
    removed_since = None

    class _getRealTimeSettings(Route):
        name = "getRealTimeSettings"
        available_since = '3.6'
        httpMethod = Route.GET
        path = "/realTimeSocket"
