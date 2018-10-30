from HyperAPI.utils.exceptions import ApiException
import importlib
import logging


def get_required_module(module_name):
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError:
        warn_msg = 'The module {md} is missing and required for this function.\n'
        warn_msg = warn_msg + 'To install it on a notebook, execute "!pip install {md}" and restart the kernel'
        logging.warning(warn_msg.format(md=module_name))
        raise ApiException(f'Missing module for this function : {module_name}')
