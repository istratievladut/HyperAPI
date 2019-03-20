from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class Map(Resource):
    name = "Map"
    available_since = "1.0"
    removed_since = None

    class _Retrievedataforgeomapping(Route):
        name = "Retrieve data for geo mapping"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/mapping/{type}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'type': Route.VALIDATOR_ANY,
        }
