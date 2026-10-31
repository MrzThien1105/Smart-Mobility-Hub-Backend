from app.models.entities import (
    CoordinationRecommendation,
    MobilityHub,
    OperationalIncident,
    RedistributionTask,
    Vehicle,
)
from app.schemas.operations import (
    IncidentCreate,
    RedistributionTaskCreate,
)


class OperationService:
    def __init__(self, uow):
        self.uow = uow

    def report_incident(self, reporter_id: str, payload: IncidentCreate) -> OperationalIncident:
        raise NotImplementedError

    def resolve_incident(self, incident_id: str, resolver_id: str) -> OperationalIncident:
        raise NotImplementedError

    def create_distribution_task(
        self, creator_id: str, payload: RedistributionTaskCreate
    ) -> RedistributionTask:
        raise NotImplementedError

    def start_task(self, task_id: str) -> RedistributionTask:
        raise NotImplementedError

    def complete_task(self, task_id: str) -> RedistributionTask:
        raise NotImplementedError

    def cancel_task(self, task_id: str) -> RedistributionTask:
        raise NotImplementedError

    def get_task(self, task_id: str) -> RedistributionTask:
        raise NotImplementedError

    def generate_recommendations(self, simulation_run_id: str) -> list[CoordinationRecommendation]:
        raise NotImplementedError

    def accept_recommendation(self, recommendation_id: str) -> RedistributionTask:
        raise NotImplementedError

    def _task(self, task_id: str) -> RedistributionTask:
        raise NotImplementedError

    def _transition(self, task: RedistributionTask, expected: str, target: str) -> None:
        raise NotImplementedError
