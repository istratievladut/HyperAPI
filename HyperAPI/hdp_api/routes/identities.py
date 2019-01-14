from HyperAPI.hdp_api.routes import Resource, Route


class Identities(Resource):
    name = "Identities"

    class _getAllIdentities(Route):
        name = "Get all identities"
        httpMethod = Route.GET
        path = "/identities"

    class _getAllUsers(Route):
        name = "Get all users"
        httpMethod = Route.GET
        path = "/identities/users"

    class _addUser(Route):
        name = "Add a user"
        httpMethod = Route.POST
        path = "/identities/users"

    class _updateUser(Route):
        name = "Update a user"
        httpMethod = Route.POST
        path = "/identities/users/{user_ID}"
        _path_keys = {
            'user_ID': Route.VALIDATOR_OBJECTID
        }

    class _getAllGroups(Route):
        name = "Get all groups"
        httpMethod = Route.GET
        path = "/identities/groups"

    class _addGroup(Route):
        name = "Add a new group"
        httpMethod = Route.POST
        path = "/identities/groups"

    class _updateGroup(Route):
        name = "Update a group"
        httpMethod = Route.POST
        path = "/identities/groups/{group_ID}"
        _path_keys = {
            'group_ID': Route.VALIDATOR_OBJECTID
        }

    class _getIdentityById(Route):
        name = "Get an identity"
        httpMethod = Route.GET
        path = "/identities/{identity_ID}"
        _path_keys = {
            'identity_ID': Route.VALIDATOR_OBJECTID
        }

    class _deleteIdentity(Route):
        name = "Delete an identity"
        httpMethod = Route.POST
        path = "/identities/{identity_ID}/delete"
        _path_keys = {
            'identity_ID': Route.VALIDATOR_OBJECTID
        }
    
    class _getAllUserInfos(Route):
        name = "Get all user infos"
        httpMethod = Route.GET
        path = "/identities/users/info"
