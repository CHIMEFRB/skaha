"""Skaha Exceptions."""


class APIError(Exception):
    """API Error."""

    pass


class ClientError(Exception):
    """Client Error."""

    pass


# Authentication Errors
class AuthenticationError(APIError):
    """Authentication Error."""

    pass


class InvalidCredentialsError(AuthenticationError):
    """Invalid Credentials Error."""

    pass


class InvalidTokenError(AuthenticationError):
    """Invalid Token Error."""

    pass


class InvalidUserError(AuthenticationError):
    """Invalid User Error."""

    pass


class InvalidPasswordError(AuthenticationError):
    """Invalid Password Error."""

    pass


# Connection Errors
class ConnectionError(APIError):
    """Connection Error."""

    pass


class InvalidRequestError(APIError):
    """Invalid Request Error."""

    pass


class InvalidResponseError(APIError):
    """Invalid Response Error."""

    pass


class RateLimitError(APIError):
    """Rate Limit Error."""

    pass


class ServiceUnavailableError(APIError):
    """Service Unavailable Error."""

    pass


# Client Errors
class ServerError(ClientError):
    """Server Error."""

    pass


class UnknownError(ClientError):
    """Unknown Error."""

    pass
