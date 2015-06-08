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

    _url_builder = OneCodexAPIURLBuilder(u"analyses")

    def __init__(self, the_id, status, number_reads, proportion_mapped, reference_id,
                 reference_name, sample_id, sample_filename):
        """
        Create a new instance of Analysis.
        :param the_id: The ID in the One Codex system.
        :param status: The current status of the analysis ("Success", "Pending", or "Failed").
        :param number_reads: Number of reads or contigs in the sample.
        :param proportion_mapped: Proportion of sample reads mapped against the reference (0 to 1).
        :param reference_id: Unique string id of the reference database.
        :param reference_name: Human-readable name of the reference database.
        :param sample_id: Unique string id of the sample.
        :param sample_filename: Name of the uploaded sample.
            By default, this should be the same as the name of the uploaded FASTA or FASTQ file.
        :return: A new instance of Analysis.
        """
        self.id = the_id
        self.status = status
        self.number_reads = number_reads
        self.percentage_mapped = proportion_mapped
        self.reference_id = reference_id
        self.reference_name = reference_name
        self.sample_id = sample_id
        self.sample_filename = sample_filename

    def get_table(self):
        """
        Returns an ordered list of the top hits found for a given Sample against a given
        ReferenceDatabase (per read or contig).
        """
        table_url = self._url_builder.get_resource_url(id=self.id, action=u"table")
        request = OneCodexRequest.get(table_url)
        return request.json()

    def download_and_save_raw_data_to_path(self, out_path):
        """
        Iterate through the raw data stream and save it to the given path.
        :param out_path: The destination path where the raw data file will be saved.
        """
        with open(out_path, u"wb") as fd:
            for chunk in self._iterate_through_raw_data_stream(chunk_size=1024):
                fd.write(chunk)

    def _iterate_through_raw_data_stream(self, chunk_size=1024):
        """
        Stream the raw analysis data (encoded as a tsv.gz file, downloaded in byte chunks).
        :param chunk_size: The size of the chunks in which the file will be downloaded.
        :return: Yields each of the file chunks using a generator.
        """
        raw_data_url = self._url_builder.get_resource_url(id=self.id, action=u"raw")
        r = OneCodexRequest.get(raw_data_url, stream=True)
        for chunk in r.iter_content(chunk_size):
            yield chunk
