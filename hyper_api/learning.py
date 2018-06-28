from json import loads
from hypercube_api.util import Helper
from hypercube_api.hyper_api.base import Base
from hypercube_api.hyper_api.target import TargetFactory


class HyperCubeClassifierFactory:
    def __init__(self, api):
        self.__api = api

    def __call__(self, *args, **kwargs):
        return self.create(*args, **kwargs)

    @Helper.try_catch
    def create(self, name, nb_quantiles=10, discretization={},
               score_thresholds={'Purity': 0.1, 'Coverage': 0.01, 'Z-score': 1, 'Lift': 1},
               complexity=2, min_coverage_contribution=0.1):
        local_dict = locals()
        local_dict.pop('self')
        return HyperCubeClassifier(self.__api, {}, {}, local_dict)

    @Helper.try_catch
    def get_by_dataset(self):
        return NotImplemented

    @Helper.try_catch
    def get(self, project, name):
        return list(filter(lambda x: x.name == name, self.filter(project)))[0]

    @Helper.try_catch
    def get_or_create(self):
        return self.get() or self.create()

    @Helper.try_catch
    def filter(self, project):
        project_id = project if type(project) is str else project.project_id
        json = {'project_ID': project_id}

        return list(filter(None, map(lambda x: HyperCubeClassifier(self.__api, json, x, None) if not x.get('status') else None,
                                     self.__api.Rules.getlearnings(**json))))


class HyperCubeClassifier(Base):
    def __init__(self, api, json_sent, json_return, param_dict):
        self.__api = api
        self.__json_sent = json_sent
        self.__json_returned = json_return
        self.__params = param_dict

    @property
    def Targets(self):
        return list(map(lambda x: TargetFactory(self.__api).get_by_id(x.get('kpiId')),
                        loads(self.__json_returned.get('tag').get('kpis'))))

    @property
    def name(self):
        return self.__json_returned.get('tag', {}).get('tagName')

    @property
    def rules_count(self):
        return self.__json_returned.get('rulesCount')

    @property
    def dataset_id(self):
        return self.__json_returned.get('datasetId')

    @property
    def created(self):
        return self.__json_returned.get('lastChangeAt')

    @property
    def id(self):
        return self.__json_returned.get('_id')

    @Helper.try_catch
    def update(self):
        return NotImplemented

    @Helper.try_catch
    def fit(self, dataset, target):
        data = {
            "projectId": dataset.project_id,
            "task": {
                "type": "learning",
                "datasetId": dataset.dataset_id,
                "projectId": dataset.project_id,
                "params": {
                    "learningName": self.__params.get('name'),
                    "datasetName": dataset.name,
                    "buildPredictiveModel": 0,
                    "complexityExhaustive": self.__params.get('complexity'),
                    "countQuantiles": self.__params.get('nb_quantiles'),
                    "discretizations": self.__params.get('discretization'),
                    "minMarginalContribution": self.__params.get('min_coverage_contribution'),
                    "target": [],
                    "kpis": []
                }
            }
        }

        _kpi = target._json
        _minValues = self.__params.get('score_thresholds')

        for _score in _kpi.get('scores'):
            _kpiData = {
                "kpiId": _score.get('kpiId'),
                "type": _score.get('type'),
                "minValue": _minValues.get(_score.get('type')),
                "kpiFamily": "target",
                "scoreType": _score.get('type'),
                "kpiType": _kpi.get('type'),
                "output": _kpi.get('variable'),
                "kpiName": _kpi.get('name'),
                "omodality": _kpi.get('modality')
            }
            data['task']['params']['target'].append(_kpiData)

        self.__json_returned = self.__api.SimpleLift.newsimplelift(project_ID=dataset.project_id, json=data)

        return HyperCubeClassifierFactory(self.__api).get(dataset.project_id, self.__params.get('name'))

    @Helper.try_catch
    def get_params(self):
        return self.__params

    @Helper.try_catch
    def export(self):
        return NotImplemented

    @Helper.try_catch
    def delete(self):
        return NotImplemented

    @Helper.try_catch
    def minimize(self):
        return NotImplemented

    @Helper.try_catch
    def predict(self):
        return NotImplemented
