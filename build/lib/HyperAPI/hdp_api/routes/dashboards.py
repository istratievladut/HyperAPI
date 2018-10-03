from HyperAPI.hdp_api.routes import Resource, Route


class Dashboards(Resource):
    name = "Dashboards"

    class _Dashboards(Route):
        name = "getDashboards"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/dashboards"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _GetDashboard(Route):
        name = "getDashboard"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/dashboards/{dashboard_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'dashboard_ID': Route.VALIDATOR_OBJECTID
        }

    class _addDashboard(Route):
        name = "addDashboard"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/dashboards"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _updateDashboard(Route):
        name = "updateDashboard"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/dashboards/{dashboard_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'dashboard_ID': Route.VALIDATOR_OBJECTID
        }

    class _deleteDashboard(Route):
        name = "deleteDashboard"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/dashboards/{dashboard_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'dashboard_ID': Route.VALIDATOR_OBJECTID
        }
