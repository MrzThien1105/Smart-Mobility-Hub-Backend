from fastapi import APIRouter, Depends, Query
from app.database import get_uow
from app.schemas.mobility import HubOut, VehicleOut

router = APIRouter()


@router.get("/hubs", response_model=list[HubOut])
def list_hubs(
    uow = Depends(get_uow),
    offset: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
):
    items, _ = uow.hubs.list(offset=offset, limit=limit)
    return items


@router.get("/vehicles", response_model=list[VehicleOut])
def list_vehicles(
    uow = Depends(get_uow),
    offset: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
):
    items, _ = uow.vehicles.list(offset=offset, limit=limit)
    return items
