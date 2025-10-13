from api.exceptions.ride_exceptions import RideEstimateException
from api.services.ride_service import RideService

class RideScheduler:
    @classmethod
    async def run(cls) -> None:
        try: await RideService.create()
        except RideEstimateException:
            return
