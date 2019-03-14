from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class Settings(Resource):
    name = "Settings"
    available_since = "1.0"
    removed_since = None

    class _getUserSettings(Route):
        name = "Get User Settings"
        httpMethod = Route.GET
        path = "/settings"

    class _updateUserSettings(Route):
        name = "Update User Settings"
        httpMethod = Route.POST
        path = "/settings"

    class _resetUserApiToken(Route):
        name = "Reset a user ApiToken"
        httpMethod = Route.POST
        path = "/settings/resetApiToken"
