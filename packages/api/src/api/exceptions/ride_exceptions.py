from typing import ClassVar
from starlette import status
from api.exceptions import BaseApplicationException

class RideNotFoundException(BaseApplicationException):
    STATUS_CODE: ClassVar[int] = status.HTTP_404_NOT_FOUND
    MESSAGE: ClassVar[str] = "A corrida solicitada não foi encontrada."

class RideEstimateException(BaseApplicationException):
    STATUS_CODE: ClassVar[int] = status.HTTP_400_BAD_REQUEST
    MESSAGE: ClassVar[str] = "Não foi possível estimar o preço da corrida."
