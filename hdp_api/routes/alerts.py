from HyperAPI.hdp_api.routes import Resource, Route


class Alerts(Resource):
    name = "alerts"

    class _getAlerts(Route):
        name = "getAlerts"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/alerts"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }
        
    class _getAlert(Route):
        name = "getAlert"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/alerts/{alert_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'alert_ID': Route.VALIDATOR_OBJECTID,
        }

    class _updateAlert(Route):
        name = "updateAlert"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/alerts/{alert_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'alert_ID': Route.VALIDATOR_OBJECTID,
        }

    class _computeAlert(Route):
        name = "computeAlert"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/alerts/{alert_ID}/compute"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'alert_ID': Route.VALIDATOR_OBJECTID,
        }
