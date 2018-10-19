from HyperAPI.hdp_api.routes import Resource, Route


class SmartDataViz(Resource):
    name = "SmartDataViz"

    class _getSmartDataViz(Route):
        name = "getSmartDataViz"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/smartDataViz/{smartDataViz_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'smartDataViz_ID': Route.VALIDATOR_OBJECTID,
        }

    class _computeSmartDataViz(Route):
        name = "computeSmartDataViz"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/smartDataViz/"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getSmartDataVizs(Route):
        name = "getSmartDataVizs"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/smartDataViz/"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _deleteSmartDataViz(Route):
        name = "deleteSmartDataViz"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/smartDataViz/{smartDataViz_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'smartDataViz_ID': Route.VALIDATOR_OBJECTID,
        }
