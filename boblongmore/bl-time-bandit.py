#!/usr/bin/env python

import datetime
import dateutil.parser
from itertools import izip

def get_dates(tstart, tend):
	#convert ISO8601 dates to seconds since epoch
    start_time = dateutil.parser.parse(tstart)
    end_time = dateutil.parser.parse(tend)
    start_seconds = int(start_time.strftime('%s'))
    end_seconds = int(end_time.strftime('%s'))
    return (start_seconds, end_seconds)


def parse_days(t0, t1):
	#takes the beginning and end epoch seconds, finds how many days, 
	#then iterates over those days to make a list of days in seconds since epoch format
	tdelta = t1 - t0
	days = []
	days.append(t0)
	days_count = (tdelta // 86400)
	for day in range(days_count):
		t0 = t0 + 86400
		days.append(t0)
	return(days)

def pairwise(l):
	#using itertools, izip, returns items from the list days in two pairs
	a = iter(l)
	return izip(a, a)

def output_to_user(days):
	#takes a starting time value and an end time value, converts them back to ISO format and outputs to screen
	for day1,day2 in pairwise(days):
		day2 = day2 - 1
		print datetime.datetime.utcfromtimestamp(day1).isoformat() + ', ' + datetime.datetime.utcfromtimestamp(day2).isoformat()

def tb():
	start = '2017-03-27T09:00:00-0700'
	end = '2017-05-27T09:00:00-0700'
	dates = get_dates(start, end)
	days = parse_days(dates[0], dates[1])
	output_to_user(days)

if __name__ == "__main__":
	tb()