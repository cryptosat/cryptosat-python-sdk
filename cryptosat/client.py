from typing import Optional

from pydantic import BaseModel

from .api.client import Client
from .api.delay_encryption import post_delay_enc_keypair
from .api.message_signing import post_sign_message, SignMessageBody
from .api.private_ballot import post_ballot
from .api.random_beacon import (
    get_randomness,
    GetRandomnessType,
    GetRandomnessFormat,
    RandomnessResponse,
)
from .api.sat_metrics import (
    get_timestamp,
    get_public_keys,
    PublicKeysResponse,
    TimestampResponse,
    get_public_random,
    PublicRandomResponse,
    get_next_online,
)
from .ballot import Ballot
from .delay_enc_keypair import DelayEncKeypair
from .sign_message import SignMessageRequest
from importlib.metadata import version

VERSION = version("cryptosat-python-sdk")


class VersionResponse(BaseModel):
    version: str = VERSION
    timestamp: int


class StatusResponse(BaseModel):
    status: str = "ok"
    timestamp: int


class CryptosatClient:
    def __init__(self, base_url: str):
        self.api_client = Client(base_url)

    def version(self) -> VersionResponse:
        response = get_timestamp(self.api_client)
        return VersionResponse(timestamp=response.timestamp)

    def status(self) -> StatusResponse:
        response = get_timestamp(self.api_client)
        return StatusResponse(timestamp=response.timestamp)

    def get_public_signing_key(self) -> str:
        response = get_public_keys(self.api_client)
        return response.public_keys[0]

    def get_public_keys(self) -> PublicKeysResponse:
        return get_public_keys(self.api_client)

    def get_timestamp(self) -> TimestampResponse:
        return get_timestamp(self.api_client)

    def get_public_random(self) -> PublicRandomResponse:
        return get_public_random(self.api_client)

    def get_next_online(self) -> int:
        response = get_next_online(self.api_client)
        return response.next_online_s

    def get_randomness(
            self,
            num: Optional[int] = None,
            rtype: Optional[GetRandomnessType] = GetRandomnessType.FLOAT,
            rformat: Optional[GetRandomnessFormat] = GetRandomnessFormat.DEC,
    ) -> RandomnessResponse:
        return get_randomness(self.api_client, num, rtype, rformat)

    def sign_message(self, message: str) -> SignMessageRequest:
        response = post_sign_message(self.api_client, body=SignMessageBody(message=message))
        return SignMessageRequest(self.api_client, response.request_uuid)

    def create_ballot(self, min_participants: int) -> Ballot:
        response = post_ballot(self.api_client, min_participants)
        return Ballot(self.api_client, response.ballot_id)

    def create_keypair(self, delay: str) -> DelayEncKeypair:
        response = post_delay_enc_keypair(self.api_client, delay)
        return DelayEncKeypair(self.api_client, response.keypair_id)
