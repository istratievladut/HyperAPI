from HyperAPI.utils.version import Version


# Route version management --------------------------------------------------------------------------
def deprecated_since(version: str):
    def cls_decorator(cls):
        cls.deprecated_since = Version(version)
        return cls
    return cls_decorator


def reroute(version: str, reroute_to, convert_to: callable):
    def cls_decorator(cls):
        cls.add_redirection(Version(version), reroute_to, convert_to)
        return cls
    return cls_decorator


def available_since(version: str):
    def cls_decorator(cls):
        cls.available_since = Version(version)
        return cls
    return cls_decorator
