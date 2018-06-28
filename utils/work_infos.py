import datetime


def strmongo_to_datetime(value):
    return datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')


class WorkInfo(object):
    def __init__(self, work):
        self._id = work.get('_id')
        self.type = work.get('type')
        self.status = work.get('_status', {}).get('kind').upper()
        self.reason = work.get('_status', {}).get('reason', None)
        self.ram = work.get('resources', {}).get('ram', None)
        _td = strmongo_to_datetime(work.get('lastUpdatedAt')) - strmongo_to_datetime(work.get('createdAt'))
        self.duration = _td.total_seconds()

    def __str__(self):
        msg = "{s.type: >20} <{s._id}>   {s.status: >12} : {s.duration:.3f}s  {s.ram: .3f}GB".format(s=self)
        if self.status == 'ERROR':
            msg += "\n\t{}".format(self.reason)
        return msg

    def __repr__(self):
        return self.__str__()
