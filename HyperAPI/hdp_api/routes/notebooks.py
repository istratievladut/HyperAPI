from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class Notebooks(Resource):
    name = "notebooks"
    available_since = "1.0"
    removed_since = None

    class _getNotebooks(Route):
        name = "getNotebooks"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/notebooks"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _startNotebookServer(Route):
        name = "startNotebookServer"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/notebookServer/start"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _createNotebook(Route):
        name = "createNotebook"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/notebooks/{notebook_name}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'notebook_name': Route.VALIDATOR_ANY,
        }

    class _stopNotebookServer(Route):
        name = "stopNotebookServer"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/notebookServer/stop"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _shutDownNotebook(Route):
        name = "shutDownNotebook"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/notebooks/{notebook_name}/stop"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'notebook_name': Route.VALIDATOR_ANY,
        }

    class _deleteNoteBook(Route):
        name = "deleteNoteBook"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/notebooks/{notebook_name}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'notebook_name': Route.VALIDATOR_ANY,
        }

    class _renameNotebook(Route):
        name = "renameNotebook"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/notebooks/{notebook_name}/rename/{new_name}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'notebook_name': Route.VALIDATOR_ANY,
            'new_name': Route.VALIDATOR_ANY,
        }

    class _copyNotebook(Route):
        name = "copyNotebook"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/notebooks/{notebook_name}/copy"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'notebook_name': Route.VALIDATOR_ANY,
        }
