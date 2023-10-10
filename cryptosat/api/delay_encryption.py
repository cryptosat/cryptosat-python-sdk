from http import HTTPStatus
from typing import Optional

from pydantic import BaseModel

from .client import Client
from ..errors import validate_model


class KeypairResponse(BaseModel):
    keypair_id: str


class PublicKeyResponse(BaseModel):
    public_key: str


class PrivateKeyResponse(BaseModel):
    private_key: str


def post_delay_enc_keypair(client: Client, delay: str) -> KeypairResponse:
    path = f"/delay-enc-keypair/{delay}"
    response = client.request("POST", path)
    return validate_model(KeypairResponse, response.json())


def get_delay_enc_keypair_public(client: Client, keypair_id: str) -> Optional[PublicKeyResponse]:
    path = f"/delay-enc-keypairs/{keypair_id}/public"
    response = client.request("GET", path)

    if response.status_code == HTTPStatus.OK:
        return validate_model(PublicKeyResponse, response.json())

    return None


def get_delay_enc_keypair_private(client: Client, keypair_id: str) -> Optional[PrivateKeyResponse]:
    path = f"/delay-enc-keypairs/{keypair_id}/private"
    response = client.request("GET", path)

    if response.status_code == HTTPStatus.OK:
        return validate_model(PrivateKeyResponse, response.json())

    return None
