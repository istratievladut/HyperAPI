from HyperAPI.hdp_api.routes import Resource, Route


class Dashboards(Resource):
    name = "Dashboards"
    available_since = "3.0"
    removed_since = None

    class _Dashboards(Route):
        name = "getDashboards"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/dashboards"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    @available_since('3.1')
    class _ProjectDashboards(Route):
        name = "getProjectDashboards"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/dashboards"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
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

    @available_since('3.1')
    class _GetProjectDashboard(Route):
        name = "getProjectDashboard"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/dashboards/{dashboard_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
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

    @available_since('3.1')
    class _addProjectDashboard(Route):
        name = "addProjectDashboard"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/dashboards"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
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

    @available_since('3.1')
    class _updateProjectDashboard(Route):
        name = "updateProjectDashboard"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/dashboards/{dashboard_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
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

    @available_since('3.1')
    class _deleteProjectDashboard(Route):
        name = "deleteProjectDashboard"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/dashboards/{dashboard_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dashboard_ID': Route.VALIDATOR_OBJECTID
        }
