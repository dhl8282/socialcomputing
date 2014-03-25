#!/usr/bin/env python
"""
Twitter api setup.

Date   : 2014 March 20
Author : donghun.lee7@gmail.com
"""

import twitter

CONSUMER_KEY = 'ScN0r4hXjWMC7zBBT8ZPw'
CONSUMER_SECRET = 'CdL2qYraRfhl8kC3Nk94xuxvlfVSy1fngKYUCZhc'
OAUTH_TOKEN = '199929377-HVXtaZFvu6frKntYbTJjGMfSVjU9pwbEZtyZMoZE'
OAUTH_TOKEN_SECRET = 'H0uPUGQYR56oBerJ7Im12gjizrWAGJrZJHssjWv6mSMFG'

def connectTwitterApi():
    """Connect to twitter api."""

    auth = twitter.oauth.OAuth(OAUTH_TOKEN,
    OAUTH_TOKEN_SECRET,
    CONSUMER_KEY,
    CONSUMER_SECRET)
    return twitter.Twitter(auth=auth)
