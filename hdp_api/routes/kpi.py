from HyperAPI.hdp_api.routes import Resource, Route


class Kpi(Resource):
    name = "Kpi"

    class _getKpiCorrelation(Route):
        name = "getKpi Correlation"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/kpis"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _kpisFamily(Route):
        name = "kpisFamily"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/kpis/family/{familyKpi_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'familyKpi_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getKpisForRuleBuilder(Route):
        name = "getKpisForRuleBuilder"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/kpis/rb"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _addKpi(Route):
        name = "add Kpi"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/kpis"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _deleteKpi(Route):
        name = "deleteKpi"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/kpis/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _updateKpi(Route):
        name = "updateKpi"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/kpis/update"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getScoreByKpis(Route):
        name = "getScoreByKpis"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/kpis/scores"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getKpisVariable(Route):
        name = "getKpisVariable"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/kpis/variables"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }
