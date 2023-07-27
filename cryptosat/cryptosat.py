import requests

class Client:
    def __init__(self, base_url):
        self.base_url = base_url

    def request(self, method, path, **kwargs):
        url = self.base_url + path
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Parse JSON response

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

class DelayEncKeypair:
    def __init__(self, client, delay):
        self.client = client
        self.keypair_id = self.create(delay)

    def create(self, delay):
        # TODO: Add input validation
        path = f"/delay-enc-keypair/{delay}"
        response = self.client.request("POST", path)
        return response["keypair_id"]  # Store keypair_id

    def get_private(self):
        path = f"/delay-enc-keypairs/{self.keypair_id}/private"
        return self.client.request("GET", path)

    def get_public(self):
        path = f"/delay-enc-keypairs/{self.keypair_id}/public"
        return self.client.request("GET", path)

class SignMessage:
    def __init__(self, client, payload):
        self.client = client
        self.request_uuid = self.create(payload)

    def create(self, payload):
        # TODO: Add input validation
        path = "/sign-message"
        response = self.client.request("POST", path, json=payload)
        return response["request_uuid"]  # Store request_uuid

    def get_status(self):
        path = f"/sign-message/status/{self.request_uuid}"
        return self.client.request("GET", path)

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



