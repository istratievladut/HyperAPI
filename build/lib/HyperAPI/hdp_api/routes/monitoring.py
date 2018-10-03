from HyperAPI.hdp_api.routes import Resource, Route


class Monitoring(Resource):
    name = "monitoring"

    class _listWorksOfAProject(Route):
        name = "listWorksOfAProject"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/works"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _killWork(Route):
        name = "killWork"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/works/{work_ID}/stop"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'work_ID': Route.VALIDATOR_OBJECTID
        }

    class _worksDetails(Route):
        name = "worksDetails"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/works/{work_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'work_ID': Route.VALIDATOR_OBJECTID
        }

    class _hyperWorkersList(Route):
        name = "hyperWorkersList"
        httpMethod = Route.GET
        path = "/monitoring/hyperWorkerList"

    class _processList(Route):
        name = "processList"
        httpMethod = Route.GET
        path = "/monitoring/processList"

    class _lastActiveUsers(Route):
        name = "lastActiveUsers"
        httpMethod = Route.GET
        path = "/monitoring/lastActiveUsers"

    class _instanceList(Route):
        name = "instanceList"
        httpMethod = Route.GET
        path = "/monitoring/instances"

    class _instanceSpawn(Route):
        name = "instanceSpawn"
        httpMethod = Route.POST
        path = "/monitoring/instances/spawn"

    class _killWorker(Route):
        name = "killWorker"
        httpMethod = Route.POST
        path = "/monitoring/workers/{worker_ID}/kill"
        _path_keys = {
            'worker_ID': Route.VALIDATOR_OBJECTID
        }

    class _metrics(Route):
        name = "metrics"
        httpMethod = Route.GET
        path = "/monitoring/metrics"
