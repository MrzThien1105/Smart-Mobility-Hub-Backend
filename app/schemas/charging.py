from datetime import datetime

from app.schemas.common import APIModel


class ChargingSessionCreate(APIModel):
    vehicle_id: str
    charging_point_id: str
    target_battery_pct: float | None = None
    target_duration_minutes: int | None = None
    scheduled_start_time: datetime | None = None


class ChargingSessionOut(APIModel):
    session_id: str
    user_id: str
    vehicle_id: str
    charging_point_id: str
    priority_score: int | None = None
    status: str | None = None


class ChargingSessionModify(APIModel):
    charging_point_id: str | None = None
    target_battery_pct: float | None = None
    target_duration_minutes: int | None = None
    scheduled_start_time: datetime | None = None
