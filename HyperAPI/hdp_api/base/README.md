# HyperAPI.hdp_api.routes.base

This module contains base implementations for Resources, Routes and version management.
- [Resource Abstract Class](#resource_class)
- [Route Abstract Class](#route_class)
- [SubRoute Abstract Class](#subroute_class)
- [Resource and Routes definition example](#example)

<a name="resource_class"></a>

## Resource Abstract Class

Defines a resource which is a Route container as defined in the `hypercubeApi.json` file on HDP. 
Resources are instanciated when the `HyperAPI.hdp_api.base.Router` is instanciated and a session is opened. 

When a resource is created, all `HyperAPI.hdp_api.base.Route` classes defined within a resource are also instanciated if their hdp_version requirements are met. 

Resources are iterables, yielding every routes they contains. 

### Attributes and properties

#### name (abstract property, must be defined in all subclasses)
The name of the resource as stated in the `hypercubeApi.json` file on HDP. The name must be an exact match. 

_Expected Format_: str

#### available_since
The HDP version on which the resource was created. The resource will only be created and available if the API connects to a HDP server of that version (included) and above. 

_Expected Format_: str (must be a suitable hdp version string)
_Default Value_: 0 (will be converted to `Version(0.0.0)`)

#### removed_since
The HDP version on which the resource was deleted. The resource not be available if the API connects to a HDP server of that version (included) onwards. 

_Expected Format_: str (must be a suitable hdp version string)
_Default Value_: None (will be converted to `Version(None)`)

#### unavailable_on
Specific HDP versions on which the resource is not available. This setting takes precedence over `available_since` setting.

_Expected Format_: str[] (must be a list of suitable hdp version string)
_Default Value_: []

### Public Methods

#### is_available(version)
Classmethod. Returns true if the resource is available for the specified version, false otherwise. `version` must be a valid hdp version string or a `HyperAPI.utils.version.Version` instance.

#### check_routes_integrity()
Classmethod. Checks the integrity of all routes defined in the ressource. 

<a name="route_class"></a>

## Route Abstract Class

<a name="subroute_class"></a>

## SubRoute Abstract Class

<a name="example"></a>

## Resource and Routes definition example