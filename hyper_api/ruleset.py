from hypercube_api.util import Helper
from hypercube_api.hyper_api.target import Description
from hypercube_api.hyper_api.base import Base
from hypercube_api.hyper_api.model import ModelFactory
from hypercube_api.hyper_api.rule import Rules, decode_kpiname_to_id
from hypercube_api.utils.exceptions import ApiException

import urllib.parse


class KeyIndicatorOption:
    """Creation of a key indicator"""
    def __init__(self, _target=None, _min_purity=0.1, _max_purity=1, _min_coverage=1, _max_coverage=600):
        self._target = _target
        self._min_purity = _min_purity
        self._max_purity = _max_purity
        self._min_coverage = _min_coverage
        self._max_coverage = _max_coverage


class RulesetFactory:
    _PURITY = 'Purity'
    _COVERAGE = 'Coverage'
    _LIFT = 'Lift'

    def __init__(self, api, project_id):
        self.__api = api
        self.__project_id = project_id

    @Helper.try_catch
    def create_kpi_option(self, target, min_purity=0.1, max_purity=1, min_coverage=1, max_coverage=600):
        """
        Create a key indicator
        Args:
            target (Target): Target to generate the key indicator
            min_purity (int):  Minimum score required for purity score
            max_purity (int):  Maximum score required for purity score
            min_coverage (int):  Minimum score required for coverage score
            max_coverage (int):  Maximum score required for coverage score
        Returns:
            key indicator
        """
        return KeyIndicatorOption(target, min_purity, max_purity, min_coverage, max_coverage)

    @Helper.try_catch
    def create(self, dataset, name, target, purity_min=None, coverage_min=None, rule_complexity=2, quantiles=10,
               enable_custom_discretizations=True, min_marginal_contribution=None, compute_other_key_indicators=None,
               locally_increase_complexity=False, max_complexity=3, nb_minimizations=1, coverage_increment=0.01,
               validate_stability=False, split_ratio=0.7, nb_iterations=1, purity_tolerance=0.1):
        """
        Create a new ruleset

        Args:
            dataset (Dataset): Dataset used to generate the ruleset
            name (str): Name of the new ruleset
            target (Target): Target to generate the ruleset
            purity_min (float): Minimum purity of rules, default is the entire dataset purity
            coverage_min (int): Minimum coverage of the target population for each rule, default is 10
            rule_complexity (int): Maximum number of variables in rules, default is 2
            quantiles (int): Number of intervals the continuous variables are quantized in, default is 10
            enable_custom_discretizations (boolean): use custom discretizations, eventually use "quantiles" parameter for remaining variables, default is True
            min_marginal_contribution (float): a new rule R', created by adding a new constraint to an existing rule R (and thus increasing its complexity),
                is added to the ruleset if and only if it increases the original purity of R by the minimum marginal contribution or more. Default is 0.1
            compute_other_key_indicators (list of KeyIndicatorOption): Compute other Key Indicators.
            locally_increase_complexity (bool): Enable the locally increase complexity when set as true.
            max_complexity (int): Maximum numbers of features per rule.
            nb_minimizations (int):Interate the minimization process.
            coverage_increment (float): Percentage increment of target samples that a new rule must bring to be added to the minimization ruleset.
            validate_stability (bool): Enable to split your dataset, add iteration and set a purity tolerance when set as true.
            split_ratio (float): The percentage for the split (Between 0 and 1).
            nb_iterations (int): Number of iterations wanted.
            purity_tolerance (float): Purity tolerence allowed (Between 0 and 1).

        Returns:
            Ruleset
        """
        variable = next(variable for variable in dataset.variables if variable.name == target.variable_name)
        index = variable.modalities.index(target.modality)
        datasetPurity = variable.purities[index]
        score_purity_min = purity_min or round(datasetPurity, 3)

        if min_marginal_contribution is None:
            if score_purity_min > 0.99:
                min_marginal_contribution = round(1 / score_purity_min - 1, 3)
            elif score_purity_min > 0.9:
                min_marginal_contribution = round(0.99 / score_purity_min - 1, 3)
            else:
                min_marginal_contribution = 0.1

        coverage_min = coverage_min or 10 if (variable.frequencies[index] < 1000) else 0.01

        if enable_custom_discretizations is True:
            discretizations = dataset._discretizations
        else:
            discretizations = {}

        if not compute_other_key_indicators:
            compute_other_key_indicators = []

        if not target:
            raise ApiException('You need a target to create a ruleset')
        if isinstance(target, Description):
            raise ApiException('Cannot perform a ruleset with a description kpi')

        data = {
            "projectId": self.__project_id,
            "task": {
                "type": "learning",
                "datasetId": dataset.dataset_id,
                "projectId": self.__project_id,
                "params": {
                    "learningName": name,
                    "datasetName": dataset.name,
                    "buildPredictiveModel": 0,
                    "sourceFileName": dataset.source_file_name,
                    "delimiter": dataset.separator,
                    "complexityExhaustive": rule_complexity,
                    "countQuantiles": quantiles,
                    "discretizations": discretizations,
                    "minMarginalContribution": min_marginal_contribution,
                    "target": [],
                    "kpis": []
                }
            }
        }

        for _id, _type in zip(target.score_ids, target.scores):
            _kpiData = {
                "kpiId": _id,
                "type": _type,
                "kpiFamily": target.indicator_family,
                "scoreType": _type,
                "kpiType": target.indicator_type,
                "output": target.variable_name,
                "kpiName": target.name,
                "omodality": target.modality
            }
            if _type == self._PURITY:
                _kpiData['minValue'] = score_purity_min
            elif _type == self._COVERAGE:
                _kpiData['minValue'] = coverage_min
            elif _type == self._LIFT:
                _kpiData['minValue'] = 1
            data['task']['params']['target'].append(_kpiData)

        msg = "Rules settings: \n\t- Target: {} \n\t- Min Purity: {} \n\t- Min Coverage: {} \n\t- Rule Complexity: {} \
\n\t- Default Number of Bins: {} \n\t- Enable custom discretizations: {}  \n\t- Min Marginal contribution: \
{}".format(target.name, score_purity_min, coverage_min, rule_complexity, quantiles, enable_custom_discretizations, min_marginal_contribution)

        if (len(compute_other_key_indicators) > 0):
            for key_indicator in compute_other_key_indicators:
                min_param = [key_indicator._min_purity, key_indicator._min_coverage]
                max_param = [key_indicator._max_purity, key_indicator._max_coverage]
                other_target = key_indicator._target
                score_types = ['Purity', 'Coverage']
                for _id, _type, _mini, _maxi in zip(other_target.score_ids, score_types, min_param, max_param):
                    _kpiKI = {
                        "kpiId": _id,
                        "type": _type,
                        "minValue": _mini,
                        "maxValue": _maxi,
                        "kpiFamily": other_target.indicator_family,
                        "scoreType": _type,
                        "kpiType": other_target.indicator_type,
                        "output": other_target.variable_name,
                        "kpiName": other_target.name,
                        "omodality": other_target.modality
                    }
                    data['task']['params']['target'].append(_kpiKI)
                    msg += "\n\t- Key Indicator: {} \n\t- Min {}: {} \n\t- Max {}: {} ".format(other_target.name, _type, _mini, _type, _maxi)

        if (locally_increase_complexity):
            data['task']['params']['maxComplexity'] = max_complexity
            data['task']['params']['nbMinimizations'] = nb_minimizations
            data['task']['params']['coverageIncrement'] = coverage_increment
            msg += "\n\t- Max complexity: {} \n\t- Number of Minimizations: {} \n\t- Minimization \
            Coverage Increment: {}".format(max_complexity, nb_minimizations, coverage_increment)
        if (validate_stability):
            data['task']['params']['percentageSplit'] = split_ratio
            data['task']['params']['nbModels'] = nb_iterations
            data['task']['params']['purityTolerance'] = purity_tolerance
            msg += "\n\t- Percentage split: {} \n\t- Number of Iterations: {} \n\t- Purity Tolerance: {}".format(split_ratio, nb_iterations, purity_tolerance)

        print(msg)
        _ruleset = self.__api.Task.createtask(project_ID=self.__project_id, json=data)
        self.__api.handle_work_states(self.__project_id, work_type='learning', work_id=_ruleset.get('_id'))
        return self.get(name)

    @Helper.try_catch
    def filter(self):
        """
        Get all the rulesets of the project

        Returns:
            List of ruleset
        """
        from hypercube_api.hyper_api.dataset import DatasetFactory
        factory = DatasetFactory(self.__api, self.__project_id)
        ruleset_project = self.__api.Rules.getlearnings(project_ID=self.__project_id)
        return [Ruleset(self, self.__api, factory.get_by_id(ruleset.get('datasetId')), ruleset) for ruleset in ruleset_project]

    @Helper.try_catch
    def minimize(self, ruleset, minimization_name, score_to_minimize='Purity', increment_threshold=0.01):
        """
        Perform a minimzation on a give ruleset

        Args:
            ruleset (Ruleset): Ruleset to minimize
            minimization_name (str): Name of the new ruleset
            score_to_minimize (str): Score to apply the minimization, default is purity
            increment_threshold (float): Percentage increment of target samples that a new rule must bring to be added to the minimized ruleset.

        Return:
            Ruleset
        """
        json = {
            "type": "minimization",
            "datasetId": ruleset.dataset_id,
            "projectId": ruleset.project_id,
            "params": {
                "query": "tagsfilter={}".format(urllib.parse.quote(ruleset.name)),
                "taglist": [ruleset.name],
                "kpisList": ruleset.kpis,
                "kpiId": decode_kpiname_to_id(ruleset.kpis, score_to_minimize),
                "incrementThreshold": increment_threshold,
                "tag": minimization_name
            }
        }
        _ruleset = self.__api.Task.createtask(project_ID=ruleset.project_id, json=json)
        self.__api.handle_work_states(ruleset.project_id, work_type='minimization', work_id=_ruleset.get('_id'))
        return self.get(minimization_name)

    def get(self, name):
        """
        Get a ruleset by name

        Args:
            name (str): Name of the ruleset

        Returns:
            Ruleset
        """
        try:
            return [ruleset for ruleset in self.filter() if ruleset.name == name][0]
        except IndexError:
            return []

    @Helper.try_catch
    def get_by_id(self, id):
        """
        Get the ruleset matching the given ID or None if there is no match

        Returns:
            The Ruleset or None
        """
        rulesets = [ruleset for ruleset in self.filter() if ruleset.id == id]
        if rulesets:
            return rulesets[0]
        return None

    def get_or_create(self, dataset, name, target=None, purity_min=None, coverage_min=None, rule_complexity=2, quantiles=10,
                      enable_custom_discretizations=True, min_marginal_contribution=None, compute_other_key_indicators=None,
                      locally_increase_complexity=False, max_complexity=3, nb_minimizations=1, coverage_increment=0.01,
                      validate_stability=False, split_ratio=0.7, nb_iterations=1, purity_tolerance=0.1):
        """
        Get or create a ruleset, if the ruleset exists, only the name is mandatory

        Args:
            name (str): Name of the ruleset
            target (Target): Target to generate the ruleset
            purity_min (float): Minimum purity of rules, default is the entire dataset purity
            coverage_min (int): Minimum coverage of the target population for each rule, default is 10
            rule_complexity (int): Number of features considered for generating the association rules
            quantiles (int): Number of intervals the continuous variables are quantized in
            enable_custom_discretizations (boolean): use custom discretizations, eventually use "quantiles" parameter for remaining variables, default is True
            min_marginal_contribution (float): a new rule R', created by adding a new constraint to an existing rule R (and thus increasing its complexity),
                is added to the ruleset if and only if it increases the original purity of R by the minimum marginal contribution or more. Default is 0.1
            compute_other_key_indicators (list of KeyIndicatorOption): Compute other Key Indicators.
            locally_increase_complexity (bool): Enable the locally increase complexity when set as true.
            max_complexity (int): Maximum numbers of features per rule.
            nb_minimizations (int):Interate the minimization process.
            coverage_increment (float): Percetage increment of target samples that a new rule must bring to be added to the minimization ruleset.
            validate_stability (bool): Enable to split your dataset, add iteration and set a purity tolerance when set as true.
            split_ratio (float): The percentage for the split (Between 0 and 1).
            nb_iterations (int): Number of iterations wanted.
            purity_tolerance (float): Purity tolerence allowed (Between 0 and 1).

        Returns:
            Ruleset
        """

        for ruleset in dataset.rulesets:
            if (ruleset.name == name) and (ruleset.dataset_id == dataset.dataset_id):
                return ruleset

        return self.create(dataset, name, target, purity_min, coverage_min, rule_complexity, quantiles, enable_custom_discretizations,
                           min_marginal_contribution, compute_other_key_indicators, locally_increase_complexity, max_complexity,
                           nb_minimizations, coverage_increment, validate_stability, split_ratio, nb_iterations, purity_tolerance)


class Ruleset(Base):
    def __init__(self, factory, api, dataset, json_return):
        self.__api = api
        self.__factory = factory
        self.__json_returned = json_return
        self.__dataset = dataset
        self._is_deleted = False

    def __repr__(self):
        return """\n{} : {} <{}>\n""".format(
            self.__class__.__name__,
            self.name,
            self.id
        ) + ("\t<! This ruleset has been deleted>\n" if self._is_deleted else "") + \
            """\t- Dataset : {}\n\t- Rules count : {}\n\t- Created on : {}\n""".format(
            self.dataset_name,
            self.rules_count,
            self.created.strftime('%Y-%m-%d %H:%M:%S UTC'))

    # Property part
    @property
    def _json(self):
        return self.__json_returned

    @property
    def dataset_name(self):
        return self.__json_returned.get('datasetName')

    @property
    def name(self):
        return self.__json_returned.get('tag', {}).get('tagName')

    @property
    def kpis(self):
        return self.__json_returned.get('tag').get('kpis')

    @property
    def rules_count(self):
        return self.__json_returned.get('rulesCount')

    @property
    def dataset_id(self):
        return self.__json_returned.get('datasetId')

    @property
    def project_id(self):
        return self.__json_returned.get('projectId')

    @property
    def created(self):
        return self.str2date(self.__json_returned.get('lastChangeAt'), '%Y-%m-%dT%H:%M:%S.%fZ')

    @property
    def id(self):
        return self.__json_returned.get('_id')

    # Method part
    @Helper.try_catch
    def get_params(self):
        if not self._is_deleted:
            return NotImplemented

    @Helper.try_catch
    def export(self):
        if not self._is_deleted:
            return NotImplemented

    @Helper.try_catch
    def delete(self):
        """
        Delete the ruleset
        """
        if not self._is_deleted:
            json = {
                '_id': self.id,
                'status': 'done',
                'tagName': self.name
            }
            self.__api.Rules.removealearning(project_ID=self.project_id, dataset_ID=self.dataset_id, json=json)
            self._is_deleted = True
        return self

    @Helper.try_catch
    def minimize(self, minimization_name, score_to_minimize='Purity', increment_threshold=0.01):
        """
        Function to apply a minimization on a ruleset

        Args:
            minimization_name (str): Name of the new ruleset
            score_to_minimize (str): Score to apply the minimization, default is purity
            increment_threshold (float): Percentage increment of target samples that a new rule must bring to be added to the minimized ruleset.

        Returns:
            Ruleset
        """
        if not self._is_deleted:
            return self.__factory.minimize(self, minimization_name, score_to_minimize, increment_threshold)

    @Helper.try_catch
    def get_rules(self, limit=100, sort=None, min_scores=None, max_scores=None, include_variables=None, exclude_variables=None):
        """
        Args:
            limit (int): Number of rules to get, default is 100
            sort (dict): Sorting the rules. Example {'score': 'size', 'asc': true}
            min_scores (dict): Set a minimum on a score. Example {'score': 'Purity', 'value': 0,563}
            max_scores (dict): Set a maximum on a score. Example {'score': 'Coverage', 'value': 300}
            include_variables (str): Variables to include
            exclude_variables (str): Variables to exclude

        Returns:
            List of rules
        """
        if not self._is_deleted:
            json = {'skip': 0,
                    'limit': limit,
                    'tagsfilter': self.name
                    }
            if sort:
                if 'score' in sort and 'asc' in sort:
                    var_name = decode_kpiname_to_id(self.kpis, sort['score'])
                    if sort['asc']:
                        json['sortasc'] = var_name
                    else:
                        json['sortdesc'] = var_name
                else:
                    raise ValueError('Wrong sort parameter, please follow this syntax : {\'score\': String, \'asc\': Boolean}')

            if min_scores:
                if isinstance(min_scores, dict):
                    min_scores = [min_scores]
                for score in min_scores:
                    if 'score' in score and 'value' in score:
                        var_name = decode_kpiname_to_id(self.kpis, score['score'])
                        json['min ' + var_name] = score['value']
                    else:
                        raise ValueError('Wrong min_score parameter, please follow this syntax : {\'score\': String, \'value\': Number}')

            if max_scores:
                if isinstance(max_scores, dict):
                    max_scores = [max_scores]
                for score in max_scores:
                    if 'score' in score and 'value' in score:
                        var_name = decode_kpiname_to_id(self.kpis, score['score'])
                        json['max ' + var_name] = score['value']
                    else:
                        raise ValueError('Wrong max_score parameter, please follow this syntax : {\'score\': String, \'value\': Number}')

            if include_variables:
                if isinstance(include_variables, str):
                    include_variables = [include_variables]
                json['varinclus'] = urllib.parse.quote(','.join(include_variables), safe='~()*!.\'')

            if exclude_variables:
                if isinstance(exclude_variables, str):
                    exclude_variables = [exclude_variables]
                json['varexclus'] = urllib.parse.quote(','.join(exclude_variables), safe='~()*!.\'')

            json_returned = self.__api.Rules.getrules(project_ID=self.project_id, dataset_ID=self.dataset_id, params=json).get('rules')
            return Rules(self.__api, json_returned, self.kpis, self.project_id, self.dataset_id)

    def predict(self, dataset, name, target, nb_minimizations=1, coverage_increment=0.01):
        """
        Create a prediction model from the ruleset

        Args:
            dataset (Dataset): Dataset to apply the prediction
            name (str): Name of the new model
            target (Target): Target used to generate the model
            nb_minimizations (int): Number of minimizations to perform on the ruleset, default is 1
            coverage_increment (float): Percentage increment of target samples that a new rule must bring to be added to the minimized ruleset,
                default is 0.01

        Returns:
            Model
        """
        if not self._is_deleted:
            return ModelFactory(self.__api, self.project_id).predict_from_ruleset(self.__dataset, dataset, self.name, name, target,
                                                                                  nb_minimizations, coverage_increment)
