#!usr/bin/env python
import clusters
"""
Functions for getting words for rss feed and clustering

Date   : 2014 March 27
Author : donghun.lee7@gmail.com
"""

def getHCluster(inputFile):
    """Do Hierarchical Clustering"""

    blognames, words, data = clusters.readfile(inputFile)
    return blognames, words, clusters.hcluster(data)

def getKClusterRotated(inputFile, k):
    """Do K-means Clustering"""

    blognames, words, data = clusters.readfile(inputFile)
    kclust = clusters.kcluster(clusters.rotatematrix(data), k=k)
    return blognames, words, getNumbersToString(words, kclust)

def getNumbersToString(words, clust):
    """Converted returned index to strings"""

    listToReturn = []
    for item in clust:
        singleClust = []
        for i in item:
            singleClust += [words[i]]
        listToReturn += [singleClust]
    return listToReturn

def kclustUntillContainsKeywords(inputFile, startK, word1, word2):
    """Find clust which contains two words in same clust"""

    flag = True
    k = startK
    while(flag):
        # run each k for 5 times
        for x in range(0,5):
            print "K is " + str(k)
            b, w, data = getKClusterRotated(inputFile, k)
            for clust in data:
                if containsWord(word1, clust) & containsWord(word2, clust):
                    return k, clust
        k += 1

def getClustContainsWord(word, clusts):
    """Return clust which contains given word"""

    for clust in clusts:
        if containsWord(word, clust):
            return clust

def containsWord(word, clust):
    """Return true if givem word is in clust"""

    return word in clust

def getClustJson(clust, outputFile, labelData):
    """Save clust data to json file"""

    f = open(outputFile, 'w')
    clusters.jsonclust(clust, f, labels=labelData)
    f.close()
