from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class Anaplan(Resource):
    name = "anaplan"
    available_since = "4.2.6"
    removed_since = None

    class _getWorkspaces(Route):
        name = "getWorkspaces"
        httpMethod = Route.GET
        path = "/anaplan/workspaces"

    class _getModels(Route):
        name = "getModels"
        httpMethod = Route.GET
        path = "/anaplan/models"

    class _getFiles(Route):
        name = "getFiles"
        httpMethod = Route.GET
        path = "/anaplan/workspaces/{workspace_id}/model/{model_id}",
        _path_keys = {
            'workspace_id': Route.VALIDATOR_OBJECTID,
            'model_id': Route.VALIDATOR_OBJECTID
        }
        
    class _login(Route):
        name = "login"
        httpMethod = Route.POST
        path = "/anaplan/login"
