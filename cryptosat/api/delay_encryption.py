from http import HTTPStatus
from typing import Optional

from pydantic import BaseModel

from .client import Client


class KeypairResponse(BaseModel):
    keypair_id: str


class PublicKeyResponse(BaseModel):
    public_key: str


def post_delay_enc_keypair(client: Client, delay: str) -> KeypairResponse:
    path = f"/delay-enc-keypair/{delay}"
    response = client.request("POST", path)
    response.raise_for_status()
    return KeypairResponse.model_validate(response.json())


def get_delay_enc_keypair_public(client: Client, keypair_id: str) -> Optional[PublicKeyResponse]:
    path = f"/delay-enc-keypairs/{keypair_id}/public"
    response = client.request("POST", path)
    response.raise_for_status()

    if response.status_code == HTTPStatus.OK:
        return PublicKeyResponse.model_validate(response.json())

    return None
