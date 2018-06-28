from hypercube_api.sessionClass import Session

from hypercube_api.hdp_api.routes.alerts import Alerts
from hypercube_api.hdp_api.routes.analytics import Analytics
from hypercube_api.hdp_api.routes.auxdata import AuxData
from hypercube_api.hdp_api.routes.color import Color
from hypercube_api.hdp_api.routes.correlations import Correlations
from hypercube_api.hdp_api.routes.dashboards import Dashboards
from hypercube_api.hdp_api.routes.datasets import Datasets
from hypercube_api.hdp_api.routes.datasetReshapes import DatasetReshapes
from hypercube_api.hdp_api.routes.docapi import DocApi
from hypercube_api.hdp_api.routes.exports import Exports
from hypercube_api.hdp_api.routes.hyperEngines import HyperEngines
from hypercube_api.hdp_api.routes.joinDatasets import JoinDatasets
from hypercube_api.hdp_api.routes.kpi import Kpi
from hypercube_api.hdp_api.routes.map import Map
from hypercube_api.hdp_api.routes.nitro import Nitro
from hypercube_api.hdp_api.routes.notebooks import Notebooks
from hypercube_api.hdp_api.routes.optimProcess import OptimProcess
from hypercube_api.hdp_api.routes.prediction import Prediction
from hypercube_api.hdp_api.routes.projects import Projects
from hypercube_api.hdp_api.routes.projectResources import ProjectResources
from hypercube_api.hdp_api.routes.query import Query
from hypercube_api.hdp_api.routes.reports import Reports
from hypercube_api.hdp_api.routes.rules import Rules
from hypercube_api.hdp_api.routes.rulesetViz import RulesetViz
from hypercube_api.hdp_api.routes.schedulerDashboard import SchedulerDashboard
from hypercube_api.hdp_api.routes.simpleLift import SimpleLift
from hypercube_api.hdp_api.routes.system import System
from hypercube_api.hdp_api.routes.tags import Tags
from hypercube_api.hdp_api.routes.task import Task
from hypercube_api.hdp_api.routes.tempData import TempData
from hypercube_api.hdp_api.routes.textProcessing import TextProcessing
from hypercube_api.hdp_api.routes.timeSeriesQuery import TimeSeriesQuery
from hypercube_api.hdp_api.routes.timeSeriesViz import TimeSeriesViz
from hypercube_api.hdp_api.routes.identities import Identities
from hypercube_api.hdp_api.routes.variable import Variable
from hypercube_api.hdp_api.routes.visualization import Visualization
from hypercube_api.hdp_api.routes.workalendar import Workalendar
from hypercube_api.hdp_api.routes.workflows import Workflows
from hypercube_api.hdp_api.routes.settings import Settings
from hypercube_api.hdp_api.routes.monitoring import Monitoring
from hypercube_api.hdp_api.routes.authentication import Authentication
from hypercube_api.hdp_api._timeoutSettings import TimeOutSettings


class Router(object):
    _resources = [
        Alerts,
        Analytics,
        AuxData,
        Color,
        Correlations,
        Dashboards,
        Datasets,
        DatasetReshapes,
        DocApi,
        Exports,
        HyperEngines,
        JoinDatasets,
        Kpi,
        Map,
        Monitoring,
        Nitro,
        Notebooks,
        OptimProcess,
        Prediction,
        Projects,
        ProjectResources,
        Query,
        Reports,
        Rules,
        RulesetViz,
        SchedulerDashboard,
        SimpleLift,
        System,
        Tags,
        Task,
        TempData,
        TextProcessing,
        TimeSeriesQuery,
        TimeSeriesViz,
        Identities,
        Variable,
        Visualization,
        Workalendar,
        Workflows,
        Settings,
        Authentication
    ]

    def __init__(self, username=None, password=None, url=None, token=None, watcher=None):
        # Initiate session with HyperCube server
        self.session = Session(username=username, password=password, token=token, url=url)

        for resourceCls in self._resources:
            self.__setattr__(resourceCls.__name__, resourceCls(self.session, watcher=watcher))
        self._default_timeout_settings = TimeOutSettings()

    def refresh_session(self, username=None, password=None, token=None):
        self.session.refresh(username, password, token)

    def __iter__(self):
        for resourceCls in self._resources:
            yield self.__getattribute__(resourceCls.__name__)

    # Work Management Specific Code ---------------------------------------------------------------------

    def handle_work_states(self, project_id, work_type=None, work_id=None, query=None, timeout_settings=None):
        if timeout_settings is None:
            timeout_settings = self._default_timeout_settings

        def _getStatus(work):
            if work is None:
                return None
            return work.get('_status', {}).get('kind', None)

        work_data = {'projectId': project_id}
        if work_type is not None and query is not None:
            work_data['type'] = work_type
            work_data.update(query)
        elif work_id is not None:
            work_data['_id'] = work_id
        else:
            raise ValueError('Missing conditions for works')

        _works = self.Task.task.wait_until(project_ID=project_id, json=work_data, condition=lambda x: len(x) > 0)
        if not _works:
            # List empty, the work has not been created
            if work_id:
                raise ValueError('The work <{}> could not be found'.format(work_id))
            raise ValueError('The corresponding work could not be found')

        _work = next(iter(_works))

        while _getStatus(_work) != 'done':
            if _getStatus(_work) is None:
                raise ValueError('Missing Status on work <{}>'.format(work_id))

            if _getStatus(_work) == 'error':
                raise ValueError('Work "{}" <{}> has failed'.format(_work.get("type", "Unknown type"), work_id))

            if _getStatus(_work) == 'starting':
                _works = self.Task.task.wait_until(condition=lambda x: _getStatus(x[-1]) != 'starting',
                                                   timeout=timeout_settings.get_starting_timeout(),
                                                   project_ID=project_id, json=work_data)

            elif _getStatus(_work) == 'creating':
                _works = self.Task.task.wait_until(condition=lambda x: _getStatus(x[-1]) != 'creating' and _getStatus(x[-1]) != 'pending',
                                                   timeout=timeout_settings.get_pending_timeout(),
                                                   project_ID=project_id, json=work_data)

            elif _getStatus(_work) == 'pending':
                _works = self.Task.task.wait_until(condition=lambda x: _getStatus(x[-1]) != 'pending',
                                                   timeout=timeout_settings.get_pending_timeout(),
                                                   project_ID=project_id, json=work_data)

            elif _getStatus(_work) == 'inprogress':
                _works = self.Task.task.wait_until(condition=lambda x: _getStatus(x[-1]) != 'inprogress',
                                                   timeout=timeout_settings.get_progress_timeout(),
                                                   project_ID=project_id, json=work_data)

            if _works is None:
                if work_type:
                    msg = 'Timeout reached on work "{}" <{}>'.format(work_type, work_id)
                else:
                    msg = 'Timeout reached on work <{}>'.format(work_id)
                raise ValueError(msg)

            _work = next(iter(_works))
        return _work
