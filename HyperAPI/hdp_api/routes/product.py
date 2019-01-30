from HyperAPI.hdp_api.routes import Resource, Route


class Product(Resource):
    name = "Product"
    available_since = "3.0"
    removed_since = None

    class _info(Route):
        name = "info"
        httpMethod = Route.GET
        path = "/product/info"
        _path_keys = {
        }
