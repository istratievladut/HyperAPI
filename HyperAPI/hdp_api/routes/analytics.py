from HyperAPI.hdp_api.routes import Resource, Route


class Analytics(Resource):
    name = "analytics"

    class _newPageView(Route):
        name = "newPageView"
        httpMethod = Route.POST
        path = "/analytics/pageView"
