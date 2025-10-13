from os import getenv
from pathlib import Path
from typing import List

class Config:
    class API:
        UBER_RIDE_URL: str = getenv("API_UBER_RIDE_URL")
        SCHEDULER_INTERVAL_IN_MINUTES: int = int(getenv("API_SCHEDULER_INTERVAL_IN_MINUTES"))
        CORS_ORIGINS: List[str] = [x.strip() for x in (getenv("API_CORS_ORIGINS") or "").split(",") if x.strip()]

    class MongoDB:
        DATABASE: str = getenv("MONGODB_DATABASE")
        HOST: str = getenv("MONGODB_HOST")
        USERNAME: str = getenv("MONGODB_USERNAME")
        PASSWORD: str = getenv("MONGODB_PASSWORD")

    class Paths:
        ROOT: Path = Path(__file__).resolve().parents[5]
        CONFIG: Path = ROOT / "config"
