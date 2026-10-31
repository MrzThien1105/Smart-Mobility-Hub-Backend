from app.models.entities import HubResource, MobilityHub, Vehicle


class MobilityService:
    def __init__(self, uow):
        self.uow = uow

    def search_hubs(self, criteria: dict) -> list[MobilityHub]:
        raise NotImplementedError

    def get_hub(self, hub_id: str) -> MobilityHub:
        raise NotImplementedError

    def create_hub(self, hub_data: dict) -> MobilityHub:
        raise NotImplementedError

    def update_hub(self, hub_id: str, changes: dict) -> MobilityHub:
        raise NotImplementedError

    def search_resources(self, hub_id: str | None, resource_type: str | None) -> list[HubResource]:
        raise NotImplementedError

    def create_resource(self, hub_id: str, resource_data: dict) -> HubResource:
        raise NotImplementedError

    def deactivate_resource(self, resource_id: str) -> HubResource:
        raise NotImplementedError

    def search_available_vehicles(
        self,
        hub_id: str | None = None,
        vehicle_type: str | None = None,
        battery_min: float | None = None,
    ) -> list[Vehicle]:
        raise NotImplementedError

    def calculate_hub_capacity(self, hub_id: str) -> dict:
        raise NotImplementedError
