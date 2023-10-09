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
