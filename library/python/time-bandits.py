#!/usr/bin/env python
#
"""
    time-bandits.py

    Copyright (c) 2017 World Wide Technology, Inc.
    All rights reserved.

    Author: Joel W. King (GitHub: @joelwking, Twitter: @joel_w_king)

"""
#
from datetime import datetime
#
class Connector(object):
    """ Class used for demonstration.
    """
    MAX_DURATION = 86400                                   # seconds in a day, 24 * 60 * 60

    def __init__(self):
        """ Not used.
        """

    def iso8601_epoch(self, iso8601="2017-05-27T09:00:00-0700"):
        """ Convert timestamp iso8601 string to epoch string,
            return epoch as an integer.
        """
        p = '%Y-%m-%dT%H:%M:%S-' + iso8601[-4:]
        epoch = datetime(1970, 1, 1)
        return int((datetime.strptime(iso8601, p) - epoch).total_seconds())

    def gimme_two_dates(self, t0="2017-05-25T09:00:00-0700", t1="2017-05-27T09:05:00-0700"):
        """ Input is the user entered start (t0) and end (t1) times to query,
            Tetration API can query based either  iso8601 or epoch time in the API call.
            However, Tetration only allows querying maximum time range of 1 day per request.
            If a user wants to query a longer time range, they need to split that time range
            into 1 day time periods and query separately for each period.
        """
        try:
            t0 = self.iso8601_epoch(iso8601=t0)
            t1 = self.iso8601_epoch(iso8601=t1)
        except ValueError as e:
            return []                                      # error due to input format errors

        time_range = [(t0, t1)]
        if t0 > t1:                                        # sanity check, let the API return the error
            return time_range

        if t1 <= (t0 + Connector.MAX_DURATION):            # range was less than a day, return original values
            return time_range
        else:
            time_range = []
            nmbr_iterations =  -(-(t1 - t0) // Connector.MAX_DURATION) # round up
            for i in range(1, nmbr_iterations):            # loop for all but the last
                t1a = t0 + (Connector.MAX_DURATION - 1)    # one second less than 24 hours
                time_range.append((t0, t1a))               # create list entry
                t0 = t1a + 1                               # create next start time, add one second
            time_range.append((t0, t1))                    # last element

        return time_range                                  # return list of tuples, the t0, t1 values

def main():

    # Test data
    demo = []
    demo.append(("2017-05-25T09:00:00-0000", "2017-05-27T09:05:00-0000"))
    demo.append(("2017-03-05T19:00:00-0600", "2017-03-07T09:05:00-0600"))
    demo.append(("2017-03-05T19:00:00-0500", "2017-03-07T09:05:00-0500"))
    demo.append(("2017-06-05T19:00:00-0500", "2017-04-27T09:05:00-0500"))

    tb = Connector()

    # Run test
    for item in demo:   
        time_range = tb.gimme_two_dates(t0=item[0], t1=item[1])
        # Output returned values
        print "\n%s" % time_range
        for item in time_range:
            print "%s %s" % (datetime.fromtimestamp(item[0]).strftime('%c'), 
                               datetime.fromtimestamp(item[1]).strftime('%c'))

if __name__ == '__main__':
    main()
