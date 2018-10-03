from HyperAPI.hdp_api.routes import Resource, Route


class Query(Resource):
    name = "Query"

    class _GetQuerybyqueryname(Route):
        name = "Get Query by query name"
        httpMethod = Route.GET
        path = "/query/{project_ID}/{query_name}/getQuery"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'query_name': Route.VALIDATOR_ANY,
        }

    class _Getqueriesofaproject(Route):
        name = "Get queries of a project"
        httpMethod = Route.GET
        path = "/query/{project_ID}/getQueries"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _Deletequery(Route):
        name = " Delete query"
        httpMethod = Route.POST
        path = "/query/{project_ID}/{dataset_ID}/{query_name}/deleteQuery"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'query_name': Route.VALIDATOR_ANY,
        }
