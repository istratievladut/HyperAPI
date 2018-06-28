from hypercube_api.hyper_api.constraint import Constraint


class Rules(list):
    """
    """
    def __init__(self, api, json, kpis, project_id, dataset_id):
        self.__api = api
        self.__kpis = kpis
        self.__project_id = project_id
        self.__dataset_id = dataset_id
        self.__rules = [Rule(x, kpis) for x in json]
        super().__init__(Rule(x, kpis) for x in json)

    def __repr__(self):
        return ''.join([r.__repr__() for r in self.__rules])

    def tag(self, tags_name):
        """
        Args:
            tags_name: Names of the new tag you want to add

        Returns:
            Update the tags of your rules
        """
        if isinstance(tags_name, str):
            tags_name = [tags_name]

        json = {
            'kpis': self.__kpis,
            'ruleIds': [rule.id for rule in self.__rules],
            'tagsToAdd': tags_name,
            'tagsToDelete': []
        }
        self.__api.Rules.updatetagsofrules(project_ID=self.__project_id, dataset_ID=self.__dataset_id, json=json)


class Rule:
    def __init__(self, json, kpi_mapping):
        self.__json = json
        self.__constraints = [Constraint(cons) for cons in json.get('constraints')]
        self.__mapping = kpi_mapping

    def __repr__(self):
        constraints = '\n'.join([x.__repr__() for x in self.__constraints])
        scores = '\n\t'.join('\x1b[4m' + key + '\x1b[0m: ' + str(value) for key, value in self.scores.items())
        return ('\n\x1b[31m\x1b[1mConstraints\x1b[0m \n' + constraints + '\n\x1b[34m\x1b[1mScores\x1b[0m \n\t' + scores + '\n\n').expandtabs(3)

    @property
    def constraints(self):
        return self.__constraints

    @property
    def id(self):
        return self.__json.get('_id')

    @property
    def tags(self):
        return self.__json.get('tags')

    @property
    def scores(self):
        scores = {}
        for key, value in self.__json.get('scores').items():
            scores[decode_id_to_kpiname(self.__mapping, key).capitalize()] = value
        return scores


def decode_id_to_kpiname(mapping, _id):
    decoded_type = [('{} {}'.format(x.get('scoreType'), x.get('kpiName'))) for x in mapping if _id == x['kpiId']]
    if decoded_type:
        return decoded_type[0]
    else:
        return str(_id)


def decode_kpiname_to_id(mapping, name):
    decoded_type = [x['kpiId'] for x in mapping if name.capitalize() == x['scoreType']]
    if decoded_type:
        return decoded_type[0]
    else:
        return name
