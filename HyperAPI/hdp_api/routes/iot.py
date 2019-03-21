from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class IoT(Resource):
    name = "iotEtlApi"
    available_since = "4.1"
    removed_since = None

    class _getAll(Route):
        name = "getAll"
        httpMethod = Route.GET
        path = "/etl/streams"

    class _details(Route):
        name = "details"
        httpMethod = Route.GET
        path = "/etl/streams/{stream_ID}"
        _path_keys = {
            'stream_ID': Route.VALIDATOR_OBJECTID
        }

    class _create(Route):
        name = "create"
        httpMethod = Route.POST
        path = "/etl/streams/create"

    class _update(Route):
        name = "update"
        httpMethod = Route.POST
        path = "/etl/streams/{stream_ID}/update"
        _path_keys = {
            'stream_ID': Route.VALIDATOR_OBJECTID
        }

    class _delete(Route):
        name = "delete"
        httpMethod = Route.POST
        path = "/etl/streams/{stream_ID}/delete"
        _path_keys = {
            'stream_ID': Route.VALIDATOR_OBJECTID
        }
