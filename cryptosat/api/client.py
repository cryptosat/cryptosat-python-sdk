import requests

from cryptosat.errors import APICommunicationError


class Client:
    def __init__(self, base_url: str):
        if not base_url:
            base_url = "https://sandbox.api.cryptosat.io/v0"
        self.base_url = base_url

    def request(self, method, path, **kwargs):
        url = self.base_url + path
        response = requests.request(method, url, **kwargs)

        try:
            response.raise_for_status()
        except requests.RequestException as e:
            raise APICommunicationError(f"API request failed with error: {str(e)}") from e

        return response
