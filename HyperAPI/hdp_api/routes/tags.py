from HyperAPI.hdp_api.routes import Resource, Route


class Tags(Resource):
    name = "Tags"
    available_since = "3.0"
    removed_since = None

    class _addtag(Route):
        name = "add tag"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/variables/addTag"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _renameTag(Route):
        name = "renameTag"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/tags/{tag_ID}/rename"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'tag_ID': Route.VALIDATOR_OBJECTID
        }

    class _addtags(Route):
        name = "add tags"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/variables/addTags"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _addmetatag(Route):
        name = "add metatag"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/variables/tags"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _deletetag(Route):
        name = "delete tag"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/tags/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _edittag(Route):
        name = "edit tag"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/variables/tag"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _editmetatag(Route):
        name = "edit metatag"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/metatype/tag"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _createmetatag(Route):
        name = "create metatag"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/metatype/addTag"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }
