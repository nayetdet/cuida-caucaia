from typing import Optional
from api.config import Config
from api.utils.ride_utils import RideUtils

class UtilsInstance:
    __ride_utils: Optional[RideUtils] = None

    @classmethod
    def get_ride_utils(cls) -> RideUtils:
        if cls.__ride_utils is None:
            cls.__ride_utils = RideUtils(
                ride_url=Config.API.UBER_RIDE_URL,
                config_path=Config.Paths.CONFIG
            )
        return cls.__ride_utils
