from fastapi import APIRouter, Depends, status
from app.core.security import get_current_principal
from app.database import get_uow
from app.schemas.operations import IncidentCreate, RedistributionTaskCreate, SimulationCreate
from app.services.operation_service import OperationService
from app.services.simulation_service import SimulationService

router = APIRouter()


@router.post("/incidents", status_code=status.HTTP_201_CREATED)
def report_incident(
    payload: IncidentCreate,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return OperationService(uow).report_incident(str(principal["user_id"]), payload)


@router.post("/incidents/{incident_id}/resolve")
def resolve_incident(
    incident_id: str,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return OperationService(uow).resolve_incident(incident_id, str(principal["user_id"]))


@router.post("/redistribution-tasks", status_code=status.HTTP_201_CREATED)
def create_redistribution_task(
    payload: RedistributionTaskCreate,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return OperationService(uow).create_distribution_task(str(principal["user_id"]), payload)


@router.post("/redistribution-tasks/{task_id}/start")
def start_redistribution_task(task_id: str, uow=Depends(get_uow)):
    return OperationService(uow).start_task(task_id)


@router.post("/redistribution-tasks/{task_id}/complete")
def complete_redistribution_task(task_id: str, uow=Depends(get_uow)):
    return OperationService(uow).complete_task(task_id)


@router.post("/simulations", status_code=status.HTTP_201_CREATED)
def run_simulation(
    payload: SimulationCreate,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return SimulationService(uow).run(str(principal["user_id"]), payload)
