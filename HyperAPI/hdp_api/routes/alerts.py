from HyperAPI.hdp_api.routes import Resource, Route


class Alerts(Resource):
    name = "alerts"

    class _getAlerts(Route):
        name = "getAlerts"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/alerts/group"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _computeAlerts(Route):
        name = "computeAlerts"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/alerts/group/{alert_group_ID}/compute"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'alert_group_ID': Route.VALIDATOR_OBJECTID,
        }

    class _ignoreAlerts(Route):
        name = "ignoreAlerts"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/alerts/group/{alert_group_ID}/ignore"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'alert_group_ID': Route.VALIDATOR_OBJECTID,
        }

    class _resolveAlerts(Route):
        name = "resolveAlerts"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/alerts/group/{alert_group_ID}/resolve"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'alert_group_ID': Route.VALIDATOR_OBJECTID,
        }

    class _proposeAlertsResolution(Route):
        name = "proposeAlertsResolution"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/alerts/group/{alert_group_ID}/proposeResolution"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'alert_group_ID': Route.VALIDATOR_OBJECTID,
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

    class _ignoreAlert(Route):
        name = "ignoreAlert"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/alerts/{alert_ID}/ignore"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'alert_ID': Route.VALIDATOR_OBJECTID,
        }

    class _resolveAlert(Route):
        name = "resolveAlert"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/alerts/{alert_ID}/resolve"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'alert_ID': Route.VALIDATOR_OBJECTID,
        }

    class _proposeAlertResolution(Route):
        name = "proposeAlertResolution"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/alerts/{alert_ID}/proposeResolution"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'alert_ID': Route.VALIDATOR_OBJECTID,
        }
