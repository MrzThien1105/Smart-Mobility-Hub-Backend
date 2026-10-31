from datetime import datetime

from app.schemas.common import APIModel


class HubOut(APIModel):
    hub_id: str
    name: str
    hub_type: str | None = None
    latitude: str | None = None
    longitude: str | None = None
    status: str | None = None


class VehicleOut(APIModel):
    vehicle_id: str
    license_plate: str
    current_hub_id: str | None = None
    vehicle_type: str | None = None
    ownership_type: str | None = None
    battery_pct: float | None = None
    status: str | None = None
