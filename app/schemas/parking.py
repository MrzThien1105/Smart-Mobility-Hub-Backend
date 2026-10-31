from datetime import datetime

from app.schemas.common import APIModel


class ParkingReservationCreate(APIModel):
    vehicle_id: str
    parking_space_id: str
    starts_at: datetime
    ends_at: datetime


class ParkingReservationOut(APIModel):
    reservation_id: str
    user_id: str
    vehicle_id: str
    parking_space_id: str
    starts_at: datetime | None
    ends_at: datetime | None
    status: str | None = None
