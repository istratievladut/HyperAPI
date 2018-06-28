import json
import os
import re
from os.path import join as j
from os.path import exists
from requests import request


def get_current_cluster_name():
    return request(url='http://gateway:51678/v1/metadata', method='get').json()['Cluster']


def is_reserved(key):
    return re.match(r'^_.*$', key)


def is_optionnal(schema):
    if not isinstance(schema, dict):
        return False
    if "_optional" in schema.keys():
        return schema["_optional"]
    return False


def is_alternative(schema):
    if "_type" in schema.keys():
        return schema["_type"] == 'alternative'
    return False


def is_any(schema):
    if isinstance(schema, dict) and "_type" in schema.keys():
        return schema["_type"] == 'any'
    return False


def get_real_keys(schema):
    keys = []
    for key in schema.keys():
        if not is_reserved(key):
            keys.append(key)
    return keys


def contains_key(schema, key):
    return key in get_real_keys(schema)


def is_valid_type_any(schema, key):
    if is_any(schema[key]):
        for sub_key in schema[key].keys():
            if sub_key not in ["_optional", "_type"]:
                raise Exception('Invalid config - %s is a type any but contains other keys (not optionnal)' % key)
        return True
    return False


def is_valid_alternative(conf, schema, key):
    if is_alternative(schema[key]):
        type = conf[key]['type']
        if not contains_key(schema[key], type):
            raise Exception('Invalid config - %s is not a valid %s option !' % (type, key))
        return True
    return False


def get_dynamic_type(key):
    if re.match(r'^dev[-]env:.*$', key):
        return 'dev-env'
    if re.match(r'^env:.*$', key):
        return 'env'
    if re.match(r'^ecs[-]s3:.*$', key):
        return 'ecs-s3'
    return False


def get_env(s):
    env_var = os.environ.get(s.replace('env:', ''))
    try:
        var_to_return = json.loads(env_var)
    except Exception:
        var_to_return = env_var
    return var_to_return


def get_dev_env(s):
    env_var = os.environ.get(s.replace('dev-env:', ''))
    try:
        env_var = env_var.replace('\'', '\"')
        var_to_return = json.loads(env_var)
    except Exception:
        var_to_return = env_var
    return var_to_return


def get_ecs_s3(string):
    [method, file] = string.split(':')
    assert method == 'ecs-s3'
    assert len(file) > 0

    import boto3
    s3 = boto3.client('s3')

    cluster = get_current_cluster_name()
    assert len(cluster) > 0
    key = '/'.join([cluster, file])

    response = s3.get_object(Bucket='hc-cluster-configs', Key=key)
    content = response["Body"].read().decode()
    assert len(content) > 0
    return json.loads(content)


def validate_partial(conf, schema):
    for key in conf.keys():
        if is_reserved(key):
            raise Exception('Invalid config - %s is a reserved value - should be use only in schema' % key)

        if key not in schema.keys():
            raise Exception('Invalid config - %s is in the conf but not in schema !' % key)

        if conf[key] is None and not is_optionnal(schema[key]):
            raise Exception('Invalid config - %s is None but not optionnal !' % key)

    for key in schema.keys():
        if key not in conf.keys() and not is_reserved(key) and not is_optionnal(schema[key]):
            raise Exception('Invalid config - %s is in the schema but not in conf !' % key)

    for key in conf.keys():
        if isinstance(conf[key], str):
            dynamic_type = get_dynamic_type(conf[key])
            if dynamic_type:
                if dynamic_type == 'dev-env':
                    conf[key] = validate_partial({key: get_dev_env(conf[key])}, {key: schema[key]})[key]
                elif dynamic_type == 'env':
                    conf[key] = validate_partial({key: get_env(conf[key])}, {key: schema[key]})[key]
                elif dynamic_type == 'ecs-s3':
                    conf[key] = validate_partial({key: get_ecs_s3(conf[key])}, {key: schema[key]})[key]
                else:
                    raise Exception('Invalid config - ${dynamicType} is not implemented yet.' % dynamic_type)

        if not type(conf[key]) == type(schema[key]):  # NOQA
            if (isinstance(conf[key], dict) or isinstance(schema[key], dict)) \
                    and not is_any(schema[key]) and not (is_optionnal(schema[key]) and conf[key] is None):
                raise Exception('Invalid config - %s is a %s in the conf but an %s in the schema.' % (key, type(conf[key]), type(schema[key])))

        if isinstance(conf[key], dict):
            if is_valid_alternative(conf, schema, key):
                sub_schema = schema[key][conf[key]["type"]]
                if isinstance(sub_schema, dict):
                    sub_schema["type"] = conf[key]["type"]
                else:
                    sub_schema = {"type": conf[key]["type"]}
                conf[key] = validate_partial(conf[key], sub_schema)

            elif not is_valid_type_any(schema, key):
                conf[key] = validate_partial(conf[key], schema[key])
    return conf


def validate(config, schema):
    return validate_partial(config, schema)


_config = None


def get_config():
    global _config
    if _config is None:
        config_path = os.environ.get('HYPERCUBE_CONFIG')

        if config_path is None:
            return None

        if not exists(config_path):
            print("Could not find Config file at %s" % config_path)
            raise FileNotFoundError

        _config = read_config(config_path)
    return _config


def read_config(config_path):
    with open(config_path) as build_config_file:
        build_config = json.load(build_config_file)

    with open(build_config["confFile"]) as platform_config_file:
        platform_config = json.load(platform_config_file)

    # TODO: replace configFolder by shared folder
    with open(j(build_config["dependencies"]["configFolder"], 'products.json')) as product_definition_file:
        product_definition = json.load(product_definition_file)

    # TODO: Resolve (= check) the conf with schema
    with open(j(build_config["dependencies"]["configFolder"], 'config_schema.json')) as schema_file:
        schema = json.load(schema_file)

    platform_config = validate(platform_config, schema)

    config = build_config
    for key in platform_config.keys():
        config[key] = platform_config[key]

    config["features"] = product_definition[config["defaultProduct"]]

    return config
