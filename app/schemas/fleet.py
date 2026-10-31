from app.schemas.common import APIModel


class PrivateVehicleCreate(APIModel):
    license_plate: str
    current_hub_id: str | None = None
    vehicle_type: str | None = None
    battery_pct: float | None = None
    rfid_tag_code: str | None = None


class VehicleStatusUpdate(APIModel):
    status: str
    current_hub_id: str | None = None
    battery_pct: float | None = None


class TelemetryCreate(APIModel):
    vehicle_id: str | None = None
    resource_id: str | None = None
    metric_name: str
    metric_value: float | None = None
    is_simulated: bool = False
