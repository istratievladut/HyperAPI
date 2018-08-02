from HyperAPI.hdp_api.routes import Resource, Route


class SimpleLift(Resource):
    name = "Simple Lift"

    class _NewSimpleLift(Route):
        name = "New Simple Lift"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/tasks/new"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _newSimpleLiftName(Route):
        name = "new SimpleLift Name"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/simplelifts/newSimpleLiftName"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _GetglobalJSONfile(Route):
        name = "Get global JSON file"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/simplelifts/{task_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'task_ID': Route.VALIDATOR_OBJECTID,
        }

    class _GetvariableJSONfile(Route):
        name = "Get variable JSON file"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/simplelifts/{task_ID}/variable/{column_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'task_ID': Route.VALIDATOR_OBJECTID,
            'column_ID': Route.VALIDATOR_INT,
        }

    class _GetCSVfile(Route):
        name = "Get CSV file"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/simplelifts/{task_ID}/exportSimplelift"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'task_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getSimpleLift(Route):
        name = "getSimpleLift"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/simplelifts/{simpleLift_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'simpleLift_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getSimpleLifts(Route):
        name = "getSimpleLifts"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/simplelifts"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }
