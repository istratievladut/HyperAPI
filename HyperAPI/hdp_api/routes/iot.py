from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class IotEtlApi(Resource):
    name = "iotEtlApi"
    available_since = "4.1"
    removed_since = None

    class _getAllStreams(Route):
        name = "getAllStreams"
        httpMethod = Route.GET
        path = "/etl/streams"

    class _getStream(Route):
        name = "getStream"
        httpMethod = Route.GET
        path = "/etl/streams/{stream_ID}"
        _path_keys = {
            'stream_ID': Route.VALIDATOR_OBJECTID
        }

    class _createStream(Route):
        name = "createStream"
        httpMethod = Route.POST
        path = "/etl/streams/create"

    class _updateStream(Route):
        name = "updateStream"
        httpMethod = Route.POST
        path = "/etl/streams/{stream_ID}/update"
        _path_keys = {
            'stream_ID': Route.VALIDATOR_OBJECTID
        }

    class _deleteStream(Route):
        name = "deleteStream"
        httpMethod = Route.POST
        path = "/etl/streams/{stream_ID}/delete"
        _path_keys = {
            'stream_ID': Route.VALIDATOR_OBJECTID
        }
