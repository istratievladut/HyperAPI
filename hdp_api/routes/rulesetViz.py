from hypercube_api.hdp_api.routes import Resource, Route


class RulesetViz(Resource):
    name = "RulesetViz"

    class _DeleteRulesetViz(Route):
        name = "Delete Ruleset Viz"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/rulesetViz/{rulesetViz_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'rulesetViz_ID': Route.VALIDATOR_OBJECTID,
        }

    class _RenameRulesetViz(Route):
        name = "Rename Ruleset Viz"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/rulesetViz/{rulesetViz_ID}/rename"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'rulesetViz_ID': Route.VALIDATOR_OBJECTID,
        }

    class _GetAllRulesetViz(Route):
        name = "Get All Ruleset Viz"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/rulesetViz"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getRulesetViz(Route):
        name = "get Ruleset Viz"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/rulesetViz/{rulesetViz_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'rulesetViz_ID': Route.VALIDATOR_OBJECTID,
        }

    class _exportRulesetViz(Route):
        name = "export Ruleset Viz"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/rulesetViz/{rulesetViz_ID}/export"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'rulesetViz_ID': Route.VALIDATOR_OBJECTID,
        }

    class _UpdateRulesetViz(Route):
        name = "Update Ruleset Viz"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/rulesetViz/{rulesetViz_ID}/update"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'rulesetViz_ID': Route.VALIDATOR_OBJECTID,
        }

    class _createSampleRulesetViz(Route):
        name = "createSampleRulesetViz"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/rulesetViz/sample"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _createRulesetViz(Route):
        name = "createRulesetViz"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/rulesetViz/create"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }
