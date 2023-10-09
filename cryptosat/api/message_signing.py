from http import HTTPStatus
from typing import Optional

from pydantic import BaseModel

from .client import Client


class SignMessageBody(BaseModel):
    message: str


class SignMessageResponse(BaseModel):
    request_uuid: str


class StatusResponse(BaseModel):
    signature: str
    message: str
    timestamp: int


def post_sign_message(client: Client, body: SignMessageBody) -> SignMessageResponse:
    response = client.request("POST", "/sign-message", json=body.model_dump())
    response.raise_for_status()
    return SignMessageResponse.model_validate(response.json())


def get_sign_message_status(client: Client, request_uuid: str) -> Optional[StatusResponse]:
    path = f"/sign-message/status/{request_uuid}"
    response = client.request("GET", path)
    response.raise_for_status()

    if response.status_code == HTTPStatus.OK:
        return StatusResponse.model_validate(response.json())

    return None
