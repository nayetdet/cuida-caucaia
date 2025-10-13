from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from api.config import Config
from api.models.ride import Ride

async def init_mongodb() -> None:
    mongo_uri: str = f"mongodb://{Config.MongoDB.USERNAME}:{Config.MongoDB.PASSWORD}@{Config.MongoDB.HOST}/{Config.MongoDB.DATABASE}?authSource=admin"
    client = AsyncIOMotorClient(mongo_uri)
    await init_beanie(database=client[Config.MongoDB.DATABASE], document_models=[Ride])
