from app.models.entities import (
    ChargingPoint,
    ChargingSession,
    CoordinationRecommendation,
    HubResource,
    MobilityHub,
    OperationalIncident,
    ParkingReservation,
    ParkingSession,
    ParkingSpace,
    PrivateVehicle,
    PublicVehicle,
    RedistributionTask,
    Rental,
    SensorTelemetry,
    SimulationRun,
    Trip,
    Role,
    StudentProfile,
    User,
    UserRole,
    Vehicle,
    VehicleReservation,
)
from app.repositories.base import BaseRepository


class VehicleRepository(BaseRepository[Vehicle]):
    model = Vehicle


class PrivateVehicleRepository(BaseRepository[PrivateVehicle]):
    model = PrivateVehicle


class PublicVehicleRepository(BaseRepository[PublicVehicle]):
    model = PublicVehicle


class SensorTelemetryRepository(BaseRepository[SensorTelemetry]):
    model = SensorTelemetry


class MobilityHubRepository(BaseRepository[MobilityHub]):
    model = MobilityHub


class HubResourceRepository(BaseRepository[HubResource]):
    model = HubResource


class ParkingReservationRepository(BaseRepository[ParkingReservation]):
    model = ParkingReservation


class ParkingSessionRepository(BaseRepository[ParkingSession]):
    model = ParkingSession


class ParkingSpaceRepository(BaseRepository[ParkingSpace]):
    model = ParkingSpace


class ChargingSessionRepository(BaseRepository[ChargingSession]):
    model = ChargingSession


class ChargingPointRepository(BaseRepository[ChargingPoint]):
    model = ChargingPoint


class RentalRepository(BaseRepository[Rental]):
    model = Rental


class TripRepository(BaseRepository[Trip]):
    model = Trip


class VehicleReservationRepository(BaseRepository[VehicleReservation]):
    model = VehicleReservation


class OperationalIncidentRepository(BaseRepository[OperationalIncident]):
    model = OperationalIncident


class SimulationRunRepository(BaseRepository[SimulationRun]):
    model = SimulationRun


class CoordinationRecommendationRepository(BaseRepository[CoordinationRecommendation]):
    model = CoordinationRecommendation


class RedistributionTaskRepository(BaseRepository[RedistributionTask]):
    model = RedistributionTask


class UserRepository(BaseRepository[User]):
    model = User


class RoleRepository(BaseRepository[Role]):
    model = Role


class UserRoleRepository(BaseRepository[UserRole]):
    model = UserRole


class StudentProfileRepository(BaseRepository[StudentProfile]):
    model = StudentProfile
