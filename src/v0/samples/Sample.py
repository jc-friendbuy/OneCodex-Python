"""
Sample class.  It provides access to the details of a specific sample (FASTA or FASTQ file)
uploaded via the API or web platform to the One Codex system.
"""

from util.time import localize_utc_datetime_to_local_timezone


class Sample(object):

    def __init__(self, the_id, filename, size, size_in_bytes, upload_date_utc, upload_status):
        """
        Initialize a new Sample instance with the provided arguments.
        :param the_id: The unique sample ID
        :param filename: The filename of the uploaded sample
        :param size: Human-readable size of the uploaded sample's underlying file, e.g., 4.5MB
        :param size_in_bytes: Size of the uploaded file in bytes
        :param upload_date_utc: Date and time of the upload (in UTC)
        :param upload_status: Status of the upload, e.g., "Successfully uploaded." or
        "Uploading and processing..."
        """
        self.id = the_id
        self.filename = filename
        self.human_readable_size = size
        self.size_in_bytes = size_in_bytes,
        self.upload_date = upload_date_utc
        self.upload_status = upload_status

    @property
    def localized_upload_date(self):
        """
        Get the upload date of this sample, localized to the local timezone.  Useful for
        presentation purposes, but nothing more.  Localized dates SHOULD NOT be used for
        comparisons or date computation.  Use the upload_date property instead, which is in the
        UTC timezone.
        :return: A datetime object localized to this system's timezone.
        """
        return localize_utc_datetime_to_local_timezone(self.upload_date)
