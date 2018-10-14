#!/usr/bin/env python

# https://developers.google.com/calendar/quickstart/python
# pip install --upgrade google-api-python-client oauth2client

import operator

import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import time_utils as tu

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CAL_DAYS = 10
END_DATE = tu.convert_ts_to_string_date(tu.get_now_as_ts() + (86400 * CAL_DAYS)) # now plus 10 days
CAL_LIST = ['arcsecond@gmail.com', 'andrea shear']

def get_events(creds, calendar_id, ):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    #print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId=calendar_id, timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    event_list = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        #print(start, event['summary'])
        event_list.append((start, event['summary']))
    return event_list

def get_creds():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    return creds

def get_all_calendars(creds):
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    cal_results = service.calendarList().list().execute()
    calendars = cal_results.get('items', [])
    return calendars

def get_my_calendars():
    cals = {}
    creds = get_creds()
    calendars = get_all_calendars(creds)
    for cal in calendars:
        #print(res.keys())
        cals[cal['summary']] = cal['id']
    #print(cals.keys())

    all_events = []
    for cal in CAL_LIST:
        events = get_events(creds, cals[cal])
        all_events.extend(events)

    all_events.sort(key=operator.itemgetter(0))
    for event in all_events:
        start_time = None
        if len(event[0]) > 10:
            date = event[0][:10]
            start_time = event[0][12:16]
            end_time = event[0][-4:]
        else:
            date = event[0]
        
        if date <= END_DATE:
            print('{} :: {}'.format(date, event[1]))
            if start_time:
                print('\t{} - {}'.format(start_time, end_time))


if __name__ == '__main__':
    get_my_calendars()
