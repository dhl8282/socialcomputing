#!/usr/bin/env python
"""
Helper to get Hashtag statuses.

Date   : 2014 March 20
Author : donghun.lee7@gmail.com
"""

def countHashtagRate(statuses):
    """Count Hashtag rate from search results."""

    count = 0
    for status in statuses:
        if not status['entities']['hashtags']:
            count = count + 1
    return ("Hashtag rate is " + str(int((count/float(MAX_COUNT))*100)) + '%'
            + ' (' + str(count) + '/' + str(MAX_COUNT) + ')')
