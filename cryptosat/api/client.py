from http import HTTPStatus
from typing import MutableMapping, Optional, Generic, T, Any

import requests


class Response(Generic[T]):
    status_code: HTTPStatus
    content: bytes
    headers: MutableMapping[str, str]
    parsed: Optional[T]


class Client:
    def __init__(self, base_url: str):
        if not base_url:
            base_url = "https://sandbox.api.cryptosat.io/v0"
        self.base_url = base_url

    def request(self, method, path, **kwargs):
        url = self.base_url + path
        return requests.request(method, url, **kwargs)
