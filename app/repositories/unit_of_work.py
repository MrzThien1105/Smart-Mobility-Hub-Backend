from sqlalchemy.orm import Session

from app.repositories.domain import (
    ChargingPointRepository,
    ChargingSessionRepository,
    CoordinationRecommendationRepository,
    HubResourceRepository,
    MobilityHubRepository,
    OperationalIncidentRepository,
    ParkingReservationRepository,
    ParkingSessionRepository,
    ParkingSpaceRepository,
    PrivateVehicleRepository,
    PublicVehicleRepository,
    RedistributionTaskRepository,
    RoleRepository,
    StudentProfileRepository,
    RentalRepository,
    SensorTelemetryRepository,
    SimulationRunRepository,
    TripRepository,
    UserRepository,
    UserRoleRepository,
    VehicleRepository,
    VehicleReservationRepository,
)


class UnitOfWork:
    def __init__(self, session: Session):
        self.session = session
        self.vehicles = VehicleRepository(session)
        self.private_vehicles = PrivateVehicleRepository(session)
        self.public_vehicles = PublicVehicleRepository(session)
        self.telemetry = SensorTelemetryRepository(session)
        self.hubs = MobilityHubRepository(session)
        self.resources = HubResourceRepository(session)
        self.parking_reservations = ParkingReservationRepository(session)
        self.parking_sessions = ParkingSessionRepository(session)
        self.parking_spaces = ParkingSpaceRepository(session)
        self.charging_sessions = ChargingSessionRepository(session)
        self.charging_points = ChargingPointRepository(session)
        self.rentals = RentalRepository(session)
        self.trips = TripRepository(session)
        self.reservations = VehicleReservationRepository(session)
        self.incidents = OperationalIncidentRepository(session)
        self.runs = SimulationRunRepository(session)
        self.recommendations = CoordinationRecommendationRepository(session)
        self.tasks = RedistributionTaskRepository(session)
        self.users = UserRepository(session)
        self.roles = RoleRepository(session)
        self.user_roles = UserRoleRepository(session)
        self.student_profiles = StudentProfileRepository(session)

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def close(self) -> None:
        self.session.close()

    def __enter__(self) -> "UnitOfWork":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if exc_type is None:
            self.commit()
        else:
            self.rollback()
        self.close()
