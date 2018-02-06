from pong import settings
from pong.utils.helpers import format_time


def get_records(fname=settings.RECORDS_FILENAME):
    """
    Open records file and return list of records.
    """
    try:
        with open(fname, 'r+') as f:
            records = [int(r) for r in f.readlines()]
    except FileNotFoundError:
        with open(fname, 'w+'):
            records = []
    return records


def get_formatted_records(fname=settings.RECORDS_FILENAME):
    """
    Get records from file formatted as MM:SS.
    """
    records = [format_time(int(r)) for r in get_records(fname)]
    return records


def save_records_to_file(seconds, fname=settings.RECORDS_FILENAME):
    """
    Add given time in seconds to the records file.
    """
    records = get_records()
    record_time, idx = recent_time_is_record(seconds, records)
    if record_time:
        records = update_records(idx, seconds, records)
        with open(fname, 'w+') as f:
            for record in records:
                f.write('{}\n'.format(record))


def recent_time_is_record(seconds, records):
    """
    Return True if the given time in seconds is in the top 5
    saved on file.
    """
    if len(records) < 1:
        return True, 0
    for idx, record in enumerate(records):
        if int(seconds) > int(record):
            return True, idx
    return False, None


def update_records(idx, seconds, records):
    """
    Insert time in seconds at a given index in a list of records.
    """
    records.insert(idx, seconds)
    if len(records) > 5:
        records.pop()
    return records
