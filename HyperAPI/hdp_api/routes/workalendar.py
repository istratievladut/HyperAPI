from HyperAPI.hdp_api.routes import Resource, Route


class Workalendar(Resource):
    name = "workalendar"
    available_since = "3.0"
    removed_since = None

    class _getWorkalendarCountries(Route):
        name = "getWorkalendarCountries"
        httpMethod = Route.GET
        path = "/workalendar/countries"
