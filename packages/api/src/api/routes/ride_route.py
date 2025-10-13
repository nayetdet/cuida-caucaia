from fastapi import APIRouter, Depends
from starlette import status
from api.schemas.queries.base_query_schema import PageSchema
from api.schemas.queries.ride_query_schema import RideQuerySchema
from api.schemas.responses.ride_response_schema import RideResponseSchema
from api.services.ride_service import RideService

router = APIRouter()

@router.get("/", response_model=PageSchema[RideResponseSchema])
async def search(query: RideQuerySchema = Depends()):
    return await RideService.search(query)

@router.get("/{ride_id}", response_model=RideResponseSchema)
async def get_by_id(ride_id: str):
    return await RideService.get_by_id(ride_id)

@router.post("/", status_code=status.HTTP_204_NO_CONTENT)
async def create():
    await RideService.create()
