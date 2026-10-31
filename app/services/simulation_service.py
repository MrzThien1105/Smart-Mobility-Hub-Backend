import json
from dataclasses import dataclass

from app.core.utils import utc_now_iso, uuid_id
from app.models.entities import SimulationRun
from app.schemas.operations import SimulationCreate


@dataclass(frozen=True)
class SimulationResult:
    baseline_unmet_demand: int
    projected_unmet_demand: int
    outcome: dict[str, object]


class DemandSimulationEngine:
    def run(self, scenario_config: dict) -> SimulationResult:
        baseline = max(0, int(scenario_config.get("baseline_demand", 100)))
        reduction_pct = max(0.0, min(100.0, float(scenario_config.get("demand_reduction_pct", 0))))
        projected = max(0, round(baseline * (100 - reduction_pct) / 100))
        return SimulationResult(
            baseline_unmet_demand=baseline,
            projected_unmet_demand=projected,
            outcome={
                "baseline_demand": baseline,
                "projected_unmet_demand": projected,
                "demand_reduction_pct": reduction_pct,
            },
        )


class SimulationService:
    def __init__(self, uow, engine: DemandSimulationEngine | None = None):
        self.uow = uow
        self.engine = engine or DemandSimulationEngine()

    def run(self, user_id: str, payload: SimulationCreate) -> SimulationRun:
        result = self.engine.run(payload.scenario_config)
        simulation = SimulationRun(
            run_id=uuid_id(),
            started_by_user_id=user_id,
            scenario_name=payload.scenario_name,
            scenario_config=json.dumps(payload.scenario_config),
            baseline_unmet_demand=result.baseline_unmet_demand,
            projected_unmet_demand=result.projected_unmet_demand,
            simulation_outcome=json.dumps(result.outcome),
            status="COMPLETED",
            started_at=utc_now_iso(),
        )
        return self.uow.runs.add(simulation)
