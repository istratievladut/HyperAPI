from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class TimeSeriesAnalysis(Resource):
    name = "TimeSeriesAnalysis"
    available_since = "3.0"
    removed_since = None

    class _listTimeSeriesAnalysis(Route):
        name = "listTimeSeriesAnalysis"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/timeSeriesAnalysis/"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _createTimeSeriesAnalysis(Route):
        name = "createTimeSeriesAnalysis"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/timeSeriesAnalysis/"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _updateTimeSeriesAnalysis(Route):
        name = "updateTimeSeriesAnalysis"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/timeSeriesAnalysis/{analysis_ID}/update"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'analysis_ID': Route.VALIDATOR_OBJECTID
        }

    class _deleteTimeSeriesAnalysis(Route):
        name = "deleteTimeSeriesAnalysis"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/timeSeriesAnalysis/{analysis_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'analysis_ID': Route.VALIDATOR_OBJECTID
        }

    class _getTimeSeriesAnalysis(Route):
        name = "getTimeSeriesAnalysis"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/timeSeriesAnalysis/{analysis_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'analysis_ID': Route.VALIDATOR_OBJECTID
        }
