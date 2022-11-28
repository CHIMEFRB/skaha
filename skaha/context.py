"""Get available resources from the skaha server."""

from pydantic import root_validator
from skaha.client import SkahaClient


class Context(SkahaClient):
    """Get available resources from the skaha server."""

    @root_validator
    def set_server(cls, values):
        """Sets the server path after validation"""
        values["server"] = values["server"] + "/context"
        return values

    def resources(self) -> dict:
        """Get available resources from the skaha server.

        Returns:
            A dictionary of available resources.

        Examples:
            >>> from skaha.context import Context
                context = Context()
                context.resources()
            >>> {'defaultCores': 2,
                 'defaultCoresHeadless': 1,
                 ...}

        """
        return self.session.get(url=self.server).json()
