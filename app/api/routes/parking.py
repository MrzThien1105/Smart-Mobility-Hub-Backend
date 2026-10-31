from fastapi import APIRouter, Depends, status
from app.core.security import get_current_principal
from app.database import get_uow
from app.schemas.parking import ParkingReservationCreate, ParkingReservationOut
from app.services.parking_service import ParkingService

router = APIRouter()


@router.post("/reservations", response_model=ParkingReservationOut, status_code=status.HTTP_201_CREATED)
def reserve_parking(
    payload: ParkingReservationCreate,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return ParkingService(uow).reserve(str(principal["user_id"]), payload)


@router.post("/reservations/{reservation_id}/cancel", response_model=ParkingReservationOut)
def cancel_reservation(
    reservation_id: str,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return ParkingService(uow).cancel(reservation_id, str(principal["user_id"]))


@router.post("/reservations/{reservation_id}/check-in")
def check_in(
    reservation_id: str,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return ParkingService(uow).check_in(reservation_id, str(principal["user_id"]))


@router.post("/sessions/{session_id}/check-out")
def check_out(
    session_id: str,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return ParkingService(uow).check_out(session_id, str(principal["user_id"]))
