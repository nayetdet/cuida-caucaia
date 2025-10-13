import re
import asyncio
from datetime import datetime
from pathlib import Path
from typing import List, Optional
from aioconsole import ainput
from camoufox import AsyncCamoufox
from playwright.async_api import Page, Locator
from api.enums.ride_type import RideType
from api.models.ride import Ride

class RideUtils:
    __PRICE_REGEX: re.Pattern[str] = re.compile(r"R\$\s*\d+(?:\.\d{2})?")

    def __init__(self, ride_url: str, config_path: Path):
        self.__ride_url: str = ride_url
        self.__config_path: Path = config_path

    async def login(self) -> None:
        async with AsyncCamoufox(user_data_dir=self.__config_path, persistent_context=True, headless=False) as browser:
            page: Page = browser.pages[0] if browser.pages else await browser.new_page()
            await page.goto("https://auth.uber.com/v2")
            await ainput()

    async def estimate_rides(self) -> List[Ride]:
        async with AsyncCamoufox(user_data_dir=self.__config_path, persistent_context=True, headless=True, humanize=1) as browser:
            page: Page = browser.pages[0] if browser.pages else await browser.new_page()
            await page.goto(self.__ride_url, wait_until="load")

            ride_elements: Locator = page.locator("li[data-testid='product_selector.list_item']")
            await ride_elements.first.wait_for(state="visible", timeout=10000)

            rides: List[Ride] = []
            timestamp: datetime = datetime.now()
            for ride_element in await ride_elements.all():
                inner_text: str = await ride_element.inner_text()
                ride_type: Optional[RideType] = self.__extract_ride_type(inner_text)
                price: Optional[float] = self.__extract_price(inner_text)
                if ride_type is None or price is None:
                    continue

                rides.append(Ride(ride_type=ride_type, price=price, timestamp=timestamp))
                await asyncio.sleep(1)

            return rides

    @classmethod
    def __extract_ride_type(cls, text: str) -> Optional[RideType]:
        text_upper: str = text.upper()
        for ride_type in RideType:
            if ride_type.value in text_upper:
                return ride_type
        return None

    @classmethod
    def __extract_price(cls, text: str) -> Optional[float]:
        price_match: Optional[re.Match[str]] = cls.__PRICE_REGEX.search(text)
        if price_match is None:
            return None

        try:
            return float(price_match.group().replace("R$", "").strip())
        except ValueError:
            return None
