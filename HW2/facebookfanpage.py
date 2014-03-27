#!/usr/bin/env python

import re
import requests

#local file import
import util

def getMsgs(feeds):
    msgs = [re.sub(r'\W+', '', w) 
            for f in getDataWithMsgs(feeds)
            for w in f['message'].split()]
    return util.stringNormalization(getURLRemovedMsgs(msgs))

def getURLRemovedMsgs(lists):
    return [item for item in lists
            if not re.match(r'^http', item)]

def getDataWithMsgs(feeds):
    return [t for t in feeds
            if t.has_key('message')]

def getFanpageFeeds(facebook_api, query, count):
    g = facebook_api.get_connections(query, 'feed')
    data = g['data']
    while (len(data) < count):
        next_url = g['paging']['next']
        g = requests.get(getUrlWithLimitCount(next_url, count)).json()
        data += g['data']
    return data

def getUrlWithLimitCount(url, count):
    return url.replace(re.search('limit=\d+', url).group(), 'limit='+str(count))
