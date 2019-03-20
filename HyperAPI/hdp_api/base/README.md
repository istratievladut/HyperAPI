# HyperAPI.hdp_api.routes.base

This module contains base implementations for Resources, Routes and version management.
- [Resource Abstract Class](#resource_class)
- [Route Abstract Class](#route_class)

<a name="resource_class"></a>

## Resource Abstract Class

Defines a resource which is a Route container as defined in the `hypercubeApi.json` file on HDP. 
Resources are instanciated when the `HyperAPI.hdp_api.Router` is instanciated and a session is opened. 

When a resource is created, all `HyperAPI.hdp_api.routes.Route` classes defined within a resource are also instanciated if their hdp_version requirements are met. 

Resources are iterables, yielding every routes they contains. 

### Properties to define

#### Available Since
The HDP version on which the resource was created. The resource will only be created and available if the API connects to a HDP server of that version (included) and above. 

_Expected Format_: str


#### Removed Since
The HDP version on which the resource was deleted. The resource not be available if the API connects to a HDP server of that version (included) onwards. 

_Expected Format_: str


#### Name
The name of the resource as stated in the `hypercubeApi.json` file on HDP. The name must be an exact match. 

_Expected Format_: str


<a name="route_class"></a>

## Route Abstract Class