"""Test Skaha Images API."""

import pytest

from skaha.exceptions import InvalidCertificateError, InvalidServerURL
from skaha.images import Images


@pytest.fixture(scope="session")
def images():
    """Test images."""
    images = Images()
    yield images
    del images


def test_bad_server():
    """Test bad server."""
    with pytest.raises(InvalidServerURL):
        Images(server="abcdefd")


def test_bad_certificate():
    """Test bad certificate."""
    with pytest.raises(InvalidCertificateError):
        Images(certificate="abcdefd")


def test_images_fetch(images):
    """Test fetching images."""
    assert images.fetch()


def test_images_with_kind(images):
    """Test fetching images with kind."""
    assert images.fetch(kind="headless")
