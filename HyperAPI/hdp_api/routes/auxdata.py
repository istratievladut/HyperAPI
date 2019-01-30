from HyperAPI.hdp_api.routes import Resource, Route


class AuxData(Resource):
    name = "auxdata"
    available_since = "3.0"
    removed_since = None

    class _getProjectAuxData(Route):
        name = "getProjectAuxData"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/auxdata"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _createAuxData(Route):
        name = "createAuxData"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/auxdata"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getAuxData(Route):
        name = "getAuxData"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/auxdata/{auxdata_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'auxdata_ID': Route.VALIDATOR_OBJECTID,
        }

    class _updateAuxData(Route):
        name = "updateAuxData"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/auxdata/{auxdata_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'auxdata_ID': Route.VALIDATOR_OBJECTID,
        }

    class _deleteAuxData(Route):
        name = "deleteAuxData"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/auxdata/{auxdata_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'auxdata_ID': Route.VALIDATOR_OBJECTID,
        }

    class _exportAuxData(Route):
        name = "exportAuxData"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/auxdata/{auxdata_ID}/export"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'auxdata_ID': Route.VALIDATOR_OBJECTID,
        }

    class _viewAuxData(Route):
        name = "viewAuxData"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/auxdata/{auxdata_ID}/view"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'auxdata_ID': Route.VALIDATOR_OBJECTID,
        }

    class _listAuxDataGroups(Route):
        name = "listAuxDataGroups"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/auxdata/groups"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _copyAuxData(Route):
        name = "copyAuxData"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/auxdata/{auxdata_ID}/copy"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'auxdata_ID': Route.VALIDATOR_OBJECTID,
        }

    class _listAuxDataElems(Route):
        name = "listAuxDataElems"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/auxdata/{auxdata_ID}/listelems"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'auxdata_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getAuxDataMatrices(Route):
        name = "getAuxDataMatrices"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/auxdata/{auxdata_ID}/matrices"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'auxdata_ID': Route.VALIDATOR_OBJECTID,
        }

    class _updateAuxDataMatrices(Route):
        name = "updateAuxDataMatrices"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/auxdata/{auxdata_ID}/matrices"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'auxdata_ID': Route.VALIDATOR_OBJECTID,
        }

    class _exportAuxDataMatrices(Route):
        name = "exportAuxDataMatrices"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/auxdata/{auxdata_ID}/exportMatrices/{work_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'auxdata_ID': Route.VALIDATOR_OBJECTID,
            'work_ID': Route.VALIDATOR_OBJECTID,
        }

    class _importAuxDataMatrices(Route):
        name = "importAuxDataMatrices"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/auxdata/{auxdata_ID}/importMatrices"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'auxdata_ID': Route.VALIDATOR_OBJECTID,
        }

    class _validateAuxData(Route):
        name = "validateAuxData"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/auxdata/validate"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }
