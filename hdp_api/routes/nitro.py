from HyperAPI.hdp_api.routes import Resource, Route


class Nitro(Resource):
    name = "nitro"

    class _getForecasts(Route):
        name = "getForecasts"
        httpMethod = Route.GET
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
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts"
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

    class _getForecastAggregateTunes(Route):
        name = "getForecastAggregateTunes"
        httpMethod = Route.GET
        path = "/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/aggregate"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'dataset_ID': Route.VALIDATOR_OBJECTID,
            'forecast_ID': Route.VALIDATOR_OBJECTID
        }
