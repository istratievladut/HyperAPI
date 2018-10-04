from HyperAPI.hdp_api.routes import Resource, Route


class Settings(Resource):
    name = "Settings"

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
