from fastapi import APIRouter, Depends, status
from app.core.security import get_current_principal
from app.database import get_uow
from app.schemas.rental import RentalReturn, VehicleReservationCreate, VehicleReservationOut
from app.services.rental_service import RentalService

router = APIRouter()


@router.post("/reservations", response_model=VehicleReservationOut, status_code=status.HTTP_201_CREATED)
def create_reservation(
    payload: VehicleReservationCreate,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return RentalService(uow).reserve_vehicle(str(principal["user_id"]), payload)


@router.post("/reservations/{reservation_id}/cancel", response_model=VehicleReservationOut)
def cancel_reservation(
    reservation_id: str,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return RentalService(uow).cancel_reservation(reservation_id, str(principal["user_id"]))


@router.post("/reservations/{reservation_id}/pickup")
def pick_up_vehicle(
    reservation_id: str,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return RentalService(uow).pick_up(reservation_id, str(principal["user_id"]))


@router.post("/rentals/{rental_id}/return")
def return_vehicle(
    rental_id: str,
    payload: RentalReturn,
    uow = Depends(get_uow),
    principal: dict[str, object] = Depends(get_current_principal),
):
    return RentalService(uow).return_vehicle(
        rental_id,
        str(principal["user_id"]),
        payload.return_hub_id,
        payload.return_condition,
    )
