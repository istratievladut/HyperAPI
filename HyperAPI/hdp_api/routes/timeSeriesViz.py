from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class TimeSeriesViz(Resource):
    name = "TimeSeriesViz"
    available_since = "1.0"
    removed_since = None

    class _listTimeSeriesViz(Route):
        name = "listTimeSeriesViz"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/timeSeries/list"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _createTimeSeriesViz(Route):
        name = "createTimeSeriesViz"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/timeSeries/new"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _updateTimeSeriesViz(Route):
        name = "updateTimeSeriesViz"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/timeSeries/update"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _deleteTimeSeriesViz(Route):
        name = "deleteTimeSeriesViz"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/timeSeries/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }
