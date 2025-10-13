import asyncio
from api.deps.utils_instance import UtilsInstance

async def main() -> None:
    await UtilsInstance.get_ride_utils().login()

if __name__ == "__main__":
    asyncio.run(main())
