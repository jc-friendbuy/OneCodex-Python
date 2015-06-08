"""
This class contains the functionality of a specific One Codex analysis, related to a sample.
"""

from v0.common.OneCodexRequest import OneCodexRequest
from v0.common.OneCodexAPIURLBuilder import OneCodexAPIURLBuilder


class Analysis(object):
    """
    This class allows for interaction with One Codex Analysis API objects, particularly retrieving
    analysis result information for a specified analysis.
    """

    _url_builder = OneCodexAPIURLBuilder("analyses")

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
        table_url = self._url_builder.get_resource_url(id=self._id, action="table")
        request = OneCodexRequest.get(table_url)
        return request.json()

    def download_and_save_raw_data_to_path(self, out_path):
        """
        Iterate through the raw data stream and save it to the given path.
        :param out_path: The destination path where the raw data file will be saved.
        """
        with open(out_path, 'wb') as fd:
            for chunk in self._iterate_through_raw_data_stream(chunk_size=1024):
                fd.write(chunk)

    def _iterate_through_raw_data_stream(self, chunk_size=1024):
        """
        Stream the raw analysis data (encoded as a tsv.gz file, downloaded in byte chunks).
        :param chunk_size: The size of the chunks in which the file will be downloaded.
        :return: Yields each of the file chunks using a generator.
        """
        raw_data_url = self._url_builder.get_resource_url(id=self._id, action="raw")
        r = OneCodexRequest.get(raw_data_url, stream=True)
        for chunk in r.iter_content(chunk_size):
            yield chunk
