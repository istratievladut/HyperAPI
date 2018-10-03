from HyperAPI.hdp_api.routes import Resource, Route


class SWPMatchmaking(Resource):
    name = "swpMatchmaking"

    class _getAgents(Route):
        name = "getAgents"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/redeployments/{work_ID}/agents"
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
