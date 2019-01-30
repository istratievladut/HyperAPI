from HyperAPI.hdp_api.routes import Resource, Route


class DatasetResources(Resource):
    name = "DatasetResources"
    available_since = "3.0"
    removed_since = None

    class _getDatasetResource(Route):
        name = "getDatasetResource"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/resources"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }
