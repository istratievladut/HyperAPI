from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route, SubRoute


class Nitro(Resource):
    name = "nitro"
    available_since = "1.0"
    removed_since = None

    class _getForecasts(Route):
        name = "getForecasts"
        httpMethod = Route.GET
        removed_since = "3.0"
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

        class _getForecastsPost(SubRoute):
            name = "getForecasts"
            httpMethod = Route.POST
            available_since = "3.0"
            path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts"
            _path_keys = {
                'project_ID': Route.VALIDATOR_OBJECTID,
                'dataset_ID': Route.VALIDATOR_OBJECTID
            }

    class _postForecasts(Route):
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
        available_since = "3.0"
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

    class _updateForecastCoef(Route):
        name = "updateForecastCoef"
        available_since = '2.0'
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
        httpMethod = Route.GET
        available_since = "1.0"
        removed_since = "3.0"
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

        class _postForecastTunes(SubRoute):
            name = "getForecastTunes"
            httpMethod = Route.POST
            available_since = "3.0"
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

    class _getForecastTunesAggregate(Route):
        name = "getForecastTunesAggregateGeo"
        httpMethod = Route.GET
        available_since = "1.0"
        removed_since = "3.0"
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/aggregate"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    class _getForecastTunesAggregateGeo(Route):
        name = "getForecastTunesAggregateGeo"
        httpMethod = Route.POST
        available_since = "3.0"
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/aggregate/geo"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    class _getForecastTunesAggregateDepot(Route):
        name = "getForecastTunesAggregateDepot"
        httpMethod = Route.POST
        available_since = "3.0"
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/aggregate/depot"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    class _exportForecastTunes(Route):
        name = "exportForecastTunes"
        httpMethod = Route.GET
        available_since = "3.0"
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/export"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    class _exportReport(Route):
        name = "exportReport"
        available_since = '2.0'
        httpMethod = Route.GET
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/exportreport"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    class _getForecastTunesStats(Route):
        name = "getForecastTunesStats"
        available_since = '3.0.2'
        httpMethod = Route.POST
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/stats"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    class _getForecastTunesMetadata(Route):
        name = "getForecastTunesMetadata"
        available_since = '4.2.2'
        removed_since = '4.2.3'
        httpMethod = Route.GET
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/metadata"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }

    class _getForecastMetadata(Route):
        name = "getForecastMetadata"
        available_since = '4.2.3'
        removed_since = '4.2.8'
        httpMethod = Route.GET
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/metadata"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID
        }

    class _getForecastIdMetadata(Route):
        name = "getForecastIdMetadata"
        available_since = '4.2.8'
        httpMethod = Route.GET
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/metadata"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }        

    class _getForecastTunesModalities(Route):
        name = "getForecastTunesModalities"
        available_since = '4.2.2'
        httpMethod = Route.POST
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/modalities"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }
