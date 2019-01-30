from HyperAPI.hdp_api.routes import Resource, Route


class DatasetReshapes(Resource):
    name = "datasetReshapes"
    available_since = "3.0"
    removed_since = None

    class _getReshapes(Route):
        name = "getReshapes"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/reshapes"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _createReshape(Route):
        name = "createReshape"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/reshapes"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getReshape(Route):
        name = "getReshape"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/reshapes/{reshape_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'reshape_ID': Route.VALIDATOR_OBJECTID,
        }

    class _updateReshape(Route):
        name = "updateReshape"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/reshapes/{reshape_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'reshape_ID': Route.VALIDATOR_OBJECTID,
        }

    class _deleteReshape(Route):
        name = "deleteReshape"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/reshapes/{reshape_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'reshape_ID': Route.VALIDATOR_OBJECTID,
        }

    class _inheritReshape(Route):
        name = "inheritReshape"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/reshapes/{reshape_ID}/inherit"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'reshape_ID': Route.VALIDATOR_OBJECTID,
        }

    class _publishReshapeToEtl(Route):
        name = "publishReshapeToEtl"
        available_since = '3.3'
        httpMethod = Route.POST
        path = "/projects/{project_ID}/reshapes/{reshape_ID}/etlpublish"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'reshape_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getReshapeGroups(Route):
        name = "getReshapeGroups"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/reshapes/{reshape_ID}/groups"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'reshape_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getReshapesGroups(Route):
        name = "getReshapesGroups"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/reshapes/groups"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _createReshapeGroup(Route):
        name = "createReshapeGroup"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/reshapes/groups"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getReshapeGroup(Route):
        name = "getReshapeGroup"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/reshapes/groups/{group_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'group_ID': Route.VALIDATOR_OBJECTID,
        }

    class _updateReshapeGroup(Route):
        name = "updateReshapeGroup"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/reshapes/groups/{group_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'group_ID': Route.VALIDATOR_OBJECTID,
        }

    class _deleteReshapeGroup(Route):
        name = "deleteReshapeGroup"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/reshapes/groups/{group_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'group_ID': Route.VALIDATOR_OBJECTID,
        }

    class _describeReshape(Route):
        name = "describeReshape"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/reshapes/describe"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getReshapeDescription(Route):
        name = "getReshapeDescription"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/reshapes/describe"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _applyReshape(Route):
        name = "applyReshape"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/reshapes/{reshape_ID}/apply"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'reshape_ID': Route.VALIDATOR_OBJECTID,
        }

    class _removeReshape(Route):
        name = "removeReshape"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/reshapes/remove"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _proposeAlterations(Route):
        name = "proposeAlterations"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/reshapes/proposeAlterations"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }
