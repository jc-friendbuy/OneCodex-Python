"""
This class contains the functionality of a specific One Codex analysis, related to a sample.
"""

class Analysis(object):
    """
    This class allows for interaction with One Codex Analysis API objects, particularly retrieving
    analysis result information for a specified analysis.
    """

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
        pass

    def iterate_through_raw_data(self):
        pass

    def save_raw_data_to_path(self, out_path):
        pass
