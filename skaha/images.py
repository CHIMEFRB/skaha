"""Skaha Image Management."""
from typing import Optional, Dict, Any

from pydantic import root_validator

from skaha.client import SkahaClient
from skaha.utils.logs import get_logger

log = get_logger(__name__)


class Images(SkahaClient):
    """Skaha Image Management.

    Args:
        SkahaClient (object): Skaha HTTP Client

    """

    @root_validator
    def set_server(cls, values: Dict[str, Any]):
        """Sets the server path after validation"""
        values["server"] = values["server"] + "/image"
        return values

    def fetch(self, kind: Optional[str] = None, prune: bool = True) -> list:
        """Get images from Skaha Server.

        Args:
            kind (Optional[str], optional): Type of image. Defaults to None.
            prune (bool, optional): Provide only image name. Defaults to True.

        Returns:
            list: A list of images on the skaha server.

        Examples:
            >>> from skaha.images import Images
                images = Images()
                images.fetch(kind="headless")
            >>> ['images.canfar.net/chimefrb/baseband-polarization:latest',
                ...
                'images.canfar.net/skaha/terminal:0.1']

        """
        data: dict = {}
        if kind:
            data["type"] = kind
        response = self.session.get(url=self.server, params=data).json()
        if prune:
            for index, image in enumerate(response):
                response[index] = image["id"]
        return response
