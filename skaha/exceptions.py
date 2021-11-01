"""Skaha Exceptions."""


class APIError(Exception):
    """Errors raised as a result of HTTP Status Codes."""

    pass


# Authentication Errors
class AuthenticationError(APIError):
    """Authentication Error."""

    pass


class InvalidCertificateError(AuthenticationError):
    """Invalid Certificate Error."""

    pass


class InvalidTokenError(AuthenticationError):
    """Invalid Token Error."""

    pass


class InvalidServerURL(APIError):
    """Invalid Server URL."""

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


class ClientError(Exception):
    """Internal Client Error."""

    pass


class ParameterError(ClientError):
    """Invalid Parameters."""

    pass


class UnknownError(ClientError):
    """Unknown Error."""

    pass
