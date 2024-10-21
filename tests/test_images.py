"""Test Skaha Images API."""

import pytest

from skaha.images import Images


@pytest.fixture(scope="session")
def images():
    """Test images."""
    images = Images()
    yield images
    del images


def test_images_fetch(images: Images):
    """Test fetching images."""
    assert len(images.fetch()) > 0


def test_images_with_kind(images: Images):
    """Test fetching images with kind."""
    assert "images.canfar.net/skaha/base-notebook:latest" in images.fetch(
        kind="notebook"
    )
