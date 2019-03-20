from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class Workalendar(Resource):
    name = "workalendar"
    available_since = "1.0"
    removed_since = None

    class _getWorkalendarCountries(Route):
        name = "getWorkalendarCountries"
        httpMethod = Route.GET
        path = "/workalendar/countries"
