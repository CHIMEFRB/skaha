"""Test Skaha Client API."""

import pytest

from skaha.client import SkahaClient
from skaha.exceptions import InvalidCertificateError, InvalidServerURL


def test_bad_server():
    """Test bad server."""
    with pytest.raises(InvalidServerURL):
        SkahaClient(server="abcdefd")


def test_bad_certificate():
    """Test bad certificate."""
    with pytest.raises(InvalidCertificateError):
        SkahaClient(certificate="abcdefd")


def test_bad_certificate_path():
    """Test bad certificate."""
    with pytest.raises(InvalidCertificateError):
        SkahaClient(certificate="/tmp/abcdefd")


def test_client_headers():
    """Test client headers."""
    assert SkahaClient().headers["Content-Type"] == "application/json"
