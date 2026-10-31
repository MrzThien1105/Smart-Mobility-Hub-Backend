from fastapi import APIRouter, Depends, status
from app.core.security import get_current_principal
from app.database import get_uow
from app.schemas.charging import (
    ChargingSessionCreate,
    ChargingSessionModify,
    ChargingSessionOut,
)
from app.services.charging_service import ChargingService

router = APIRouter()


@router.post("/sessions", response_model=ChargingSessionOut, status_code=status.HTTP_201_CREATED)
def reserve_charging(
    payload: ChargingSessionCreate,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return ChargingService(uow).reserve(str(principal["user_id"]), payload)


@router.patch("/sessions/{session_id}", response_model=ChargingSessionOut)
def modify_session(
    session_id: str,
    payload: ChargingSessionModify,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return ChargingService(uow).modify(session_id, str(principal["user_id"]), payload)


@router.post("/sessions/{session_id}/cancel", response_model=ChargingSessionOut)
def cancel_session(
    session_id: str,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return ChargingService(uow).cancel(session_id, str(principal["user_id"]))


@router.post("/sessions/{session_id}/start", response_model=ChargingSessionOut)
def start_session(session_id: str, uow=Depends(get_uow)):
    return ChargingService(uow).start(session_id)


@router.post("/sessions/{session_id}/stop", response_model=ChargingSessionOut)
def stop_session(
    session_id: str,
    interrupted: bool = False,
    uow = Depends(get_uow),
):
    return ChargingService(uow).stop(session_id, interrupted)


@router.post("/priorities/recalculate", response_model=list[ChargingSessionOut])
def recalculate_priorities(uow=Depends(get_uow)):
    return ChargingService(uow).assign_priorities()
