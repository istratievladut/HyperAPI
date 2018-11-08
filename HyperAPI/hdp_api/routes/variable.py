from HyperAPI.hdp_api.routes import Resource, Route


class Variable(Resource):
    name = "Variable"

    class _Bins(Route):
        name = "Bins"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/bin/{var_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'var_ID': Route.VALIDATOR_OBJECTID,
        }

    class _variableTagsBins(Route):
        name = "variableTagsBins"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/tags/variablesTags"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getVariable(Route):
        name = "getVariable"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/variables"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _addVariableValidation(Route):
        name = "addVariableValidation"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/variables/validation"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _deleteVariableValidation(Route):
        name = "removeVariableValidation"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/variables/validation/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getVariableAndTags(Route):
        name = "getVariableAndTags"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/variablesAndTags"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _metatype(Route):
        name = "metatype"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/tags/metatype"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }
