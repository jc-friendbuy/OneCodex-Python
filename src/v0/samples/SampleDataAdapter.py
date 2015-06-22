from datetime import datetime
from util.time import get_datetime_as_utc


class SampleDataAdapter(object):

    def __init__(self, sample_data):
        self._sample_data = sample_data

    @property
    def id(self):
        """
        Get the id field of the sample data assigned to this object.
        :return: The id of the sample
        """
        return self._sample_data[u"id"]

    @property
    def filename(self):
        """
        Get the filename field of the sample data assigned to this object.
        :return: The filename of the sample
        """
        return self._sample_data[u"filename"]

    @property
    def size(self):
        """
        Get the size field of the sample data assigned to this object.
        :return: The size in of the sample in a human-readable form
        """
        return self._sample_data[u"size"]

    @property
    def size_in_bytes(self):
        """
        Get the size_bytes field of the sample data assigned to this object formatted as an int.
        :return: The size in bytes of the sample
        """
        return int(self._sample_data[u"size_bytes"])

    @property
    def upload_date(self):
        """
        Get the upload_date field of the sample data assigned to this object formatted as
        UTC-localized datetime object.
        :return: The upload date of the sample
        """
        date_string = self._sample_data[u"upload_date"]
        raw_date = datetime.strptime(date_string, u"%Y-%m-%d %H:%M:%S")
        return get_datetime_as_utc(raw_date)

    @property
    def upload_status(self):
        """
        Get the upload_status field of the sample data assigned to this object formatted as an int.
        :return: The status of the upload of the sample's file
        """
        return self._sample_data[u"upload_status"]
