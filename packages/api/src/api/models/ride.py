from beanie import Document
from datetime import datetime
from pydantic import Field
from api.enums.ride_type import RideType

class Ride(Document):
    ride_type: RideType = Field(...)
    price: float = Field(...)
    timestamp: datetime = Field(...)

    class Settings:
        name: str = "rides"
