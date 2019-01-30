# HyperAPI - Changelog

## Version 6

### 6.0

- Adding _README.md_ and _CHANGELOG.md_ files. 

- Session details (coming from the _system/about_ route) are now stored in the `hdp_api.Router` instance. Display from the `hyper_api.Api` instance has been changed accordingly. 

- Added properties `available_since` and `removed_since` on `hdp_api.routes.Resource` so no resources are created on incompatible HDP versions. 
All resources files have been updated accordingly. 

- Removed `available_since`, `deprecated_since` and `reroute` decorators for `hdp_api.routes.Route`. `available_since`and `deprecated_since` are now handled as abstract properties on `hdp_api.routes.Route`.
All routes have been updated accordingly.

