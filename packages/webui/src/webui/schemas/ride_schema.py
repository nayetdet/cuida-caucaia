from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from webui.enums.ride_type import RideType

class RideSchema(BaseModel):
    id: Optional[str] = None
    ride_type: Optional[RideType] = None
    price: Optional[float] = None
    timestamp: Optional[datetime] = None
