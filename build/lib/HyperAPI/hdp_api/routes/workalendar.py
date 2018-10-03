from HyperAPI.hdp_api.routes import Resource, Route


class Workalendar(Resource):
    name = "workalendar"

    class _getWorkalendarCountries(Route):
        name = "getWorkalendarCountries"
        httpMethod = Route.GET
        path = "/workalendar/countries"
