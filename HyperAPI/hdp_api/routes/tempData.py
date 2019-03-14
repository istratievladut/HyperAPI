from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class TempData(Resource):
    name = "tempData"
    available_since = "1.0"
    removed_since = None

    class _tempData(Route):
        name = "tempData"
        httpMethod = Route.GET
        path = "/tempData"
