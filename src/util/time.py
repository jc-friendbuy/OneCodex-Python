import pytz
import tzlocal


def localize_utc_datetime_to_local_timezone(utc_datetime):
    local_timezone = tzlocal.get_localzone()
    return utc_datetime.astimezone(local_timezone)


def get_datetime_as_utc(a_datetime):
    return pytz.utc.localize(a_datetime)
