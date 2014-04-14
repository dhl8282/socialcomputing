#!usr/bin/env python
import blogdata
import rss
"""
Get words from rss feed and cluster them

Date   : 2014 April 1
Author : donghun.lee7@gmail.com
"""

#1. Draw Hierarchical clustering with provided blogdata.txt
blognames, words, clust = blogdata.getHCluster('blogdata.txt')
blogdata.getClustJson(clust, 'dendrogram.json', blognames)

#2. Draw H Clustering with custom rss feed list
rss.getWordsFromFeedlist()
blognames, words, clust = blogdata.getHCluster('rss.txt')
blogdata.getClustJson(clust, 'dendrogram.json', blognames)

#3. Use #2 data to get K-means Clustering and print
# words in same group with Google and Apple
blognames, words, kclust = blogdata.getKClusterRotated('rss.txt', k=10)
print "Words in clust which contains word google"
print blogdata.getClustContainsWord("google", kclust)
print ""
print "Words in clust which contains word apple"
print blogdata.getClustContainsWord("apple", kclust)

