from hypercube_api.hdp_api.routes import Resource, Route


class TextProcessing(Resource):
    name = "Text Processing"

    class _ExtractWordset(Route):
        name = "Extract Wordset"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/nlp/extract"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _CreateWordset(Route):
        name = "Create Wordset"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/nlp/wordset/create"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _EnrichDatasetFromWordset(Route):
        name = "Enrich Dataset From Wordset"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/nlp/enrich"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _ListWordsets(Route):
        name = "List Wordsets"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/nlp/wordsets"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getWordset(Route):
        name = "get Wordset"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/nlp/wordset/{wordset_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'wordset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _DeleteWordset(Route):
        name = "Delete Wordset"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/nlp/wordset/{wordset_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'wordset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _updateWordset(Route):
        name = "update Wordset"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/nlp/wordset/{dataset_ID}/update"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _CreateWordsetVisiaulization(Route):
        name = "Create Wordset Visiaulization"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/wordsetsViz/create"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _deleteWordsetVisualization(Route):
        name = "delete Wordset Visualization"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/wordsetsViz/{wordsetViz_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'wordsetViz_ID': Route.VALIDATOR_OBJECTID,
        }

    class _GetwordsetsVisualization(Route):
        name = "Get wordsets Visualization"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/wordsetsViz"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _Getwordsetvisualization(Route):
        name = "Get wordset visualization"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/wordsetsViz/{wordsetViz_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'wordsetViz_ID': Route.VALIDATOR_OBJECTID,
        }

    class _updateWordsetVisualization(Route):
        name = "update Wordset Visualization"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/wordsetsViz/{wordsetViz_ID}/update"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'wordsetViz_ID': Route.VALIDATOR_OBJECTID,
        }
