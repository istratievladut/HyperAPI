from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class OptimProcess(Resource):
    name = "optimProcess"
    available_since = "1.0"
    removed_since = None

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

    class _publishControlChartToEtl(Route):
        name = "PublishControlChartToEtl"
        available_since = '3.3'
        httpMethod = Route.POST
        path = "/optimProcess/projects/{project_ID}/controlCharts/{controlChart_ID}/etlpublish"
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

    class _getAllRealtimeViz(Route):
        name = "getAllRealtimeViz"
        httpMethod = Route.GET
        path = "/optimProcess/projects/{project_ID}/realtimeViz"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _getOneRealtimeViz(Route):
        name = "getOneRealtimeViz"
        httpMethod = Route.GET
        path = "/optimProcess/projects/{project_ID}/realtimeViz/{realtimeViz_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'realtimeViz_ID': Route.VALIDATOR_OBJECTID
        }

    class _postRealtimeViz(Route):
        name = "postRealtimeViz"
        httpMethod = Route.POST
        path = "/optimProcess/projects/{project_ID}/realtimeViz"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _renameRealtimeViz(Route):
        name = "renameRealtimeViz"
        httpMethod = Route.POST
        path = "/optimProcess/projects/{project_ID}/realtimeViz/{realtimeViz_ID}/rename"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'realtimeViz_ID': Route.VALIDATOR_OBJECTID
        }

    class _deleteRealtimeViz(Route):
        name = "deleteRealtimeViz"
        httpMethod = Route.POST
        path = "/optimProcess/projects/{project_ID}/realtimeViz/{realtimeViz_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'realtimeViz_ID': Route.VALIDATOR_OBJECTID
        }
