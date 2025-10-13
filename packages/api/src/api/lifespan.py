from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator
from fastapi import FastAPI
from api.database import init_mongodb
from api.schedulers import init_schedulers

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:
    await init_mongodb()
    async with init_schedulers():
        yield
