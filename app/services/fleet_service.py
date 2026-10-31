from app.models.entities import PrivateVehicle, PublicVehicle, SensorTelemetry, Vehicle
from app.schemas.fleet import PrivateVehicleCreate, TelemetryCreate, VehicleStatusUpdate


class FleetService:
    def __init__(self, uow):
        self.uow = uow

    def register_private_vehicle(self, owner_id: str, payload: PrivateVehicleCreate) -> Vehicle:
        raise NotImplementedError

    def get_vehicle(self, vehicle_id: str) -> Vehicle:
        raise NotImplementedError

    def search_vehicles(self, criteria: dict) -> list[Vehicle]:
        raise NotImplementedError

    def update_status(self, vehicle_id: str, payload: VehicleStatusUpdate) -> Vehicle:
        raise NotImplementedError

    def record_telemetry(self, payload: TelemetryCreate) -> SensorTelemetry:
        raise NotImplementedError

    def process_telemetry(self, telemetry_id: str) -> dict:
        raise NotImplementedError

    def schedule_maintenance(self, vehicle_id: str, scheduled_at: str) -> PublicVehicle:
        raise NotImplementedError

    def mark_in_transit(self, vehicle_id: str, from_hub_id: str, to_hub_id: str) -> Vehicle:
        raise NotImplementedError
