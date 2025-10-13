from api.models.ride import Ride
from api.schemas.responses.ride_response_schema import RideResponseSchema

class RideMapper:
    @classmethod
    def to_response_schema(cls, ride: Ride) -> RideResponseSchema:
        return RideResponseSchema(
            id=str(ride.id),
            ride_type=ride.ride_type,
            price=ride.price,
            timestamp=ride.timestamp
        )
