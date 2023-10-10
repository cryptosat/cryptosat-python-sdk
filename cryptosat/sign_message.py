from cryptosat.api.client import Client
from cryptosat.api.message_signing import get_sign_message_status
from cryptosat.request import RequestStatus


class SignMessageRequest:
    def __init__(self, client: Client, request_uuid: str):
        self.result = None
        self.client = client
        self.request_uuid = request_uuid

    def get_status(self) -> RequestStatus:
        if self.result:
            return RequestStatus.READY

        response = get_sign_message_status(self.client, self.request_uuid)

        if response:
            self.result = response
            return RequestStatus.READY

        return RequestStatus.SENT
