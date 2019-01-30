from HyperAPI.hdp_api.routes import Resource, Route


class SchedulerDashboard(Resource):
    name = "scheduler-dashboard"
    available_since = "3.0"
    removed_since = None

    class _schedulerdashboard(Route):
        name = "home"
        httpMethod = Route.GET
        path = "/scheduler-dashboard"

    class _schedulerapi(Route):
        name = "scheduler-api"
        httpMethod = Route.GET
        path = "/scheduler-dashboard/api"

    class _schedulerapijobsrequeue(Route):
        name = "scheduler-api-jobs-requeue"
        httpMethod = Route.POST
        path = "/scheduler-dashboard/api/jobs/requeue"

    class _schedulerapijobsdelete(Route):
        name = "scheduler-api-jobs-delete"
        httpMethod = Route.POST
        path = "/scheduler-dashboard/api/jobs/delete"

    class _schedulerapijobscreate(Route):
        name = "scheduler-api-jobs-create"
        httpMethod = Route.POST
        path = "/scheduler-dashboard/api/jobs/create"
