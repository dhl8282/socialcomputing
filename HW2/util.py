#!/usr/bin/env python
#coding: utf-8
"""
Utility for trivials.

Date   : 2014 March 20
Author : donghun.lee7@gmail.com
"""

import json
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def stringNormalization(listOfInput):
    """Normalize sting using Regex and Stemmer library."""

    stop = stopwords.words('english')
    stop_words = (nltk.corpus.stopwords.words('english') + 
            ['.', ',', '--', '\'s', '?', '!', ')', '(', ':', '\'','\'re', '"',
            '-', '}', '{', u'—', 'rt', 'http', 't', 'co', '@', '#',])
    tokens = []
    for wordInput in listOfInput:
        tokens += (nltk.tokenize.word_tokenize(
                re.sub(r'W+', '', wordInput.lower())))
    stemmer = PorterStemmer()
    stemmed = []
    for token in tokens:
        if '/t.co/' in token or token is '' or token in stop_words:
            continue
        stemmed.append(stemmer.stem(token))
    return stemmed

def saveWordsToFile(words, filename):
    """Save list of words in spicified filename."""

    f = file(filename, 'w')
    for word in words:
        try:
            f.write(word.encode('utf-8') + '\n')
        except UnicodeEncodeError, e:
            print 'Encoding error' + word + '\n'
    f.close()

def printHWHeader(keyword, count):
    """Print Header for HW1."""

    print (
            "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n" +
            "Social Computing HW1\n" +
            "Donghun Lee, 2012-23867\n" +
            "This is twitter result for\n" +
            "Keyword :" + keyword + " Query amount :" + str(count))

def dump(content):
    print json.dumps(content, indent=1)
