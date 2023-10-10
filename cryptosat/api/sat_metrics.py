from typing import List

from pydantic import BaseModel

from .client import Client
from ..errors import validate_model


class NextOnlineResponse(BaseModel):
    next_online_s: int


class PublicKeysResponse(BaseModel):
    public_keys: List[str]


class TimestampResponse(BaseModel):
    timestamp: int
    signature: str


class PublicRandomResponse(BaseModel):
    randomness: str
    signature: str


class VRFPublicResponse(BaseModel):
    round: int
    randomness: str
    signature: str


def get_next_online(client: Client) -> NextOnlineResponse:
    response = client.request("GET", "/next-online")
    return validate_model(NextOnlineResponse, response.json())


def get_public_keys(client: Client) -> PublicKeysResponse:
    response = client.request("GET", "/public-keys")
    return validate_model(PublicKeysResponse, response.json())


def get_timestamp(client: Client) -> TimestampResponse:
    response = client.request("GET", "/timestamp")
    return validate_model(TimestampResponse, response.json())


def get_public_random(client: Client) -> PublicRandomResponse:
    response = client.request("GET", "/public-random")
    return validate_model(PublicRandomResponse, response.json())


def get_vrf_public(client: Client) -> VRFPublicResponse:
    response = client.request("GET", "/vrf-public")
    return validate_model(VRFPublicResponse, response.json())
