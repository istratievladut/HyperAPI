from HyperAPI.hdp_api.routes import Resource, Route


class TempData(Resource):
    name = "tempData"

    class _tempData(Route):
        name = "tempData"
        httpMethod = Route.GET
        path = "/tempData"
