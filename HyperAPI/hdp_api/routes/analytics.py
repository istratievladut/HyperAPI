from HyperAPI.hdp_api.routes import Resource, Route


class Analytics(Resource):
    name = "analytics"
    available_since = "3.0"
    removed_since = None

    class _newPageView(Route):
        name = "newPageView"
        httpMethod = Route.POST
        path = "/analytics/pageView"
