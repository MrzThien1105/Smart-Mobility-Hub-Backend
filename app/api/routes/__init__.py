from fastapi import APIRouter

from app.api.routes import charging, fleet, mobility, operations, parking, rental

api_router = APIRouter()
api_router.include_router(mobility.router, prefix="/mobility", tags=["mobility"])
api_router.include_router(rental.router, prefix="/rentals", tags=["rentals"])
api_router.include_router(parking.router, prefix="/parking", tags=["parking"])
api_router.include_router(charging.router, prefix="/charging", tags=["charging"])
api_router.include_router(fleet.router, prefix="/fleet", tags=["fleet"])
api_router.include_router(operations.router, tags=["operations"])
