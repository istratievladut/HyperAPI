from HyperAPI.hdp_api.routes import Resource, Route


class Visualization(Resource):
    name = "Visualization"

    class _List(Route):
        name = "List"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/visualizations"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getVisualisation(Route):
        name = "getVisualisation"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/visualizations/{visualization_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'visualization_ID': Route.VALIDATOR_OBJECTID,
        }

    class _Create(Route):
        name = "Create"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/visualizations"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _CreateMany(Route):
        name = "CreateMany"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/visualizations/createMany"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _Update(Route):
        name = "Update"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/visualizations/{visualization_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'visualization_ID': Route.VALIDATOR_OBJECTID,
        }

    class _Rename(Route):
        name = "Rename"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/visualizations/{visualization_ID}/rename"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'visualization_ID': Route.VALIDATOR_OBJECTID,
        }

    class _Delete(Route):
        name = "Delete"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/visualizations/{visualization_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'visualization_ID': Route.VALIDATOR_OBJECTID,
        }
