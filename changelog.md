# HyperAPI Changelog

## Version 6

### 6.0

- Adding _README.md_ and _CHANGELOG.md_ files. 

- Session details (coming from the _system/about_ route) are now stored in the `hdp_api.Router` instance. Display from the `hyper_api.Api` instance has been changed accordingly. 

- Added properties `available_since` and `removed_since` on `hdp_api.routes.Resource` so no resources are created on incompatible HDP versions. 
All resources files have been updated accordingly. 

- Removed `available_since`, `deprecated_since` and `reroute` decorators for `hdp_api.routes.Route`. `available_since` is now handled as abstract properties on `hdp_api.routes.Route`.
- Added `removed_since` property on `hdp_api.routes.Route`. Routes are not created if the HDP version is equal or above that version. This behaviour replaces the `deprecated_since` decorator. 
- Routes compatiblity between HDP versions is no longer managed using the `reroute` decorator but uses the ``hdp_api.routes.Route.reroute_to` class method, which dynamically creates variants for the parent route. 
All routes have been updated accordingly.

## 5.2 - Refactoring of Projects and Datasets routes

- Deprecated route `DefaultProject`
    - Starting from HDP 3.6
    - Superseded by `updateProject`

- Deprecated route `renameProject`
    - Starting from HDP 3.6
    - Superseded by `updateProject`

## 5.1

### 5.1.11 - Fix variable ignore test

- Adding Route `DefaultResampling`
    - Available since HDP 3.6
    - POST `/projects/{project_ID}/datasets/{dataset_ID}/defaultResampling` 

- Fix variable ignore test in [variable.py](HyperAPI/hyper_api/variable.py)
```
varname = self.name
data = {'updateFields': {varname: {'ignored': True }}}
```


### 5.1.10 - Get RealTime socket configuration

- Adding Resource `Realtime`

- Adding Route `realTimeSocket.getRealTimeSettings`
    - Available since HDP 3.4
    - GET `/realTimeSocket` 


### 5.1.9 - add getModalites api

- Adding Route `getModalites`
    - Available since HDP 3.6
    - POST `/projects/{project_ID}/datasets/{dataset_ID}/modalities`


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
