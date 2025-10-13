from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional, Literal, Dict, Any
from pydantic import BaseModel

T = TypeVar("T")

class PageableSchema(BaseModel):
    page_number: int
    page_size: int
    total_elements: int

class PageSchema(BaseModel, Generic[T]):
    content: List[T]
    pageable: PageableSchema

class BaseQuerySchema(BaseModel, ABC):
    page: int = 0
    size: int = 10
    sort_by: Optional[str] = None
    sort_dir: Literal["asc", "desc"] = "asc"

    def get_skip(self) -> int:
        return self.page * self.size

    def get_order_by(self) -> str:
        direction: str = "" if self.sort_dir == "asc" else "desc"
        return f"{direction}{self.sort_by}"

    @abstractmethod
    def get_filters(self) -> Dict[str, Any]:
        pass
