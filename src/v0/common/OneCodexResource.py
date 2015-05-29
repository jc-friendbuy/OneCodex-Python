

from purl import URL
import requests
from v0.config import Configuration


class OneCodexResource(object):

    _resource_name = None

    def __init__(self):
        assert self._resource_name is not None, "Missing resource definition"

    def get(self, url, **kwargs):
        """
        Issue a get request to the given action
        :param url: The One Codex URL to which the GET request will be issued.
        :return: The request object to the given One Codex URL.
        """
        request = requests.get(url, **self._get_request_configuration_kwargs(kwargs))
        request.raise_for_status()
        return request

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

    def _get_request_configuration_kwargs(self, kwargs):
        config = dict()
        config.update(auth=self._get_authentication_object())
        config.update(kwargs)
        return config

    @staticmethod
    def _get_authentication_object():
        """
        Get the authentication object to be passed into a request.
        :return: A (username, password) tuple to be used for authentication with the One Codex
        API (via HTTP basic auth).
        """
        return (Configuration.get_api_key(), "")
