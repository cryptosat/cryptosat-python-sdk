from typing import List

from pydantic import BaseModel

from .client import Client


class NextOnlineResponse(BaseModel):
    next_online_s: int


class PublicKeysResponse(BaseModel):
    public_keys: List[str]


class TimestampResponse(BaseModel):
    timestamp: float
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
    response.raise_for_status()
    return NextOnlineResponse.model_validate(response.json())


def get_public_keys(client: Client) -> PublicKeysResponse:
    response = client.request("GET", "/public-keys")
    response.raise_for_status()
    return PublicKeysResponse.model_validate(response.json())


def get_timestamp(client: Client) -> TimestampResponse:
    response = client.request("GET", "/timestamp")
    response.raise_for_status()
    return TimestampResponse.model_validate(response.json())


def get_public_random(client: Client) -> PublicRandomResponse:
    response = client.request("GET", "/public-random")
    response.raise_for_status()
    return PublicRandomResponse.model_validate(response.json())


def get_vrf_public(client: Client) -> VRFPublicResponse:
    response = client.request("GET", "/vrf-public")
    response.raise_for_status()
    return VRFPublicResponse.model_validate(response.json())
