from typing import Optional, List
from api.deps.utils_instance import UtilsInstance
from api.exceptions.ride_exceptions import RideNotFoundException, RideEstimateException
from api.mappers.ride_mapper import RideMapper
from api.models.ride import Ride
from api.repositories.ride_repository import RideRepository
from api.schemas.queries.base_query_schema import PageSchema, PageableSchema
from api.schemas.queries.ride_query_schema import RideQuerySchema
from api.schemas.responses.ride_response_schema import RideResponseSchema

class RideService:
    @classmethod
    async def search(cls, query: RideQuerySchema) -> PageSchema[RideResponseSchema]:
        content: List[Ride] = await RideRepository.search(query)
        total_elements: int = await RideRepository.count()
        return PageSchema[RideResponseSchema](
            content=[RideMapper.to_response_schema(x) for x in content],
            pageable=PageableSchema(
                page_number=query.page,
                page_size=query.size,
                total_elements=total_elements
            )
        )

    @classmethod
    async def get_by_id(cls, ride_id: str) -> RideResponseSchema:
        ride: Optional[Ride] = await RideRepository.get_by_id(ride_id)
        if ride is None:
            raise RideNotFoundException()
        return RideMapper.to_response_schema(ride)

    @classmethod
    async def create(cls) -> None:
        try:
            rides: List[Ride] = await UtilsInstance.get_ride_utils().estimate_rides()
            await RideRepository.create_many(rides)
        except Exception as e:
            raise RideEstimateException() from e
