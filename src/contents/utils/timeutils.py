import datetime


def convert_datetime(days):
    time_now = datetime.datetime.now().timestamp()
    days_in_sec = days*24*60*60

    time_diff = time_now - days_in_sec

    dt_object = datetime.fromtimestamp(time_diff)
    return  dt_object

