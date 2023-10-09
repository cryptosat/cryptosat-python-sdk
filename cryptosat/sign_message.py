class SignMessage:
    def __init__(self, client, payload):
        self.client = client
        self.request_uuid = self.create(payload)

    def create(self, message):
        # TODO: Add input validation
        payload = {"message": message}
        path = "/sign-message"
        # return payload
        response = self.client.request("POST", path, json=payload)
        return response["request_uuid"]  # Store request_uuid

    def get_status(self):
        path = f"/sign-message/status/{self.request_uuid}"
        return self.client.request("GET", path)
