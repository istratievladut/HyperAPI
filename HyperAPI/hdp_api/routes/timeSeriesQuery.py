from HyperAPI.hdp_api.routes import Resource, Route


class TimeSeriesQuery(Resource):
    name = "TimeSeriesQuery"

    class _timeSeriesQueryTags(Route):
        name = "timeSeriesQueryTags"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/timeSeriesQuery/tags"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _timeSeriesQueryDatapoints(Route):
        name = "timeSeriesQueryDatapoints"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/timeSeriesQuery/datapoints"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _timeSeriesQueryAggregations(Route):
        name = "timeSeriesQueryAggregations"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/timeSeriesQuery/aggregations"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _timeSeriesAddDataset(Route):
        name = "timeSeriesAddDataset"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/timeSeriesQuery/newdataset"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }
