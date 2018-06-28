from hypercube_api.hdp_api.routes import Resource, Route


class OptimProcess(Resource):
    name = "optimProcess"

    class _getSandboxDataForControlChart(Route):
        name = "getSandboxDataForControlChart"
        httpMethod = Route.GET
        path = "/optimProcess/projects/{project_ID}/controlCharts/{controlChart_ID}/data"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'controlChart_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getAllControlChart(Route):
        name = "getAllControlChart"
        httpMethod = Route.GET
        path = "/optimProcess/projects/{project_ID}/controlCharts"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getOneControlChart(Route):
        name = "getOneControlChart"
        httpMethod = Route.GET
        path = "/optimProcess/projects/{project_ID}/controlCharts/{controlChart_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'controlChart_ID': Route.VALIDATOR_OBJECTID,
        }

    class _postControlChart(Route):
        name = "postControlChart"
        httpMethod = Route.POST
        path = "/optimProcess/projects/{project_ID}/controlCharts"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _updateControlChart(Route):
        name = "updateControlChart"
        httpMethod = Route.POST
        path = "/optimProcess/projects/{project_ID}/controlCharts/{controlChart_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'controlChart_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getOPDashboards(Route):
        name = "getOPDashboards"
        httpMethod = Route.GET
        path = "/optimProcess/projects/{project_ID}/dashboards"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _postDashboard(Route):
        name = "postDashboard"
        httpMethod = Route.POST
        path = "/optimProcess/projects/{project_ID}/dashboards"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _postGraph(Route):
        name = "postGraph"
        httpMethod = Route.POST
        path = "/optimProcess/projects/{project_ID}/dashboards/{dashboard_ID}/graphs"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dashboard_ID': Route.VALIDATOR_OBJECTID,
        }

    class _deleteGraph(Route):
        name = "deleteGraph"
        httpMethod = Route.POST
        path = "/optimProcess/projects/{project_ID}/dashboards/{dashboard_ID}/graphs/remove"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dashboard_ID': Route.VALIDATOR_OBJECTID,
        }

    class _deleteOPDashboard(Route):
        name = "deleteOPDashboard"
        httpMethod = Route.POST
        path = "/optimProcess/projects/{project_ID}/dashboards/{dashboard_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dashboard_ID': Route.VALIDATOR_OBJECTID,
        }
