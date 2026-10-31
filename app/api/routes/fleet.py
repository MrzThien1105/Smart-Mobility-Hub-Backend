from fastapi import APIRouter, Depends, status
from app.core.security import get_current_principal
from app.database import get_uow
from app.schemas.fleet import PrivateVehicleCreate, TelemetryCreate, VehicleStatusUpdate
from app.services.fleet_service import FleetService

router = APIRouter()


@router.post("/vehicles/private", status_code=status.HTTP_201_CREATED)
def register_private_vehicle(
    payload: PrivateVehicleCreate,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return FleetService(uow).register_private_vehicle(str(principal["user_id"]), payload)


@router.patch("/vehicles/{vehicle_id}/status")
def update_vehicle_status(
    vehicle_id: str,
    payload: VehicleStatusUpdate,
    uow = Depends(get_uow),
):
    return FleetService(uow).update_status(vehicle_id, payload)


@router.post("/telemetry", status_code=status.HTTP_201_CREATED)
def record_telemetry(payload: TelemetryCreate, uow=Depends(get_uow)):
    return FleetService(uow).record_telemetry(payload)
