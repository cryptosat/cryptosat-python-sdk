from http import HTTPStatus
from typing import Optional

from pydantic import BaseModel

from .client import Client
from ..errors import validate_model


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
    return validate_model(SignMessageResponse, response.json())


def get_sign_message_status(client: Client, request_uuid: str) -> Optional[StatusResponse]:
    path = f"/sign-message/status/{request_uuid}"
    response = client.request("GET", path)

    if response.status_code == HTTPStatus.OK:
        return validate_model(StatusResponse, response.json())

    return None
