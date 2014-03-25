#!/usr/bin/env python
"""
PrettyTable helper.

Date   : 2014 March 20
Author : donghun.lee7@gmail.com
"""

from collections import Counter
from prettytable import PrettyTable

def getPrettyTableForTwoColumns(words, colName):
    """Helper function for prettytable with 2 columns."""

    pt = PrettyTable(field_names=[colName, 'Count'])
    c = Counter(words)
    for kv in c.most_common()[:10]:
        pt.add_row(kv)
    pt.align[colName], pt.align['Count'] = 'l', 'r'
    return pt

def getPrettyTableForWords(words):
    """Get prettytable for Words."""

    return getPrettyTableForTwoColumns(words, 'Words')

def getPrettyTableForHashtag(words):
    """Get prettytable for Hashtag."""

    return getPrettyTableForTwoColumns(words, 'Hashtag')

def getPrettyTableForRT(words):
    """Get prettytable for Retweet."""

    pt = PrettyTable(field_names=['Count', 'Screen Name', 'Text'])
    for row in sorted(words, reverse=True)[:10]:
        pt.add_row(row)
    pt.max_width['Text'] = 50
    pt.align = 'l'
    return pt
