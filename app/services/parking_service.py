from app.models.entities import ParkingReservation, ParkingSession, ParkingSpace, Vehicle
from app.schemas.parking import ParkingReservationCreate


class ParkingService:
    def __init__(self, uow):
        self.uow = uow

    def reserve(self, user_id: str, payload: ParkingReservationCreate) -> ParkingReservation:
        raise NotImplementedError

    def modify_reservation(self, reservation_id: str, user_id: str, changes: dict) -> ParkingReservation:
        raise NotImplementedError

    def search_available_spaces(self, criteria: dict) -> list[ParkingSpace]:
        raise NotImplementedError

    def cancel(self, reservation_id: str, user_id: str) -> ParkingReservation:
        raise NotImplementedError

    def check_in(self, reservation_id: str, user_id: str) -> ParkingSession:
        raise NotImplementedError

    def walk_in(self, user_id: str, vehicle_id: str, parking_space_id: str) -> ParkingSession:
        raise NotImplementedError

    def check_out(self, session_id: str, user_id: str) -> ParkingSession:
        raise NotImplementedError

    def _reservation(self, reservation_id: str, user_id: str) -> ParkingReservation:
        raise NotImplementedError
