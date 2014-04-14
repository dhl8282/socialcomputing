#!/usr/bin/python
import rss

#Get feed contents from feedlist
def getFeedContents():
    feedlist = [line for line in file('feedlist.txt')]
    blog = []
    for feedurl in feedlist:
        try:
            (title, w) = rss.getWordsAndTitle(feedurl)
            print title
            blog += [{'author':title, 'text':w}]
        except:
            print 'Failed to parse feed %s' % feedurl
    return blog