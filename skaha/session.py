"""Skaha Headless Session."""
from typing import Optional

from attr import attrs

from skaha.client import SkahaClient
from skaha.exceptions import ParameterError


@attrs
class Session(SkahaClient):
    """Skaha Session Client."""

    def __attrs_post_init__(self):
        """Modify the attributes of the SkahaClient class."""
        self.server = self.server + "/session"

    def fetch(
        self,
        kind: Optional[str] = None,
        status: Optional[str] = None,
        view: Optional[str] = None,
    ) -> dict:
        """List open sessions for the user.

        Args:
            kind (str, optional): Session kind. Defaults to None.
            status (str, optional): Session status. Defaults to None.
            view (str, optional): Session view level. Defaults to None.

        Raises:
            ParameterError: When `kind`, `status` or `view` are malformed.

        Returns:
            dict: Session information.

        """
        try:
            params: dict = {}
            if kind:
                assert kind in ["desktop", "notebook", "carta", "headless"]
                params["type"] = kind
            if status:
                assert status in [
                    "Pending",
                    "Running",
                    "Terminating",
                    "Succeeded",
                    "Error",
                ]
                params["status"] = status
            if view:
                assert view in ["all"]
                params["view"] = view
        except Exception as error:
            ParameterError(error)
        response = self.get(url=self.server, params=params)
        return response.json()

    def info(self, session_id: str) -> dict:
        """Get session information.

        Args:
            session_id (str): Session ID.

        Returns:
            dict: Session information.

        """
        return {}

    def logs(self, session_id: str) -> dict:
        """Get session logs.

        Args:
            session_id (str): Session ID.

        Returns:
            dict: Session logs.

        """
        return {}

    def create(
        self,
        name: str,
        image: str,
        cores: int = 1,
        ram: int = 4,
        kind: Optional[str] = None,
        cmd: Optional[str] = None,
        args: Optional[str] = None,
        env: Optional[dict] = None,
    ):
        """Launch a new session.

        Args:
            name (str): The name for the session.
            image (str): The Image ID of the session.
                e.g. images.canfar.net/skaha/notebook-scipy:0.2
            cores (int, optional): Number of cores. Defaults to 1.
            ram (int, optional): Amount of RAM. Defaults to 4.
            kind (str, optional): Session kind for images not from harbor registries.
                Defaults to None.
            cmd (str, optional): Override the image entrypoint. Defaults to None.
            args (str, optional): Override the image CMD params. Defaults to None.
            env (dict, optional): Environment variables. Defaults to None.

        Raises:
            ParameterError: When `kind` is malformed.

        Returns:
            dict: Session information.

        """
        pass

    def destroy(self, session_id: str):
        """Destroy a session.

        Args:
            session_id (str): Session ID.

        Returns:
            dict: Session information.

        """
        pass
