import re
from abc import ABC
from datetime import datetime, timezone
from typing import ClassVar
from bson.errors import InvalidId
from fastapi import status
from fastapi.responses import JSONResponse
from pymongo.errors import DuplicateKeyError

class BaseApplicationException(ABC, Exception):
    STATUS_CODE: ClassVar[int]
    MESSAGE: ClassVar[str]
    INNER_EXCEPTION: ClassVar[type[Exception]]

    @classmethod
    def get_response(cls) -> JSONResponse:
        return JSONResponse(
            status_code=cls.STATUS_CODE,
            content={
                "status": cls.STATUS_CODE,
                "code": re.sub(r"([a-z])([A-Z])", r"\1_\2", cls.__name__).upper(),
                "message": cls.MESSAGE,
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        )

class InvalidIdException(BaseApplicationException):
    STATUS_CODE: ClassVar[int] = status.HTTP_400_BAD_REQUEST
    MESSAGE: ClassVar[str] = "ID inválido: deve ter 24 caracteres hexadecimais ou 12 bytes."
    INNER_EXCEPTION: ClassVar[type[Exception]] = InvalidId

class NotUniqueException(BaseApplicationException):
    STATUS_CODE: ClassVar[int] = status.HTTP_409_CONFLICT
    MESSAGE: ClassVar[str] = "O recurso já existe e não pode ser duplicado."
    INNER_EXCEPTION: ClassVar[type[Exception]] = DuplicateKeyError

class InternalServerErrorException(BaseApplicationException):
    STATUS_CODE: ClassVar[int] = status.HTTP_500_INTERNAL_SERVER_ERROR
    MESSAGE: ClassVar[str] = "Ocorreu um erro interno no servidor."
    INNER_EXCEPTION: ClassVar[type[Exception]] = Exception
