from HyperAPI.hdp_api.routes import Resource, Route


class Task(Resource):
    name = "Task"
    available_since = "3.0"
    removed_since = None

    class _task(Route):
        name = "task"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/tasks"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _createTask(Route):
        name = "create task"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/tasks/new"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _deleteTask(Route):
        name = "deleteTask"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/tasks/{task_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'task_ID': Route.VALIDATOR_OBJECTID,
        }

    class _stopService(Route):
        name = "stopService"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/tasks/stopService"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }
