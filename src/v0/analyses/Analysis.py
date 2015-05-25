"""
This class contains the functionality of a specific One Codex analysis, related to a sample.
"""

from purl import URL, expand
from v0.config import Configuration
import requests
from requests.auth import HTTPDigestAuth


class Analysis(object):
    """
    This class allows for interaction with One Codex Analysis API objects, particularly retrieving
    analysis result information for a specified analysis.
    """

    RESOURCE_PATH = "analyses/{id}"

    def __init__(self, the_id):
        """
        Create a new instance of analysis with the provided id.
        """
        self._id = the_id

    def get_table(self):
        """
        Returns an ordered list of the top hits found for a given Sample against a given
        ReferenceDatabase (per read or contig).
        """
        table_url = self._get_action_url("table")
        table_results = requests.get(table_url, auth=self._get_authentication_information())

    def iterate_through_raw_data(self):
        pass

    def save_raw_data_to_path(self, out_path):
        pass

    @staticmethod
    def _get_authentication_information():
        return HTTPDigestAuth(Configuration.API_KEY, "")

    def _get_resource_url(self):
        return URL(Configuration.BASE_API_URL)\
            .add_path_segment(expand(Analysis.RESOURCE_PATH, {"id": self._id}))\
            .as_string()

    def _get_action_url(self, action):
        resource_url = URL(self._get_resource_url())
        action_url = resource_url.path(action)
        return action_url
