from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from api.enums.ride_type import RideType

class RideResponseSchema(BaseModel):
    id: Optional[str] = None
    ride_type: Optional[RideType] = None
    price: Optional[float] = None
    timestamp: Optional[datetime] = None
