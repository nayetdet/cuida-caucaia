from datetime import datetime
from typing import Optional, Dict, Any
from api.enums.ride_type import RideType
from api.schemas.queries.base_query_schema import BaseQuerySchema

class RideQuerySchema(BaseQuerySchema):
    ride_type: Optional[RideType] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    from_timestamp: Optional[datetime] = None
    to_timestamp: Optional[datetime] = None

    def get_filters(self) -> Dict[str, Any]:
        filters: Dict[str, Any] = {}

        # ride_type
        if self.ride_type is not None:
            filters["ride_type"] = self.ride_type

        # price
        if self.min_price is not None or self.max_price is not None:
            price_filter: Dict[str, Any] = {}
            if self.min_price is not None:
                price_filter["$gte"] = self.min_price
            if self.max_price is not None:
                price_filter["$lte"] = self.max_price
            filters["price"] = price_filter

        # timestamp
        if self.from_timestamp is not None or self.to_timestamp is not None:
            ts_filter: Dict[str, Any] = {}
            if self.from_timestamp is not None:
                ts_filter["$gte"] = self.from_timestamp
            if self.to_timestamp is not None:
                ts_filter["$lte"] = self.to_timestamp
            filters["timestamp"] = ts_filter

        return filters
