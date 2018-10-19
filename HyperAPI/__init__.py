try:
    from HyperAPI.package_metadata import __version__
except ImportError:
    __version__ = 0
    
from HyperAPI.hyper_api.api import Api
from HyperAPI.hdp_api import Router

