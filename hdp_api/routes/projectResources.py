from hypercube_api.hdp_api.routes import Resource, Route


class ProjectResources(Resource):
    name = "ProjectResources"

    class _getProjectResource(Route):
        name = "getProjectResource"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/resources"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }
