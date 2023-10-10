import base64
from typing import Optional

import rsa

from cryptosat.api.client import Client
from cryptosat.api.private_ballot import get_ballot, post_ballot_vote, VoteBody, post_ballot_finalize, get_ballot_result
from cryptosat.errors import ResourceNotFoundError, InvalidResourceStateError


def encrypt_message(pubkey_pem: str, msg: str) -> str:
    pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(pubkey_pem.encode())
    encrypted_msg = rsa.encrypt(msg.encode(), pubkey)
    return base64.encodebytes(encrypted_msg).decode()


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

        print(self.result)
        return self.result
