from pydantic import ValidationError


class SDKError(Exception):
    """Base exception for all SDK related errors."""


class ResourceNotFoundError(SDKError):
    """Raised when the requested resource (e.g., ballot) is not found."""


class InvalidResourceStateError(SDKError):
    """Raised when an action is attempted on a resource in an inappropriate state."""


class APICommunicationError(SDKError):
    """Raised when there's a problem communicating with the Cryptosat API"""


class UnexpectedAPIResponseError(SDKError):
    """Raised when the API response is not as expected."""


def validate_model(model, data):
    try:
        return model.model_validate(data)
    except ValidationError as e:
        raise UnexpectedAPIResponseError(
            f"Failed to parse API response with error: {str(e)}"
        ) from e
