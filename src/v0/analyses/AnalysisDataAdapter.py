"""
This class is a data adapter for Analysis data -- basically, a wrapper.  Its purpose is to simplify
access to the data fields defined in a data dictionary returned by the One Codex API.  It does
this by centralizing the use of string keys to access the data and therefore preventing their use in
 locations other than this.  It also handles data formatting and typing when appropriate.

 This would also be an ideal place to add data correction, cleanup or barrier code, if necessary.
"""


class AnalysisDataAdapter(object):

    def __init__(self, analysis_data):
        self._data = analysis_data

    @property
    def status(self):
        return self._data[u"analysis_status"]

    @property
    def number_reads(self):
        key = u"n_reads"
        if key in self._data:
            return int(self._data[key])
        else:
            return None

    @property
    def proportion_mapped(self):
        key = u"p_mapped"
        if key in self._data:
            return float(self._data[key])
        else:
            return None

    @property
    def reference_id(self):
        return self._data[u"reference_id"]

    @property
    def reference_name(self):
        return self._data[u"reference_name"]

    @property
    def sample_id(self):
        return self._data[u"sample_id"]

    @property
    def sample_filename(self):
        return self._data[u"sample_filename"]
