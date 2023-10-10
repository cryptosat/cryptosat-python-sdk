from enum import Enum


class RequestStatus(str, Enum):
    SENT = "SENT"
    READY = "READY"

    def __str__(self) -> str:
        return str(self.value)
