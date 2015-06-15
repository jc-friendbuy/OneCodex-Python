"""
This class is a data adapter for Analysis data -- basically, a wrapper.  Its purpose is to simplify
access to the data fields defined in a data dictionary returned by the One Codex API.  It does
this by centralizing the use of string keys to access the data and therefore preventing their use in
 locations other than this.  It also handles data formatting and typing when appropriate.

 This would also be an ideal place to add data correction, cleanup or barrier code, if necessary.
"""


class AnalysisDataAdapter(object):

    def __init__(self, analysis_data):
        """
        Initialize a new AnalysisDataAdapter to control access to the data provided.
        :param analysis_data: The analysis data from the One Codex API to access.
        """
        self._data = analysis_data

    @property
    def status(self):
        """
        Get the status of the analysis from the data.
        :return: The analysis_status field from the data dictionary set to this object.
        """
        return self._data[u"analysis_status"]

    @property
    def number_reads(self):
        """
        Get the number of reads of the analysis from the data, formatted as an int if it exists,
        or None if it doesn't.
        :return: The n_reads field from the data dictionary set to this object.
        """
        key = u"n_reads"
        if key in self._data:
            return int(self._data[key])
        else:
            return None

    @property
    def proportion_mapped(self):
        """
        Get the proportion mapped of the analysis from the data, formatted as a float if it exists,
        or None if it doesn't.
        :return: The p_mapped field from the data dictionary set to this object.
        """
        key = u"p_mapped"
        if key in self._data:
            return float(self._data[key])
        else:
            return None

    @property
    def reference_id(self):
        """
        Get the reference ID of the analysis from the data.
        :return: The reference_id field from the data dictionary set to this object.
        """
        return self._data[u"reference_id"]

    @property
    def reference_name(self):
        """
        Get the reference name of the analysis from the data.
        :return: The reference_name field from the data dictionary set to this object.
        """
        return self._data[u"reference_name"]

    @property
    def sample_id(self):
        """
        Get the sample ID of the analysis from the data.
        :return: The sample_id field from the data dictionary set to this object.
        """
        return self._data[u"sample_id"]

    @property
    def sample_filename(self):
        """
        Get the sample filename of the analysis from the data.
        :return: The sample_filename field from the data dictionary set to this object.
        """
        return self._data[u"sample_filename"]
