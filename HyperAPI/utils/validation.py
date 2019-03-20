def compare_schema_resources(available_resources, schema_resources, version):
    _available = set(_r.name for _r in available_resources if _r.is_available(version))
    _schema = set(schema_resources)

    unexpected = list(_available.difference(_schema))
    missing = list(_schema.difference(_available))
    match = list(_available.intersection(_schema))

    return unexpected, missing, match


def compare_schema_routes(available_routes, schema_routes, version):
    _available = set()

    for _r in available_routes:
        if _r.is_available(version, compatiblity_mode=False): 
            _available.add('{}:{}'.format(_r.httpMethod, _r.path))
        else:
            for _sr in _r.get_subroutes():
                if _sr.is_available(version):
                    _available.add('{}:{}'.format(_sr.httpMethod, _sr.path))

    _schema = set('{}:{}'.format(_r.get('httpMethod', None), _r.get('path', None)) for _r in schema_routes.values())

    unexpected = list(_available.difference(_schema))
    missing = list(_schema.difference(_available))
    match = list(_available.intersection(_schema))

    return unexpected, missing, match
