from HyperAPI.hdp_api.routes import Resource, Route


class Reports(Resource):
    name = "Reports"

    class _exportDatasetReports(Route):
        name = "exportDatasetReports"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/reports"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }
