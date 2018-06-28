from hypercube_api.hdp_api.routes import Resource, Route


class Color(Resource):
    name = "Color"

    class _getColors(Route):
        name = "get Project Color sList"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/colors"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _updateColors(Route):
        name = "update Color"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/colors"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _deleteColors(Route):
        name = "delete Color"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/colors/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }
