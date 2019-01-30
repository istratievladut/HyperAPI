from HyperAPI.hdp_api.routes import Resource, Route


class TempData(Resource):
    name = "tempData"
    available_since = "3.0"
    removed_since = None

    class _tempData(Route):
        name = "tempData"
        httpMethod = Route.GET
        path = "/tempData"
