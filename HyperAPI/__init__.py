try:
    from HyperAPI.package_metadata import __version__
except ImportError:
    __version__ = 0

from HyperAPI.hyper_api.api import Api  # noqa: F401
from HyperAPI.hdp_api import Router  # noqa: F401
