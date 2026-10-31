from app.models.entities import Rental, Trip, Vehicle, VehicleReservation
from app.schemas.rental import VehicleReservationCreate


class RentalService:
    def __init__(self, uow):
        self.uow = uow

    def plan_trip(self, student_id: str, trip_data: dict) -> Trip:
        raise NotImplementedError

    def get_trip(self, trip_id: str) -> Trip:
        raise NotImplementedError

    def cancel_trip(self, trip_id: str, student_id: str) -> Trip:
        raise NotImplementedError

    def search_available_vehicles(self, criteria: dict) -> list[Vehicle]:
        raise NotImplementedError

    def reserve_vehicle(self, student_id: str, payload: VehicleReservationCreate) -> VehicleReservation:
        raise NotImplementedError

    def cancel_reservation(self, reservation_id: str, student_id: str) -> VehicleReservation:
        raise NotImplementedError

    def pick_up(self, reservation_id: str, student_id: str) -> Rental:
        raise NotImplementedError

    def return_vehicle(
        self, rental_id: str, student_id: str, return_hub_id: str, condition: str | None = None
    ) -> Rental:
        raise NotImplementedError

    def _reservation(self, reservation_id: str, student_id: str) -> VehicleReservation:
        raise NotImplementedError
