from HyperAPI.hdp_api.routes import Resource, Route
from HyperAPI.hdp_api.routes.base.version_management import available_since


class Nitro(Resource):
    name = "nitro"

    class _getForecasts(Route):
        name = "getForecasts"
        httpMethod = Route.POST
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _getForecast(Route):
        name = "getForecast"
        httpMethod = Route.GET
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    class _insertForecast(Route):
        name = "insertForecast"
        httpMethod = Route.POST
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/add"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _updateForecast(Route):
        name = "updateForecast"
        httpMethod = Route.POST
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    @available_since('2.0')
    class _updateForecastCoef(Route):
        name = "updateForecastCoef"
        httpMethod = Route.POST
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/updatecoef"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    class _deleteForecast(Route):
        name = "deleteForecast"
        httpMethod = Route.POST
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    class _getForecastTunes(Route):
        name = "getForecastTunes"
        httpMethod = Route.POST
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    class _updateForecastTunes(Route):
        name = "updateForecastTunes"
        httpMethod = Route.POST
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/update"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    class _getForecastTunesAggregateGeo(Route):
        name = "getForecastTunesAggregateGeo"
        httpMethod = Route.POST
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/aggregate/geo"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    class _getForecastTunesAggregateDepot(Route):
        name = "getForecastTunesAggregateDepot"
        httpMethod = Route.POST
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/aggregate/depot"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    class _exportForecastTunes(Route):
        name = "exportForecastTunes"
        httpMethod = Route.GET
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/export"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    @available_since('2.0')
    class _exportReport(Route):
        name = "exportReport"
        httpMethod = Route.GET
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/exportreport"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }
