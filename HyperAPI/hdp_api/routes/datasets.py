from HyperAPI.hdp_api.routes import Resource, Route
from HyperAPI.hdp_api.routes.base.version_management import available_since


class Datasets(Resource):
    name = "Datasets"

    class _Datasets(Route):
        name = "Datasets"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _createMongoDataset(Route):
        name = "addDatasets"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/addDatasetFromMongo"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _createConstrainedDataset(Route):
        name = "addConstrainedDataset"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/addConstrainedDataset"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _createFolderDiffDataset(Route):
        name = "addFolderDiffDataset"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/addFolderDiffDataset"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _saveAsNewDataset(Route):
        name = "saveAsNewDataset"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/saveAsNewDataset"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getXvalues(Route):
        name = "getXvalues"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/xvalues/{columns_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'columns_ID': Route.VALIDATOR_OBJECTID,
        }

    class _UploadDatasets(Route):
        name = "UploadDatasets"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/add"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _Getadataset(Route):
        name = "Get a dataset"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _filteredGrid(Route):
        name = "filtered Grid"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/filteredGrid"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getDatasetTempData(Route):
        name = "getDatasetTempData"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/tempData"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _Stats(Route):
        name = "Stats"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/stats"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getVariablesStats(Route):
        name = "getVariablesStats"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/stats/variables"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getModalites(Route):
        name = "getModalites"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/stats/modalities"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _Defaultdataset(Route):
        name = "Default dataset"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/updateSelected"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _refreshCache(Route):
        name = "refreshCache"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/refreshCache"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _Deletedataset(Route):
        name = "Delete dataset"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _ExportCSV(Route):
        name = "ExportCSV"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/exportCSV"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _Exportmetadata(Route):
        name = "Export metadata"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/metadata/export"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _ExportdiscreteDict(Route):
        name = "Export discreteDict"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/discreteDict/export"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _getSample(Route):
        name = "getSample"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/sample"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _metadata(Route):
        name = "metadata"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/metadata"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _Importmetadata(Route):
        name = "Import metadata"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/metadata/import"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _dataValidationLog(Route):
        name = "dataValidationLog"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/dataValidationLog"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _readMetadata(Route):
        name = "readMetadata"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/readMetadata"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _readDiscreteDict(Route):
        name = "readDiscreteDict"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/readDiscreteDict"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _split(Route):
        name = "split"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/split"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _sample(Route):
        name = "sample"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/sample"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _discretize(Route):
        name = "discretize"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/discretize"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _deleteDiscretization(Route):
        name = "deleteDiscretization"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/deleteDiscretization"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    class _createDataset(Route):
        name = "createDataset"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/create"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    @available_since('3.2')
    class _getEstimate(Route):
        name = "getEstimate"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/datasets/{dataset_ID}/estimate"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }

    @available_since('3.2')
    class _setEstimate(Route):
        name = "setEstimate"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/{dataset_ID}/estimate"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
        }
