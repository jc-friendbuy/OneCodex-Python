"""
This class contains the functionality of a specific One Codex analysis, related to a sample.
"""

from purl import URL, expand
from v0.config import Configuration
import requests


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
        table_results = requests.get(table_url, auth=self._get_authentication_information()).json()
        return table_results

    def iterate_through_raw_data(self):
        pass

    def save_raw_data_to_path(self, out_path):
        # with open(filename, 'wb') as fd:
        #     for chunk in r.iter_content(chunk_size):
        #         fd.write(chunk)
        pass

    @staticmethod
    def _get_authentication_information():
        """
        Get the authentication object to be passed into the resource request for analyses.
        :return: A (username, password) tuple to be used for authentication with the One Codex
        API (via HTTP basic auth).
        """
        return (Configuration.get_api_key(), "")

    def _get_resource_url(self):
        """
        Get the URL for the Analyses resource with this object's id.
        :return: A string URL.
        """
        return URL(Configuration.BASE_API_URL)\
            .add_path_segment(expand(Analysis.RESOURCE_PATH, {"id": self._id}))\
            .as_string()

    def _get_action_url(self, action):
        """
        Get a URL for the Analyses resource referenced by this object, with the provided action (
        action here represents a segment of the URL's path).
        :param action: A string that specifies the action to be referenced by the URL.
        :return: A string URL that references the Analyses resource with the provided action.
        """
        return URL(self._get_resource_url()).add_path_segment(action).as_string()
