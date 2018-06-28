from hypercube_api.hdp_api.routes import Resource, Route


class Authentication(Resource):
    name = "Authentication"

    class _login(Route):
        name = "login"
        httpMethod = Route.POST
        path = "/auth/login"

    class _logout(Route):
        name = "logout"
        httpMethod = Route.POST
        path = "/auth/logout"
