from contextlib import asynccontextmanager
from typing import AsyncGenerator, Any
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from api.config import Config
from api.schedulers.ride_scheduler import RideScheduler

@asynccontextmanager
async def init_schedulers() -> AsyncGenerator[None, Any]:
    scheduler = AsyncIOScheduler()
    scheduler.add_job(RideScheduler.run, "interval", minutes=Config.API.SCHEDULER_INTERVAL_IN_MINUTES)
    scheduler.start()

    try:
        yield
    finally:
        scheduler.shutdown()
