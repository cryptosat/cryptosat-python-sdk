from .api.client import Client
from .api.sat_metrics import get_timestamp
from .ballot import Ballot
from .delay_enc_keypair import DelayEncKeypair
from .sign_message import SignMessage
from importlib.metadata import version

VERSION = version('cryptosat-python-sdk')


class CryptosatClient:

    def __init__(self, base_url: str):
        self.api_client = Client(base_url)

    def version(self):
        response = get_timestamp(self.api_client)
        return {
            "version": VERSION,
            "timestamp": response.timestamp
        }

    def create_keypair(self, delay):
        return DelayEncKeypair(self, delay)

    def create_sign_message(self, payload):
        return SignMessage(self, payload)

    def create_ballot(self, min_participants):
        return Ballot(self, min_participants)

    def get_next_online(self):
        path = "/next-online"
        return self.request("GET", path)

    def get_public_keys(self):
        path = "/public-keys"
        return self.request("GET", path)

    def get_public_random(self):
        path = "/public-random"
        return self.request("GET", path)

    def get_timestamp(self):
        path = "/timestamp"
        return self.request("GET", path)

    def get_randomness(self, num=None, type=None, format=None):
        path = "/randomness"
        params = {}
        if num is not None:
            params["num"] = num
        if type is not None:
            params["type"] = type
        if format is not None:
            params["format"] = format
        return self.request("GET", path, params=params)
