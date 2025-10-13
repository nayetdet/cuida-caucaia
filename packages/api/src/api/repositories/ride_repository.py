from typing import Optional, List
from api.models.ride import Ride
from api.schemas.queries.ride_query_schema import RideQuerySchema

class RideRepository:
    @classmethod
    async def search(cls, query: RideQuerySchema) -> List[Ride]:
        return await Ride.find(query.get_filters()).sort(query.get_order_by()).skip(query.get_skip()).limit(query.size).to_list()

    @classmethod
    async def get_by_id(cls, ride_id: str) -> Optional[Ride]:
        return await Ride.get(ride_id)

    @classmethod
    async def create_many(cls, rides: List[Ride]) -> List[Ride]:
        await Ride.insert_many(rides)
        return rides

    @classmethod
    async def count(cls) -> int:
        return await Ride.count()
