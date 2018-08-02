from HyperAPI.hdp_api.routes import Resource, Route


class Rules(Resource):
    name = "Rules"

    class _ruleAsDataset(Route):
        name = "ruleAsDataset"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/ruleAsDataset"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _Addtagstorules(Route):
        name = "Add tags to rules"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/tags/addRulesTags"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _AddrulefromRuleBuilder(Route):
        name = "Add rule from Rule Builder"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/rules/addRule"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _GetRuleTagsByDatasetId(Route):
        name = "Get Rule Tags by DatasetId"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/tags/getRulesTags"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _GetRulesTagByTagId(Route):
        name = "Get Rule Tag By TagId"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/tags/{tag_ID}/getRulesTag"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'tag_ID': Route.VALIDATOR_OBJECTID
        }

    class _GetRulesTag(Route):
        name = "Get Rule Tag"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/tags/getRulesTags"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _Getlearnings(Route):
        name = "Get learnings"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/learnings"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _GetRulebyruleId(Route):
        name = "Get Rule by ruleId"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/rules/{rule_ID}/getRule"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'rule_ID': Route.VALIDATOR_OBJECTID
        }

    class _GetRules(Route):
        name = "Get Rules"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/rules/getrules"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _tagallRules(Route):
        name = "tagallRules"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/tags/addAllRulesTags"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _GetthenumberofRules(Route):
        name = "Get the number of Rules"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/rules/countrules"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _newMinimizeName(Route):
        name = "newMinimizeName"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/tags/newMinimizeName"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _newLearningName(Route):
        name = "newLearningName "
        httpMethod = Route.GET
        path = "/projects/{project_ID}/tags/newLearningName"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _Removetagsofrules(Route):
        name = "Remove tags of rules"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/tags/removeRulesTags"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _Removealearning(Route):
        name = "Remove a learning"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/learning/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _ApplyaRule(Route):
        name = "Apply a Rule"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/rules/applyRule"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _Updatetagsofrules(Route):
        name = "Update tags of rules"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/tags/updateRulesTags"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }
