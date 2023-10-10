from typing import Optional

from cryptosat.api.client import Client
from cryptosat.api.message_signing import get_sign_message_status, StatusResponse


class SignMessageRequest:
    def __init__(self, client: Client, request_uuid: str):
        self.result = None
        self.client = client
        self.request_uuid = request_uuid

    def try_fetch_result(self) -> Optional[StatusResponse]:
        if self.result:
            return self.result

        response = get_sign_message_status(self.client, self.request_uuid)
        self.result = response

        return self.result
