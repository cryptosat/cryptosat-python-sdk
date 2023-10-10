from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel

from .client import Client
from ..errors import validate_model


class GetRandomnessType(str, Enum):
    FLOAT = "float"
    UINT256 = "uint256"

    def __str__(self) -> str:
        return str(self.value)


class GetRandomnessFormat(str, Enum):
    DEC = "dec"
    HEX = "hex"

    def __str__(self) -> str:
        return str(self.value)


class RandomnessResponse(BaseModel):
    random_numbers: List[Union[float, str]]


def get_randomness(
    client: Client,
    num: Optional[int] = None,
    type_: Optional[GetRandomnessType] = GetRandomnessType.FLOAT,
    format_: Optional[GetRandomnessFormat] = GetRandomnessFormat.DEC,
) -> RandomnessResponse:
    params = {
        "num": num,
        "type": type_.value if type_ else None,
        "format": format_.value if format_ else None,
    }
    params = {k: v for k, v in params.items() if v is not None}

    response = client.request("GET", "/randomness", params=params)
    return validate_model(RandomnessResponse, response.json())
