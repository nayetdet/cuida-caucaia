import requests
from typing import List, Dict, Any
from webui.config import Config
from webui.schemas.ride_schema import RideSchema

class RideService:
    @classmethod
    def get_all_rides(cls) -> List[RideSchema]:
        results: List[RideSchema] = []
        url: str = f"{Config.WebUI.API_URL}/v1/rides/"
        params: Dict[str, Any] = {
            "page": 0,
            "size": 25
        }

        while True:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data: Dict[str, Any] = response.json()
            content: List[Dict[str, Any]] = data.get("content", [])

            if content:
                for item in content:
                    result = RideSchema.model_validate(item)
                    results.append(result)

            total_elements: int = int(data.get("pageable", {}).get("total_elements", 0))
            if len(results) >= total_elements or not content:
                break

            params["page"] += 1

        return results
