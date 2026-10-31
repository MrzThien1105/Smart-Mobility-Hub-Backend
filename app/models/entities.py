from sqlalchemy import CheckConstraint, Column, Float, ForeignKey, Integer, String, Text

from app.database import Base


def uuid_column(name: str = None):
    return Column(String, primary_key=True) if name is None else Column(name, String, primary_key=True)


class User(Base):
    __tablename__ = "USER"
    user_id = Column(String, primary_key=True)
    sso_subject = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True)
    display_name = Column(String)
    user_type = Column(String, CheckConstraint("user_type IN ('STUDENT','OPERATOR')"))
    status = Column(String)


class Role(Base):
    __tablename__ = "ROLE"
    role_id = Column(String, primary_key=True)
    name = Column(String, unique=True, nullable=False)


class UserRole(Base):
    __tablename__ = "USER_ROLE"
    user_id = Column(String, ForeignKey("USER.user_id", ondelete="CASCADE"), primary_key=True)
    role_id = Column(String, ForeignKey("ROLE.role_id", ondelete="CASCADE"), primary_key=True)


class MobilityHub(Base):
    __tablename__ = "MOBILITY_HUB"
    hub_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    hub_type = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    max_parking_capacity = Column(Integer, default=0)
    max_charging_capacity = Column(Integer, default=0)
    status = Column(String)


class HubResource(Base):
    __tablename__ = "HUB_RESOURCE"
    resource_id = Column(String, primary_key=True)
    hub_id = Column(String, ForeignKey("MOBILITY_HUB.hub_id"), nullable=False)
    code = Column(String, nullable=False)
    resource_type = Column(String, CheckConstraint("resource_type IN ('PARKING_SPACE','CHARGING_POINT')"))


class Vehicle(Base):
    __tablename__ = "VEHICLE"
    vehicle_id = Column(String, primary_key=True)
    license_plate = Column(String, unique=True, nullable=False)
    current_hub_id = Column(String, ForeignKey("MOBILITY_HUB.hub_id"))
    vehicle_type = Column(String)
    ownership_type = Column(String, CheckConstraint("ownership_type IN ('PUBLIC','PRIVATE')"))
    battery_pct = Column(Float)
    status = Column(String)


class StudentProfile(Base):
    __tablename__ = "STUDENT_PROFILE"
    user_id = Column(String, ForeignKey("USER.user_id", ondelete="CASCADE"), primary_key=True)
    student_code = Column(String, unique=True, nullable=False)
    university_name = Column(String)
    faculty = Column(String)


class Trip(Base):
    __tablename__ = "TRIP"
    trip_id = Column(String, primary_key=True)
    student_id = Column(String, ForeignKey("USER.user_id"), nullable=False)
    origin_hub_id = Column(String, ForeignKey("MOBILITY_HUB.hub_id"), nullable=False)
    destination_hub_id = Column(String, ForeignKey("MOBILITY_HUB.hub_id"), nullable=False)
    planned_departure = Column(String)
    status = Column(String)


class VehicleReservation(Base):
    __tablename__ = "VEHICLE_RESERVATION"
    reservation_id = Column(String, primary_key=True)
    trip_id = Column(String, ForeignKey("TRIP.trip_id"))
    student_id = Column(String, ForeignKey("USER.user_id"), nullable=False)
    vehicle_id = Column(String, ForeignKey("VEHICLE.vehicle_id"), nullable=False)
    reserved_at = Column(String, nullable=False)
    planned_start_at = Column(String)
    pickup_deadline_at = Column(String)
    status = Column(String)


class Rental(Base):
    __tablename__ = "RENTAL"
    rental_id = Column(String, primary_key=True)
    reservation_id = Column(String, ForeignKey("VEHICLE_RESERVATION.reservation_id"), unique=True, nullable=False)
    origin_hub_id = Column(String, ForeignKey("MOBILITY_HUB.hub_id"), nullable=False)
    return_hub_id = Column(String, ForeignKey("MOBILITY_HUB.hub_id"))
    picked_up_at = Column(String)
    returned_at = Column(String)
    return_condition = Column(String)
    status = Column(String)


class ParkingSpace(Base):
    __tablename__ = "PARKING_SPACE"
    resource_id = Column(String, ForeignKey("HUB_RESOURCE.resource_id", ondelete="CASCADE"), primary_key=True)
    supported_vehicle_type = Column(String)


class ParkingReservation(Base):
    __tablename__ = "PARKING_RESERVATION"
    reservation_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("USER.user_id"), nullable=False)
    vehicle_id = Column(String, ForeignKey("VEHICLE.vehicle_id"), nullable=False)
    parking_space_id = Column(String, ForeignKey("PARKING_SPACE.resource_id"), nullable=False)
    starts_at = Column(String)
    ends_at = Column(String)
    status = Column(String)


class ParkingSession(Base):
    __tablename__ = "PARKING_SESSION"
    session_id = Column(String, primary_key=True)
    reservation_id = Column(String, ForeignKey("PARKING_RESERVATION.reservation_id"))
    user_id = Column(String, ForeignKey("USER.user_id"), nullable=False)
    vehicle_id = Column(String, ForeignKey("VEHICLE.vehicle_id"), nullable=False)
    parking_space_id = Column(String, ForeignKey("PARKING_SPACE.resource_id"), nullable=False)
    checked_in_at = Column(String)
    checked_out_at = Column(String)


class ChargingPoint(Base):
    __tablename__ = "CHARGING_POINT"
    resource_id = Column(String, ForeignKey("HUB_RESOURCE.resource_id", ondelete="CASCADE"), primary_key=True)
    connector_type = Column(String)
    max_power_kw = Column(Float)


class ChargingSession(Base):
    __tablename__ = "CHARGING_SESSION"
    session_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("USER.user_id"), nullable=False)
    vehicle_id = Column(String, ForeignKey("VEHICLE.vehicle_id"), nullable=False)
    charging_point_id = Column(String, ForeignKey("CHARGING_POINT.resource_id"), nullable=False)
    target_battery_pct = Column(Float)
    target_duration_minutes = Column(Integer)
    priority_score = Column(Integer)
    scheduled_start_time = Column(String)
    actual_start_time = Column(String)
    status = Column(String)


class ChargingPolicy(Base):
    __tablename__ = "CHARGING_POLICY"
    policy_id = Column(String, primary_key=True)
    hub_id = Column(String, ForeignKey("MOBILITY_HUB.hub_id"), nullable=False)
    updated_by_user_id = Column(String, ForeignKey("USER.user_id"), nullable=False)
    priority_weights = Column(Text)
    low_battery_threshold_pct = Column(Float)
    is_active = Column(Integer)


class PublicVehicle(Base):
    __tablename__ = "PUBLIC_VEHICLE"
    vehicle_id = Column(String, ForeignKey("VEHICLE.vehicle_id", ondelete="CASCADE"), primary_key=True)
    fleet_batch_code = Column(String)
    maintenance_schedule = Column(String)


class PrivateVehicle(Base):
    __tablename__ = "PRIVATE_VEHICLE"
    vehicle_id = Column(String, ForeignKey("VEHICLE.vehicle_id", ondelete="CASCADE"), primary_key=True)
    owner_id = Column(String, ForeignKey("USER.user_id"), nullable=False)
    rfid_tag_code = Column(String)


class SensorTelemetry(Base):
    __tablename__ = "SENSOR_TELEMETRY"
    sensor_id = Column(String, primary_key=True)
    vehicle_id = Column(String, ForeignKey("VEHICLE.vehicle_id"))
    resource_id = Column(String, ForeignKey("HUB_RESOURCE.resource_id"))
    metric_name = Column(String, nullable=False)
    metric_value = Column(Float)
    is_simulated = Column(Integer)
    timestamp = Column(String, nullable=False)
    __table_args__ = (
        CheckConstraint(
            "(vehicle_id IS NOT NULL AND resource_id IS NULL) OR "
            "(vehicle_id IS NULL AND resource_id IS NOT NULL)",
            name="chk_telemetry_fks",
        ),
    )


class OperationalIncident(Base):
    __tablename__ = "OPERATIONAL_INCIDENT"
    incident_id = Column(String, primary_key=True)
    hub_id = Column(String, ForeignKey("MOBILITY_HUB.hub_id"), nullable=False)
    vehicle_id = Column(String, ForeignKey("VEHICLE.vehicle_id"))
    resource_id = Column(String, ForeignKey("HUB_RESOURCE.resource_id"))
    reported_by_user_id = Column(String, ForeignKey("USER.user_id"), nullable=False)
    resolved_by_user_id = Column(String, ForeignKey("USER.user_id"))
    incident_type = Column(String)
    severity = Column(String)
    description = Column(String)
    status = Column(String)
    opened_at = Column(String, nullable=False)
    closed_at = Column(String)
    __table_args__ = (
        CheckConstraint("vehicle_id IS NOT NULL OR resource_id IS NOT NULL", name="chk_incident_assets"),
    )


class SimulationRun(Base):
    __tablename__ = "SIMULATION_RUN"
    run_id = Column(String, primary_key=True)
    started_by_user_id = Column(String, ForeignKey("USER.user_id"), nullable=False)
    scenario_name = Column(String)
    scenario_config = Column(Text)
    baseline_unmet_demand = Column(Integer)
    projected_unmet_demand = Column(Integer)
    simulation_outcome = Column(Text)
    status = Column(String)
    started_at = Column(String)


class CoordinationRecommendation(Base):
    __tablename__ = "COORDINATION_RECOMMENDATION"
    recommendation_id = Column(String, primary_key=True)
    simulation_run_id = Column(String, ForeignKey("SIMULATION_RUN.run_id"), nullable=False)
    source_hub_id = Column(String, ForeignKey("MOBILITY_HUB.hub_id"))
    destination_hub_id = Column(String, ForeignKey("MOBILITY_HUB.hub_id"))
    recommendation_type = Column(String)
    details = Column(Text)
    status = Column(String)


class RedistributionTask(Base):
    __tablename__ = "REDISTRIBUTION_TASK"
    task_id = Column(String, primary_key=True)
    recommendation_id = Column(String, ForeignKey("COORDINATION_RECOMMENDATION.recommendation_id"))
    vehicle_id = Column(String, ForeignKey("VEHICLE.vehicle_id"), nullable=False)
    from_hub_id = Column(String, ForeignKey("MOBILITY_HUB.hub_id"), nullable=False)
    to_hub_id = Column(String, ForeignKey("MOBILITY_HUB.hub_id"), nullable=False)
    created_by_user_id = Column(String, ForeignKey("USER.user_id"), nullable=False)
    priority = Column(Integer)
    status = Column(String)
