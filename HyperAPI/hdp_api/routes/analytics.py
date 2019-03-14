from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class Analytics(Resource):
    name = "analytics"
    available_since = "1.0"
    removed_since = None

    class _newPageView(Route):
        name = "newPageView"
        httpMethod = Route.POST
        path = "/analytics/pageView"
