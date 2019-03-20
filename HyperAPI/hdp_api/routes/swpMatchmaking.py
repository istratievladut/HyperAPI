from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class SWPMatchmaking(Resource):
    name = "swpMatchmaking"
    available_since = "3.0"
    removed_since = None

    class _getAgents(Route):
        name = "getAgents"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/redeployments/{work_ID}/agents"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'work_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getOptimizationDetail(Route):
        name = "getOptimizationDetail"
        httpMethod = Route.GET
        available_since = "3.1"
        path = "/projects/{project_ID}/redeployments/{work_ID}/optimizationDetail"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'work_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getMatches(Route):
        name = "getMatches"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/redeployments/{work_ID}/agents/{agent_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'work_ID': Route.VALIDATOR_OBJECTID,
            'agent_ID': Route.VALIDATOR_ANY,
        }
