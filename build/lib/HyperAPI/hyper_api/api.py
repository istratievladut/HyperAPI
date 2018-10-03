from HyperAPI.hdp_api._router import Router
from HyperAPI.util import Helper
from HyperAPI.hyper_api.project import ProjectFactory


class Api:
    @Helper.try_catch
    def __init__(self, token=None, url='', username=None, password=None, watcher=None):
        self.__api = Router(token=token, url=url, watcher=watcher, username=username, password=password)
        system_details = self.__api.System.about()
        print('{}\n{} - {}\nVersion: {}\nBuild date: {}'.format(self.__api.session.url,
                                                                system_details.get('name'),
                                                                system_details.get('product'),
                                                                system_details.get('version'),
                                                                system_details.get('buildDate')
                                                                ))
        self.Project = ProjectFactory(self.__api)

        self.timeout_settings = self.__api._default_timeout_settings
