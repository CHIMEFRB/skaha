"""Skaha Client."""
from os import environ
from pathlib import Path
from platform import machine, platform, python_version, release, system

from attr import attrib, attrs
from requests import Session
from validators import url, uuid

from skaha.exceptions import InvalidCertificateError, InvalidTokenError, ServerError


@attrs()
class Client(Session):
    """A client for the Skaha server."""

    server = attrib(default="https://ws-cadc.canfar.net")
    certificate = attrib(
        default="{HOME}/.ssl/cadcproxy.pem".format(HOME=environ["HOME"]), type=str
    )
    token = attrib(default="", type=str)

    @server.validator
    def _check_server(self, attribute, value):
        """Check if server is a valid url."""
        if not url(value):
            raise ServerError("Server must be a valid URL.")
        self.headers.update({"X-Skaha-Server": self.server})

    @certificate.validator
    def _check_certificate(self, attribute, value):
        """Check the certificate."""
        if not Path(value).is_file():
            raise InvalidCertificateError(f"{value} is not a valid certificate path.")
        self.headers.update({"X-Skaha-Authentication-Type": "certificate"})
        self.verify = self.certificate

    @token.validator
    def _check_token(self, attribute, value):
        """Check the token."""
        if value:
            if not uuid(value):
                raise InvalidTokenError(f"{value} is not a valid token")

    def __attrs_post_init__(self):
        """Post Intialization Attributes."""
        self.headers.update({"Content-Type": "application/json"})
        self.headers.update({"Accept": "application/json"})
        self.headers.update({"User-Agent": "skaha-client"})
        self.headers.update({"X-Skaha-Client-Version": python_version()})
        self.headers.update({"X-Skaha-Client-Release": "0.1"})
        self.headers.update({"X-Skaha-Client-Arch": machine()})
        self.headers.update({"X-Skaha-Client-OS": system()})
        self.headers.update({"X-Skaha-Client-OS-Version": release()})
        self.headers.update({"X-Skaha-Client-Platform": platform()})
