from http import HTTPStatus
from typing import Optional

from pydantic import BaseModel

from .client import Client


class CreateBallotResponse(BaseModel):
    ballot_id: str


class GetBallotResponse(BaseModel):
    public_key: str


class VoteBody(BaseModel):
    encrypted_vote: str


class GetResultResponse(BaseModel):
    ballot_result: str


def post_ballot(client: Client, min_participants: int) -> CreateBallotResponse:
    if not isinstance(min_participants, int) or min_participants <= 0:
        raise ValueError("The provided minimum number of participants is not a positive integer.")

    path = f"/ballot/{min_participants}"
    response = client.request("POST", path)
    response.raise_for_status()
    return CreateBallotResponse.model_validate(response.json())


def get_ballot(client: Client, ballot_id: str) -> Optional[GetBallotResponse]:
    path = f"/ballots/{ballot_id}"
    response = client.request("GET", path)
    response.raise_for_status()

    if response.status_code == HTTPStatus.OK:
        return GetBallotResponse.model_validate(response.json())

    return None


def post_ballot_vote(client: Client, ballot_id: str, vote: VoteBody):
    path = f"/ballots/{ballot_id}/vote"
    response = client.request("POST", path, json=vote.model_dump())
    response.raise_for_status()
    return None


def post_ballot_finalize(client: Client, ballot_id: str):
    path = f"/ballots/{ballot_id}/finalize"
    response = client.request("POST", path)
    response.raise_for_status()
    return None


def get_ballot_result(client: Client, ballot_id: int) -> Optional[GetResultResponse]:
    path = f"/ballots/{ballot_id}/result"
    response = client.request("POST", path)
    response.raise_for_status()

    if response.status_code == HTTPStatus.OK:
        return GetResultResponse.model_validate(response.json())

    return None
