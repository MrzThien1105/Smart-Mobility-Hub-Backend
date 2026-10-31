from datetime import datetime

from app.schemas.common import APIModel


class IncidentCreate(APIModel):
    hub_id: str
    vehicle_id: str | None = None
    resource_id: str | None = None
    incident_type: str
    severity: str
    description: str | None = None


class IncidentResolve(APIModel):
    resolution_notes: str | None = None


class RedistributionTaskCreate(APIModel):
    recommendation_id: str | None = None
    vehicle_id: str
    from_hub_id: str
    to_hub_id: str
    priority: int = 0


class SimulationCreate(APIModel):
    scenario_name: str
    scenario_config: dict = {}
