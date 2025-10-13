from fastapi import FastAPI, APIRouter
from api.routes import ride_route

def register_routes(app: FastAPI) -> None:
    router = APIRouter(prefix="/v1")
    router.include_router(ride_route.router, prefix="/rides", tags=["Ride"])
    app.include_router(router)
