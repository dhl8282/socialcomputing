#!/usr/bin/env python
"""
Helper to get Retweet statuses.

Date   : 2014 March 20
Author : donghun.lee7@gmail.com
"""

def getRT(statuses):
    """Get RT status from twitter search statuses."""

    retweets_dup = [
            (status['retweet_count'], 
            status['retweeted_status']['user']['screen_name'], 
            status['text'])
            for status in statuses 
            if status.has_key('retweeted_status')]
    return list(set(retweets_dup))
