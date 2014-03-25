#!/usr/bin/env python
"""
HW1 for Social Computing Class .
Get twitter results and analysis for specific keyword.

Date   : 2014 March 20
Author : donghun.lee7@gmail.com
"""

#import local python files
import hashtag
import retweet
import table
import twitter_setup
import twitter_util
import util

COUNT = 100
MAX_COUNT = 1000
QUERY = 'russia'

def main():
    #Setup 
    twitter_api = twitter_setup.connectTwitterApi()
    search_results = twitter_api.search.tweets(q=QUERY, count=COUNT)
    statuses = search_results['statuses']
    twitter_util.getMultipleStatuses(statuses, search_results, twitter_api,
            MAX_COUNT)
    status_texts, screen_names, hashtag, words = twitter_util.getAttributes(statuses)
    util.saveWordsToFile(words, 'words.txt')

    #Do homework
    util.printHWHeader(QUERY, MAX_COUNT)
    #1. Word Cloud
    print "\nTable of Top10 Words"
    print table.getPrettyTableForWords(words)
    #2. Retweet Statistics
    print "\nTable of Top10 Retweeted Tweets"
    print table.getPrettyTableForRT(retweet.getRT(statuses))
    #3. Hashtag Statistics
    print "\nTable of Top10 Hashtags"
    print table.getPrettyTableForHashtag(hashtag)

if __name__ == '__main__':
    main()
