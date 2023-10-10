from typing import Optional

from cryptosat.api.client import Client
from cryptosat.api.delay_encryption import (
    get_delay_enc_keypair_public,
    get_delay_enc_keypair_private,
)
from cryptosat.errors import ResourceNotFoundError


class DelayEncKeypair:
    def __init__(self, client: Client, keypair_id: str):
        self.client = client
        self.keypair_id = keypair_id
        self.private_key = None
        self.public_key = None

    def try_fetch_public_key(self) -> Optional[str]:
        if self.public_key:
            return self.public_key

        response = get_delay_enc_keypair_public(self.client, self.keypair_id)
        if response:
            self.public_key = response.public_key

        return self.public_key

    def try_fetch_private_key(self) -> Optional[str]:
        public_key = self.try_fetch_public_key()
        if not public_key:
            raise ResourceNotFoundError(
                f"The keypair with ID: {self.keypair_id} has not been created yet"
            )

        response = get_delay_enc_keypair_private(self.client, self.keypair_id)
        if response:
            self.private_key = response.private_key

        return self.private_key
