"""
This class contains the functionality of a specific One Codex analysis, related to a sample.
"""

from purl import URL, expand
from v0.common.OneCodexResource import OneCodexResource
from v0.config import Configuration
import requests


class Analysis(OneCodexResource):
    """
    This class allows for interaction with One Codex Analysis API objects, particularly retrieving
    analysis result information for a specified analysis.
    """

    _resource_name = "analyses/"

    def __init__(self, the_id):
        """
        Create a new instance of analysis with the provided id.
        """
        super(Analysis, self).__init__()
        self._id = the_id

    def get_table(self):
        """
        Returns an ordered list of the top hits found for a given Sample against a given
        ReferenceDatabase (per read or contig).
        """
        table_url = self._get_resource_url(id=self._id, action="table")
        request = self.get(table_url)
        return request.json()

    def download_and_save_raw_data_to_path(self, out_path):
        """
        Iterate through the raw data stream and save it to the given path.
        :param out_path: The destination path where the raw data file will be saved.
        """
        with open(out_path, 'wb') as fd:
            chunk_size = 1024
            for chunk in self._iterate_through_raw_data_stream(chunk_size):
                fd.write(chunk)

    def _iterate_through_raw_data_stream(self, chunk_size=1024):
        """
        Stream the raw analysis data (encoded as a tsv.gz file, downloaded in byte chunks).
        :param chunk_size: The size of the chunks in which the file will be downloaded.
        :return: Yields each of the file chunks using a generator.
        """
        raw_data_url = self._get_resource_url(id=self._id, action="raw")
        r = self.get(raw_data_url, stream=True, allow_redirects=True)
        for chunk in r.iter_content(chunk_size):
            yield chunk
