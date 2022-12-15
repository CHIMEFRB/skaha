"""Test Skaha Session API."""

from time import sleep
from typing import List
from uuid import uuid4

import pytest
from pydantic import ValidationError

from skaha.session import Session


@pytest.fixture(scope="module")
def name():
    """Return a random name."""
    yield str(uuid4().hex[:7])


@pytest.fixture(scope="session")
def session():
    """Test images."""
    session = Session()
    yield session
    del session


def test_fetch_with_kind(session: Session):
    """Test fetching images with kind."""
    session.fetch(kind="headless")


def test_fetch_malformed_kind(session: Session):
    """Test fetching images with malformed kind."""
    with pytest.raises(ValidationError):
        session.fetch(kind="invalid")


def test_fetch_with_malformed_view(session: Session):
    """Test fetching images with malformed view."""
    with pytest.raises(ValidationError):
        session.fetch(view="invalid")


def test_fetch_with_malformed_status(session: Session):
    """Test fetching images with malformed status."""
    with pytest.raises(ValidationError):
        session.fetch(status="invalid")


def test_session_stats(session: Session):
    """Test fetching images with kind."""
    assert "instances" in session.stats().keys()


def test_create_session_with_malformed_kind(session: Session, name: str):
    """Test creating a session with malformed kind."""
    with pytest.raises(ValidationError):
        session.create(
            name=name,
            kind="invalid",
            image="ubuntu:latest",
            cmd="bash",
            replicas=1,
        )


def test_create_session_cmd_without_headless(session: Session, name: str):
    """Test creating a session without headless."""
    with pytest.raises(ValidationError):
        session.create(
            name=name,
            kind="vnc",
            image="ubuntu:latest",
            cmd="bash",
            replicas=1,
        )


def test_create_session(session: Session, name: str):
    """Test creating a session."""
    identity: List[str] = session.create(
        name=name,
        kind="headless",
        cores=1,
        ram=1,
        image="images.canfar.net/chimefrb/testing:keep",
        cmd="env",
        replicas=1,
        env={"TEST": "test"},
    )
    assert len(identity) == 1
    assert identity[0] != ""

    # Get session info
    info = session.info(identity)
    assert info[0]["name"] == name

    # Sleep for 5 seconds
    sleep(5)

    # Get logs for the session
    logs = session.logs(identity)
    assert len(logs) == 1
    assert logs[identity[0]] != ""

    # Delete the session
    deletion = session.destroy(identity)
    assert deletion == {name: True}
