# HyperAPI Changelog

## 5.1

### 5.1.8 - HyperAPI is now HDP version 1.0 & 1.1 compliant

- Adding Route `Identities.getAllUserInfos`
    - Deprecated since HDP 2.0
    - GET `/identities/users/info`

- Adding Route `Projects.getShareusers`
    - Deprecated since HDP 2.0
    - GET `/projects/{project_ID}/getShareUsers`

- Edited Route `Visualization.CreateMany`
    - Available since HDP 2.0
    - POST `/projects/{project_ID}/datasets/{dataset_ID}/visualizations/createMany`

- Edited Route `Prediction.publishModel`
    - Available since HDP 2.0
    - POST `/projects/{project_ID}/models/{model_ID}/publish`

- Edited Route `Datasets.ExportdiscreteDict`
    - Available since HDP 3.2
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/discreteDict/export`

- Edited Route `Correlations.GetCorrelations`
    - Available since HDP 3.0
    - GET `/projects/{project_ID}/correlations`

- Edited Route `Correlations.CreateCorrelation`
    - Available since HDP 3.0
    - POST `/projects/{project_ID}/datasets/{dataset_ID}/correlations`

- Edited Route `Correlations.UpdateCorrelationName`
    - Available since HDP 3.0
    - POST `/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/rename`

- Edited Route `Correlations.GetCorrelation`
    - Available since HDP 3.0
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}`

- Edited Route `Correlations.GetCorrelationCsv`
    - Available since HDP 3.0
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/export`

- Edited Route `Correlations.UpdateCorrelationPreview`
    - Available since HDP 3.0
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/preview`

- Adding Route `Correlations.NewCorrelation`
    - Deprecated since HDP 3.0
    - POST `/projects/{project_ID}/tasks/new`

- Adding Route `Correlations.GetNewJSONfile`
    - Deprecated since HDP 3.0
    - POST `/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}`

- Adding Route `Correlations.GetJSONfile`
    - Deprecated since HDP 3.0
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/correlation/{correlation_ID}`

- Adding Route `Correlations.GetNewCSVfile`
    - Deprecated since HDP 3.0
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/export`

- Adding Route `Correlations.GetCSVfile`
    - Deprecated since HDP 3.0
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/export`

- Adding Route `Correlations.InitListOfCorrelations`
    - Deprecated since HDP 3.0
    - GET `/projects/{project_ID}/correlations`

- Adding Route `Correlations.CreateNewCorrelation`
    - Deprecated since HDP 3.0
    - POST `/projects/{project_ID}/datasets/{dataset_ID}/correlations`

- Adding Route `Correlations.RenameNewCorrelation`
    - Deprecated since HDP 3.0
    - POST `/projects/{project_ID}/datasets/{dataset_ID}/correlations/{correlation_ID}/rename`

- Adding Route `Correlations.retrieveCorrelationsPreview`
    - Deprecated since HDP 3.0
    - GET `/projects/{project_ID}/correlations/previews`

- Edited Route `Nitro.getForecasts`
    - Available since HDP 3.0
    - POST `/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts`

- Adding Route `Nitro.getForecasts`
    - Available since HDP 2.0
    - GET `/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts`

- Edited Route `Nitro.insertForecast`
    - Available since HDP 3.0
    - POST `/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/add`

- Adding Route `Nitro.insertForecast`
    - Deprecated since HDP 2.0
    - POST `/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts`

- Edited Route `Nitro.getForecastTunes`
    - Available since HDP 3.0
    - POST `/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes`

- Adding Route `Nitro.getForecastTunes`
    - Available since HDP 2.0
    - GET `/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes`

- Adding Route `Nitro.getForecastAggregateTunes`
    - Deprecated since HDP 2.0
    - GET `/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/aggregate`

- Edited Route `Nitro.getForecastTunesAggregateGeo`
    - Available since HDP 2.0
    - POST `/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/aggregate/geo`

- Edited Route `Nitro.getForecastTunesAggregateDepot`
    - Available since HDP 2.0
    - POST `/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/aggregate/depot`

- Edited Route `Nitro.exportForecastTunes`
    - Available since HDP 2.0
    - GET `/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/export`

### 5.1.7 - Nitro Forecast Tunes Stats

- Adding Route `nitro.getForecastTunesStats`
    - Available since HDP 3.5
    - POST `/nitro/projects/{project_ID}/datasets/{dataset_ID}/forecasts/{forecast_ID}/tunes/stats`

### 5.1.6 - Adding Lasso Model

- Adding Lasso model

### 5.1.5 - 3rd Parties Routes

- Adding Resource `ThirdParties`

- Adding Route `3rdParties.get3rdpartiessettings`
    - Available since HDP 3.4
    - GET `/3rdparties`

### 5.1.4 - Publish to ETL Routes

- Adding Route `DatasetReshapes.publishreshapetoetl`
    - Available since HDP 3.3
    - POST `/projects/{project_ID}/reshapes/{reshape_ID}/etlpublish`

- Adding Route `OptimProcess.publishcontrolcharttoetl`
    - Available since HDP 3.3
    - POST `/optimProcess/projects/{project_ID}/controlCharts/{controlChart_ID}/etlpublish`

### 5.1.3 - Estimate Dataset Size

- Adding Route `Datasets.getEstimate`
    - Available since HDP 3.2
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/estimate`

- Adding Route `Datasets.setEstimate`
    - Available since HDP 3.2
    - POST `/projects/{project_ID}/datasets/{dataset_ID}/estimate`

### 5.1.2 - SWP Matchmaking Get Variable Validation

- Adding Route `Variable.getvariablevalidation`
    - Available since HDP 3.2
    - GET `/projects/{project_ID}/datasets/{dataset_ID}/variables/validation`

- Adding Route `SWPMatchmaking.getoptimizationdetail`
    - GET `/projects/{project_ID}/redeployments/{work_ID}/optimizationDetail`


### 5.1.1 - Get Variable Validation

- Fix API Version number

### 5.1 - Import/Export AuxData Matrices

- Adding Route `AuxData.exportauxdatamatrices`
    - GET `/projects/{project_ID}/auxdata/{auxdata_ID}/exportMatrices/{work_ID}`

- Adding Route `AuxData.importauxdatamatrices`
    - POST `/projects/{project_ID}/auxdata/{auxdata_ID}/importMatrices`
