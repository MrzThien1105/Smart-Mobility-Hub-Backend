from datetime import datetime

from app.schemas.common import APIModel


class VehicleReservationCreate(APIModel):
    trip_id: str | None = None
    vehicle_id: str
    planned_start_at: datetime | None = None
    pickup_deadline_at: datetime | None = None


class VehicleReservationOut(APIModel):
    reservation_id: str
    trip_id: str | None
    student_id: str
    vehicle_id: str
    reserved_at: datetime
    status: str | None = None


class RentalReturn(APIModel):
    return_hub_id: str
    return_condition: str | None = None
