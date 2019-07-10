from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class Admin(Resource):
    name = "admin"
    available_since = "4.2.5"
    removed_since = None

    class _getUserWorksOverrides(Route):
        name = "getUserWorksOverrides"
        httpMethod = Route.GET
        path = "/admin/user/{user_ID}/overrides"
        _path_keys = {
            'user_ID': Route.VALIDATOR_OBJECTID
        }
    
    class _getGroupWorksOverrides(Route):
        name = "getGroupWorksOverrides"
        httpMethod = Route.GET
        path = "/admin/group/{group_ID}/overrides"
        _path_keys = {
            'group_ID': Route.VALIDATOR_OBJECTID
        }
