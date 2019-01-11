# HyperAPI Changelog

## 5.1

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
