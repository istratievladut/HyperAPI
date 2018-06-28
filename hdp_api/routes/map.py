from hypercube_api.hdp_api.routes import Resource, Route


class Map(Resource):
    name = "Map"

    class _Retrievedataforgeomapping(Route):
        name = "Retrieve data for geo mapping"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/mapping/{type}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'type': Route.VALIDATOR_ANY,
        }
