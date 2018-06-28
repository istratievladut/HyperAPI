from hypercube_api.util import Helper
from hypercube_api.hyper_api.base import Base


class XRayVariableFactory:
    """
    """
    def __init__(self, api, xray):
        self.__api = api
        self.__xray = xray

    @Helper.try_catch
    def filter(self):
        """
            Returns:
                XRayVariable[]: list of variables in the current Xray
        """
        json = {'project_ID': self.__xray.project_id, 'dataset_ID': self.__xray.dataset_id, 'simpleLift_ID': self.__xray.id}
        return [XRayVariable(self.__api, self.__xray, x) for x in self.__api.SimpleLift.getsimplelift(**json).get('variables')]

    @Helper.try_catch
    def get(self, name):
        """
            Returns:
                XRayVariable: Xray variable found by name
        """
        xray_variables = list(filter(lambda x: x.name == name, self.filter()))
        if xray_variables:
            return xray_variables[0]
        return None

    @Helper.try_catch
    def get_by_id(self, column_id):
        """
            Returns:
                XRayVariable: XRay variable found by column_id
        """
        xray_variables = list(filter(lambda x: x.column_id == column_id, self.filter()))
        if xray_variables:
            return xray_variables[0]
        return None

    @Helper.try_catch
    def sort(self, attribute_key='contrast_rate_value', reverse=True):
        """
            sort Xray variables (default is by decreasing constrast rate value)

            Args:
                attribute_key (str): key used to sort variables (default: 'contrast_rate_value')
                reverse (bool): order to reverse (default: True)

            Returns:
                XRayVariable[]: list of variables in the current Xray
        """
        xray_variables = self.filter()
        if len(xray_variables) == 0 or not hasattr(xray_variables[0], attribute_key) or getattr(xray_variables[0], attribute_key) is None:
            return xray_variables
        return sorted(xray_variables, key=lambda x: getattr(x, attribute_key), reverse=reverse)


class XRayVariable(Base):
    """
    """
    def __init__(self, api, xray, json_return):
        self.__api = api
        self.__xray = xray
        self.__details = None
        self.__json_returned = json_return

    def __repr__(self):
        return "\n{} : {}\n".format(
            self.__class__.__name__,
            self.name
        ) + ("\t<! This variable has been ignored>\n" if self.is_ignored else "") + \
            """\t- Discrete : {}\n""".format(
            self.is_discrete
        ) + ("""\t- Contrast rate : {:.2f}%\n""".format(self.contrast_rate_value * 100) if self.contrast_rate_value else "")

    @property
    def _json(self):
        return self.__json_returned

    @property
    def name(self):
        return self.__json_returned.get('name')

    @property
    def is_discrete(self):
        return self.__json_returned.get('type') == 'D'

    @property
    def is_ignored(self):
        return self.__json_returned.get('ignored')

    @property
    def column_id(self):
        return self.__json_returned.get('column')

    @property
    def contrast_rate_value(self):
        contrastRates = self.__json_returned.get('contrastRates')
        if len(contrastRates.values()) > 0:
            return list(contrastRates.values())[0]
        return None

    @property
    def contrast_rates(self):
        contrastRates = self.__json_returned.get('contrastRates')
        return contrastRates

    @property
    def coverage(self):
        self.__get_details()
        return self.__details.get('coverage')

    @property
    def xValues(self):
        self.__get_details()
        return self.__details.get('xValues')

    @property
    def yValues(self):
        self.__get_details()
        return self.__details.get('yValues')

    @property
    def size(self):
        self.__get_details()
        return self.__details.get('size')

    @property
    def value_range(self):
        self.__get_details()
        return self.__details.get('value_range')

    @property
    def outputs(self):
        self.__get_details()
        return self.__details.get('outputs')

    @Helper.try_catch
    def __get_details(self):
        if self.__details is None:
            json = {'project_ID': self.__xray.project_id, 'dataset_ID': self.__xray.dataset_id, 'task_ID': self.__xray.id, 'column_ID': self.column_id}
            self.__details = self.__api.SimpleLift.getvariablejsonfile(**json)
        return self.__details
