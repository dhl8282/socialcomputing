#!/usr/bin/env python
"""
Utility for twitter analysis.

Date   : 2014 March 20
Author : donghun.lee7@gmail.com
"""

import re
import util

def getMultipleStatuses(statuses, search_results, twitter_api, max_count):
    """Get multiple statuses up to MAX_COUNT."""

    while (len(statuses) < max_count):
        print "Length of statuses", len(statuses)
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError, e:
            #make next_results if it doesn't exits
            next_results = (search_results['search_metadata']['refresh_url']
                    .replace("since_id", "max_id"))
        kwargs = dict([kv.split('=') for kv in next_results[1:].split('&')])
        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']

def getAttributes(statuses):
    """Get valuable attributes to list from keyword search results."""

    status_texts = [status['text']
            for status in statuses]
    screen_names = [status['user']['screen_name']
            for status in statuses]
    hashtag = [hashtag['text']
            for status in statuses
                for hashtag in status['entities']['hashtags']]
    #Take alphanumeric only from words
    words = [re.sub(r'\W+', '', w) 
            for t in status_texts 
                for w in t.split()]
    return (status_texts, screen_names, 
            util.stringNormalization(hashtag),
            util.stringNormalization(words))
