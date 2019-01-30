from HyperAPI.hdp_api.routes import Resource, Route


class JoinDatasets(Resource):
    name = "joinDatasets"
    available_since = "3.0"
    removed_since = None

    class _joinDatasets(Route):
        name = "joinDatasets"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/join"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _compareDatasets(Route):
        name = "compareDatasets"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/compare"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }
