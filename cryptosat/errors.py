class SDKError(Exception):
    """Base exception for all SDK related errors."""


class ResourceNotFoundError(SDKError):
    """Raised when the requested resource (e.g., ballot) is not found."""


class InvalidResourceStateError(SDKError):
    """Raised when an action is attempted on a resource in an inappropriate state."""
