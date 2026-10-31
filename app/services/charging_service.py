from app.models.entities import ChargingPoint, ChargingSession
from app.schemas.charging import ChargingSessionCreate
from app.schemas.charging import ChargingSessionModify


class ChargingService:
    def __init__(self, uow):
        self.uow = uow

    def reserve(self, user_id: str, payload: ChargingSessionCreate) -> ChargingSession:
        raise NotImplementedError

    def request_on_demand(self, user_id: str, payload: ChargingSessionCreate) -> ChargingSession:
        raise NotImplementedError

    def search_available_points(self, criteria: dict) -> list[ChargingPoint]:
        raise NotImplementedError

    def modify(self, session_id: str, user_id: str, payload: ChargingSessionModify) -> ChargingSession:
        raise NotImplementedError

    def cancel(self, session_id: str, user_id: str) -> ChargingSession:
        raise NotImplementedError

    def start(self, session_id: str) -> ChargingSession:
        raise NotImplementedError

    def stop(self, session_id: str, interrupted: bool = False) -> ChargingSession:
        raise NotImplementedError

    def assign_priorities(self) -> list[ChargingSession]:
        raise NotImplementedError

    def fail(self, session_id: str, reason: str) -> ChargingSession:
        raise NotImplementedError

    def update_battery(self, session_id: str, battery_pct: float) -> ChargingSession:
        raise NotImplementedError

    def _session(self, session_id: str) -> ChargingSession:
        raise NotImplementedError

    def _owned_session(self, session_id: str, user_id: str) -> ChargingSession:
        raise NotImplementedError
