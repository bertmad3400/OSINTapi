from pydantic import BaseModel
from typing import List, Dict, Union, Optional

from enum import Enum


class DefaultResponseStatus(str, Enum):
    SUCCESS = "success"
    FAILURE = "failure"


class DefaultResponse(BaseModel):
    status: DefaultResponseStatus
    msg: str = ""

    class Config:
        use_enum_values = True


class HTTPError(BaseModel):
    detail: str
    headers: Dict[str, str]

    class Config:
        schema_extra = {
            "example": {"detail": "HTTPException raised."},
        }
