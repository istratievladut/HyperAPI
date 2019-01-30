from HyperAPI.hdp_api.routes import Resource, Route


class Authentication(Resource):
    name = "Authentication"
    available_since = "3.0"
    removed_since = None

    class _login(Route):
        name = "login"
        httpMethod = Route.POST
        path = "/auth/login"

    class _logout(Route):
        name = "logout"
        httpMethod = Route.POST
        path = "/auth/logout"
