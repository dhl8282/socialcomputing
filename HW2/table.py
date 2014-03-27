#!/usr/bin/env python
"""
PrettyTable helper.

Date   : 2014 March 20
Author : donghun.lee7@gmail.com
"""

from collections import Counter
from prettytable import PrettyTable

def getPrettyTableForTwoColumns(words, colName1, colName2, count):
    """Helper function for prettytable with 2 columns."""

    pt = PrettyTable(field_names=[colName1, colName2])
    c = Counter(words)
    for kv in c.most_common()[:count]:
        pt.add_row(kv)
    pt.align[colName1], pt.align[colName2] = 'l', 'r'
    return pt
