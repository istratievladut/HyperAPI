from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class ProjectResources(Resource):
    name = "ProjectResources"
    available_since = "3.0"
    removed_since = None

    class _getProjectResource(Route):
        name = "getProjectResource"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/resources"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }
