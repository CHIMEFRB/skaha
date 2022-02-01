"""Skaha Headless Sessions."""
from attr import attrs
from typing import List
from beartype import beartype

from skaha.threaded import scale
from asyncio import get_event_loop

from skaha.client import SkahaClient
from skaha.typedef import (
    ARGS,
    CMDS,
    CORES,
    ENVS,
    IDS,
    IMAGES,
    KIND,
    KINDS,
    NAMES,
    RAMS,
    STATUS,
    STATUSES,
    VIEW,
    VIEWS,
)
from skaha.utils import logs

log = logs.get_logger(__name__)


@attrs
class Sessions(SkahaClient):
    """Skaha Client for multiple sessions."""

    def __attrs_post_init__(self):
        """Modify the attributes of the SkahaClient class."""
        self.server = self.server + "/session"

    @beartype
    def fetch(
        self,
        kind: KIND = None,
        status: STATUS = None,
        view: VIEW = None,
    ) -> List:
        """List open sessions for the user.

        Args:
            kind (str, optional): Session kind. Defaults to None.
            status (str, optional): Session status. Defaults to None.
            view (str, optional): Session view level. Defaults to None.

        Raises:
            ParameterError: When `kind`, `status` or `view` are malformed.

        Returns:
            list: Sessions information.

        Examples:
            >>> from skaha.session import Session
                session = Session()
                session.fetch(kind="desktop")

        """
        params: dict = {}
        if kind:
            params["type"] = kind
        if status:
            params["status"] = status
        if view:
            params["view"] = view
        log.debug(params)
        response = self.get(url=self.server, params=params)
        response.raise_for_status()
        return response.json()

    def info(self, ids: IDS) -> List[str]:
        """Get information about sessions.

        Args:
            ids (List[str]): Session IDs.

        Returns:
            List[str]: Session information.

        Examples:
            >>> session.info(ids=["hjko98yghj", "hkko98yghj"])

        """
        arguments: list = []
        for id in ids:
            arguments.append(
                {"url": self.server + "/" + id, "params": {"view": "event"}}
            )

        loop = get_event_loop()
        responses = loop.run_until_complete(scale(self.get, arguments))
        return [response.text for response in responses]

    def logs(self, ids: IDS) -> dict[str, str]:
        """Get logs from sessions.

        Args:
            id (List[str]): Session IDs.

        Returns:
            Dict[str, str]: Logs in text/plain format.

        Examples:
            >>> session.logs(id=["hjko98yghj", "hkko98yghj"])

        """
        
        response = self.get(url=self.server + "/" + id, params={"view": "logs"})
        response.raise_for_status()
        return response.text.split("\n")
