from hypercube_api.hdp_api.routes import Resource, Route


class Prediction(Resource):
    name = "Prediction"

    class _getModel(Route):
        name = "getModel"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/models/{model_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'model_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getModels(Route):
        name = "getModels"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/models"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _createModel(Route):
        name = "createModel"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/models/create"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _zipzpark(Route):
        name = "zip zpark"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/models/{prediction_ID}/zipSpark"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'prediction_ID': Route.VALIDATOR_OBJECTID,
        }

    class _downloadspark(Route):
        name = "download spark"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/models/{prediction_ID}/downloadSpark"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'prediction_ID': Route.VALIDATOR_OBJECTID,
        }

    class _Exportscikit(Route):
        name = "Export scikit"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/models/{prediction_ID}/export"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'prediction_ID': Route.VALIDATOR_OBJECTID,
        }

    class _newModelName(Route):
        name = "newModelName"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/tags/newModelName"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getConfusionMatrix(Route):
        name = "getConfusionMatrix"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/models/{model_ID}/confusionMatrix"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'model_ID': Route.VALIDATOR_OBJECTID,
        }

    class _modelRuleSet(Route):
        name = "modelRuleSet"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/models/{model_ID}/modelRuleset"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'model_ID': Route.VALIDATOR_OBJECTID,
        }

    class _renameModel(Route):
        name = "renameModel"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/models/{model_ID}/rename"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'model_ID': Route.VALIDATOR_OBJECTID,
        }

    class _postExportScores(Route):
        name = "exportScores"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/models/{model_ID}/exportScores"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'model_ID': Route.VALIDATOR_OBJECTID,
        }

    class _publishModel(Route):
        name = "publishModel"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/models/{model_ID}/publish"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'model_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getExportScores(Route):
        name = "exportScoreCSV"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/models/{model_ID}/exportScores"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'model_ID': Route.VALIDATOR_OBJECTID,
        }

    class _exportRules(Route):
        name = "exportRules"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/models/{model_ID}/exportRules"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'model_ID': Route.VALIDATOR_OBJECTID,
        }

    class _exportRulesDataset(Route):
        name = "exportRulesDataset"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/rules/exportRules"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }
