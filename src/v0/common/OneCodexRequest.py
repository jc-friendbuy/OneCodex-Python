import requests
from v0.config import Configuration


class OneCodexRequest(object):

    @classmethod
    def get(cls, url, **kwargs):
        """
        Issue a get request to the given action
        :param url: The One Codex URL to which the GET request will be issued.
        :return: The request object to the given One Codex URL.
        """
        request = requests.get(url, **cls._get_request_configuration_kwargs(kwargs))
        request.raise_for_status()
        return request

    @classmethod
    def _get_request_configuration_kwargs(cls, kwargs=None):
        """
        Get a dictionary with normalized requests configuration options for creating requests.
        :param kwargs: A set of keyword arguments to be applied over the default configuration
        options (may be None, in which case only the defaults will be used).
        :return: A dictionary with requests configuration values set.
        """
        if not kwargs:
            kwargs = dict()
        config = dict()
        config.update(auth=cls._get_authentication_object())
        config.update(kwargs)
        return config

    @classmethod
    def _get_authentication_object(cls):
        """
        Get the authentication object to be passed into a request.
        :return: A (username, password) tuple to be used for authentication with the One Codex
        API (via HTTP basic auth).
        """
        return (Configuration.get_api_key(), u"")