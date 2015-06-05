

from purl import URL
import requests
from v0.config import Configuration


class OneCodexAPIURLBuilder(object):

    _resource_name = None

    def __init__(self):
        assert self._resource_name is not None, "Missing resource definition"

    @classmethod
    def _get_resource_url(cls, id=None, action=None):
        """
        Get a base URL for this resource.
        :return: A string URL with the full path to the resource
        """
        base_url = URL(Configuration.BASE_API_URL).add_path_segment(cls._resource_name)

        if id:
            base_url = base_url.add_path_segment(str(id))

        if action:
            base_url = base_url.add_path_segment(str(action))

        return base_url.as_string()


