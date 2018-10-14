#!/usr/bin/env python
import time
import datetime

def convert_string_date_to_dt(date_string):
    '''expects date: YYYY-MM-DD'''
    return datetime.datetime.strptime(date_string, '%Y-%m-%d')

def convert_string_date_to_ts(date_string):
    dt = convert_string_date_to_dt(date_string)
    return convert_dt_to_ts(dt)

def convert_ts_to_string_date(ts):
    return convert_ts_to_dt(ts).strftime('%Y-%m-%d')

def convert_full_string_to_dt(full_string):
    return datetime.datetime.strptime(full_string, '%a, %d %b %Y %H:%M:%S %z')

def convert_full_string_to_ts(full_string):
    return convert_dt_to_ts(convert_full_string_to_dt(full_string))

def convert_dt_to_ts(dt):
    '''expects a datetime object'''
    return time.mktime(dt.timetuple())

def convert_ts_to_dt(ts):
    '''exects a timestamp'''
    return datetime.datetime.fromtimestamp(ts)

def get_now_as_dt():
    import pytz
    now = datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('%a, %d %b %Y %H:%M:%S %z')
    return datetime.datetime.now()

def get_now_as_ts():
    return time.time()

def get_today():
    today = datetime.date.today()
    fmt_today = '{:%Y-%m-%d}'.format(today)
    return fmt_today

def get_full_string_from_dt(dt):
    return dt.strftime('%a, %d %b %Y %H:%M:%S %z')

def get_full_string_from_ts(ts):
    dt = convert_ts_to_dt(ts)
    return get_full_string_from_dt(dt)
    
