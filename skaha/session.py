"""Skaha Headless Session."""
from attr import attrs

from skaha.client import SkahaClient


@attrs
class Session(SkahaClient):
    """Skaha Headless Session.

    Args:
        SkahaClient ([type]): [description]

    """

    def __attrs_pre_init__(self, *args, **kwargs):
        """Pre init."""
        super().__init__(*args, **kwargs)

    def __attrs_post_init__(self):
        """Post init."""
        self.module = "Skaha Headless Session"
