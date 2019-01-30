from HyperAPI.hdp_api.routes import Resource, Route


class Exports(Resource):
    name = "Exports"
    available_since = "3.0"
    removed_since = None

    class _export(Route):
        name = "export"
        httpMethod = Route.GET
        path = "/exports/{file_name}"
        _path_keys = {
            'file_name': Route.VALIDATOR_ANY,
        }
