
class Ballot:
    def __init__(self, client, min_participants):
        self.client = client
        self.ballot_id = self.create(min_participants)

    def create(self, min_participants):
        # TODO: Add input validation
        path = f"/ballot/{min_participants}"
        response = self.client.request("POST", path)
        return response["ballot_id"]  # Store ballot_id

    def finalize(self):
        path = f"/ballots/{self.ballot_id}/finalize"
        return self.client.request("POST", path)

    def get(self):
        path = f"/ballots/{self.ballot_id}"
        return self.client.request("GET", path)

    def get_result(self):
        path = f"/ballots/{self.ballot_id}/result"
        return self.client.request("GET", path)

    def vote(self, vote_payload):
        # TODO: Add input validation
        path = f"/ballots/{self.ballot_id}/vote"
        return self.client.request("POST", path, json=vote_payload)
