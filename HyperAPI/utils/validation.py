def compare_schema_resources(available_resources, schema_resources):
    _available = set(_r.name for _r in available_resources)
    _schema = set(schema_resources)

    unexpected = _available.difference(_schema)
    missing = _schema.difference(_available)
    match = _available.intersection(_schema)

    return unexpected, missing, match


def compare_schema_routes(available_routes, schema_routes):
    _available = set('{}:{}'.format(_r.httpMethod, _r.path) for _r in available_routes)
    _schema = set('{}:{}'.format(_r.get('httpMethod', None), _r.get('path', None)) for _r in schema_routes.values())

    unexpected = _available.difference(_schema)
    missing = _schema.difference(_available)
    match = _available.intersection(_schema)

    return unexpected, missing, match
