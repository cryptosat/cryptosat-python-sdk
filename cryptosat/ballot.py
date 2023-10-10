import base64
from typing import Optional

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

from cryptosat.api.client import Client
from cryptosat.api.private_ballot import (
    get_ballot,
    post_ballot_vote,
    VoteBody,
    post_ballot_finalize,
    get_ballot_result,
)
from cryptosat.errors import ResourceNotFoundError, InvalidResourceStateError


def encrypt_message(pubkey_pem: str, msg: str) -> str:
    pubkey = serialization.load_pem_public_key(pubkey_pem.encode())
    ciphertext = pubkey.encrypt(
        msg.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(ciphertext).decode('utf-8')


class Ballot:
    def __init__(self, client: Client, ballot_id: str):
        self.client = client
        self.ballot_id = ballot_id
        self.public_key = None
        self.finalized = False
        self.result = None

    def try_fetch_public_key(self) -> Optional[str]:
        if self.public_key:
            return self.public_key

        response = get_ballot(self.client, self.ballot_id)
        if response:
            self.public_key = response.public_key

        return self.public_key

    def vote(self, vote: str) -> None:
        public_key = self.try_fetch_public_key()
        if not public_key:
            raise ResourceNotFoundError(f"Ballot with ID {self.ballot_id} not ready")

        encrypted_vote = encrypt_message(self.public_key, vote)
        vote_body = VoteBody(encrypted_vote=encrypted_vote)

        post_ballot_vote(self.client, self.ballot_id, vote_body)

    def finalize(self) -> None:
        public_key = self.try_fetch_public_key()
        if not public_key:
            raise ResourceNotFoundError(f"Ballot with ID {self.ballot_id} not ready")

        if self.finalized:
            raise InvalidResourceStateError(f"The ballot with ID {self.ballot_id} is finalized")

        post_ballot_finalize(self.client, self.ballot_id)
        self.finalized = True

    def try_fetch_result(self) -> Optional[str]:
        if not self.finalized:
            raise InvalidResourceStateError(f"The resource has not been finalized yet")

        if self.result:
            return self.result

        response = get_ballot_result(self.client, self.ballot_id)
        if response:
            self.result = response.ballot_result

        return self.result
