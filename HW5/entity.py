#!usr/bin/env python
# -*- coding: utf-8 -*-
import json
import nltk
import numpy
import os

HTML_TEMPLATE = """<html>
        <head>
            <title>%s</title>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
        </head>
        <body>%s</body>
    </html>"""
BASE_DIR = '/home/john/cs/socialcomputing/HW5/C50/C50train'

N = 100 # Number of words to consider
CLUSTER_THRESHOLD = 5 # Distance between words to consider
TOP_SENTENCES = 5 # Number of sentences to return for a "top n" summary
N_ARTICLES = 10 # Number of articles to consider

articles = []
least_articles = []
for authname in os.listdir(BASE_DIR):
    authdir = os.path.join(BASE_DIR, authname)
    filenames = os.listdir(authdir)
    for filename in filenames:
        filepath = os.path.join(authdir, filename)
        file = open(filepath, 'r')
        text = file.read()
        articles += [{'filename':filename, 'text':text}]
        
#Get top 10 ariticles with least words
def getNTopLeastAtricles(articles, n):
    articles_to_return = []
    counts = getArticleTextCount(articles)
    sorted_count = sorted(counts, key=lambda c:c[0])[:n]
    indices = [index for count, index in sorted_count]
    for i in indices:
        articles_to_return += [articles[i]]
    return articles_to_return

def getArticleTextCount(articles):
    count = []
    for i in range(len(articles)):
        count += [(len(articles[i]['text']), i)]
    return count

def extract_interactions(txt):
    sentences = nltk.tokenize.sent_tokenize(txt)
    tokens = [nltk.tokenize.word_tokenize(s) for s in sentences]
    pos_tagged_tokens = [nltk.pos_tag(t) for t in tokens]
    entity_interactions = []
    for sentence in pos_tagged_tokens:
        all_entity_chunks = []
        previous_pos = None
        current_entity_chunk = []
        for (token, pos) in sentence:
            if pos == previous_pos and pos.startswith('NN'):
                current_entity_chunk.append(token)
            elif pos.startswith('NN'):
                if current_entity_chunk != []:
                    all_entity_chunks.append((' '.join(current_entity_chunk),
                            pos))
                current_entity_chunk = [token]
            previous_pos = pos
        if len(all_entity_chunks) > 1:
            entity_interactions.append(all_entity_chunks)
        else:
            entity_interactions.append([])
    assert len(entity_interactions) == len(sentences)
    return dict(entity_interactions=entity_interactions,
                sentences=sentences)

least_articles = getNTopLeastAtricles(articles, N_ARTICLES)
for article in least_articles:
    article.update(extract_interactions(article['text']))
    #
    article['marked_up'] = '<p>%s</p>' % (article['text'],)
    words = []
    for s in article['entity_interactions']:
        for w,t in s:
            words += [w]
        for w in words:
            marked_up = article['marked_up'].replace(w, '<strong>%s</strong>' % (w, ))
            article['marked_up'] = marked_up
    filename = article['filename'] + '.Entity.html'
    f = open(filename, 'w')
    #
    html = HTML_TEMPLATE % (article['filename'], article['marked_up'],)
    f.write(html.encode('utf-8'))
    f.close()
    print "Data written to", f.name