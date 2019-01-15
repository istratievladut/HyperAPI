from HyperAPI.hdp_api.routes import Resource, Route
from HyperAPI.hdp_api.routes.base.version_management import available_since, deprecated_since

class Correlations(Resource):
    name = "Correlations"

    @available_since('3.0')
    class _GetCorrelations(Route):
        name = "GetCorrelations"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/correlations"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    @available_since('3.0')
    class _CreateCorrelation(Route):
        name = "CreateCorrelation"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    @available_since('3.0')
    class _UpdateCorrelationName(Route):
        name = "UpdateCorrelationName"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/rename"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    @available_since('3.0')
    class _GetCorrelation(Route):
        name = "GetCorrelation"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    @available_since('3.0')
    class _GetCorrelationCsv(Route):
        name = "GetCorrelationCsv"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/export"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    class _DeleteCorrelation(Route):
        name = "DeleteCorrelation"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    @available_since('3.0')
    class _UpdateCorrelationPreview(Route):
        name = "UpdateCorrelationPreview"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/preview"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    @deprecated_since('3.0')
    class _NewCorrelation(Route):
        name = "New Correlation"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/tasks/new"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }
    
    @deprecated_since('3.0')
    class _GetNewJSONfile(Route):
        name = "Get new JSON file"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    @deprecated_since('3.0')
    class _GetJSONfile(Route):
        name = "Get JSON file"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlation/{correlation_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }


    @deprecated_since('3.0')
    class _GetNewCSVfile(Route):
        name = "Get new CSV file"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/export"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }
    
    @deprecated_since('3.0')
    class _GetCSVfile(Route):
        name = "Get CSV file"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/export"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    @deprecated_since('3.0')
    class _InitListOfCorrelations(Route):
        name = "Init List of correlations"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/correlations"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    @deprecated_since('3.0')
    class _CreateNewCorrelation(Route):
        name = "CreateNewCorrelation"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }
    
    @deprecated_since('3.0')
    class _RenameNewCorrelation(Route):
        name = "RenamNewCorrelation"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/rename"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }

    @deprecated_since('3.0')
    class _saveCorrelationImg(Route):
        name = "saveCorrelationImg"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/preview"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'correlation_ID': Route.VALIDATOR_OBJECTID,
        }
    
    @deprecated_since('3.0')
    class _retrieveCorrelationsPreview(Route):
        name = "retrieveCorrelationsPreview"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/correlations/previews"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }
