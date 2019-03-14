from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class Exports(Resource):
    name = "Exports"
    available_since = "1.0"
    removed_since = None

    class _export(Route):
        name = "export"
        httpMethod = Route.GET
        path = "/exports/{file_name}"
        _path_keys = {
            'file_name': Route.VALIDATOR_ANY,
        }
