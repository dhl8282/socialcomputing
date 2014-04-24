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
for authname in os.listdir(BASE_DIR):
    authdir = os.path.join(BASE_DIR, authname)
    filenames = os.listdir(authdir)
    filepath = os.path.join(authdir, filenames[0])
    file = open(filepath, 'r')
    text = file.read()
    articles += [{'filename':filenames[0], 'text':text}]
    if (len(articles) == N_ARTICLES):
        break

def _score_sentences(sentences, important_words):
    scores = []
    sentence_idx = -1
    for s in [nltk.tokenize.word_tokenize(s) for s in sentences]:
        sentence_idx += 1
        word_idx = []
        # For each word in the word list...
        for w in important_words:
            try:
                # Compute an index for where any important words occur in the sentence
                word_idx.append(s.index(w))
            except ValueError, e: # w not in this particular sentence
                pass
        word_idx.sort()
        # It is possible that some sentences may not contain any important words at all
        if len(word_idx)== 0: continue
        # Using the word index, compute clusters by using a max distance threshold
        # for any two consecutive words
        clusters = []
        cluster = [word_idx[0]]
        i = 1
        while i < len(word_idx):
            if word_idx[i] - word_idx[i - 1] < CLUSTER_THRESHOLD:
                cluster.append(word_idx[i])
            else:
                clusters.append(cluster[:])
                cluster = [word_idx[i]]
            i += 1
        clusters.append(cluster)
        # Score each cluster. The max score for any given cluster is the score
        # for the sentence
        max_cluster_score = 0
        for c in clusters:
            significant_words_in_cluster = len(c)
            total_words_in_cluster = c[-1] - c[0] + 1
            score = 1.0 * significant_words_in_cluster \
                * significant_words_in_cluster / total_words_in_cluster
            if score > max_cluster_score:
                max_cluster_score = score
        scores.append((sentence_idx, max_cluster_score))
    return scores

def summarize(txt):
    sentences = [s for s in nltk.tokenize.sent_tokenize(txt)]
    normalized_sentences = [s.lower() for s in sentences]
    words = [w.lower() for sentence in normalized_sentences for w in
             nltk.tokenize.word_tokenize(sentence)]
    fdist = nltk.FreqDist(words)
    top_n_words = [w[0] for w in fdist.items()
            if w[0] not in nltk.corpus.stopwords.words('english')][:N]
    scored_sentences = _score_sentences(normalized_sentences, top_n_words)
    # Summaization Approach 1:
    # Filter out non-significant sentences by using the average score plus a
    # fraction of the std dev as a filter
    avg = numpy.mean([s[1] for s in scored_sentences])
    std = numpy.std([s[1] for s in scored_sentences])
    mean_scored = [(sent_idx, score) for (sent_idx, score) in scored_sentences
                   if score > avg + 0.5 * std]
    # Summarization Approach 2:
    # Another approach would be to return only the top N ranked sentences
    top_n_scored = sorted(scored_sentences, key=lambda s: s[1])[-TOP_SENTENCES:]
    top_n_scored = sorted(top_n_scored, key=lambda s: s[0])
    # Decorate the post object with summaries
    return dict(top_n_summary=[sentences[idx] for (idx, score) in top_n_scored],
                mean_scored_summary=[sentences[idx] for (idx, score) in mean_scored])


# A minimalist approach or scraping the text out of a web page. Lots of time could
# be spent here trying to extract the core content, detecting headers, footers, margins,
# navigation, etc.

if __name__ == '__main__':
    # It's entirely possible that this "clean page" will be a big mess. YMMV.
    # The good news is that summarize algorithm inherently accounts for handling
    # a lot of this noise.

    for article in articles:
        # Uses previously defined summarize function.
        article.update(summarize(article['text']))
        #
        article['top_n_summary_marked_up'] = '<p>%s</p>' % (article['text'],)
        for s in article['top_n_summary']:
            marked_up = article['top_n_summary_marked_up'].replace(s, '<strong>%s</strong>' % (s, ))
            article['top_n_summary_marked_up'] = marked_up
        filename = article['filename'] + '.TopSummary.html'
        f = open(filename, 'w')
        #
        html = HTML_TEMPLATE % (article['filename'], article['top_n_summary_marked_up'],)
        f.write(html.encode('utf-8'))
        f.close()
        print "Data written to", f.name

    for article in articles:
        article['mean_scored_summary_marked_up'] = '<p>%s</p>' % (article['text'],)
        for s in article['mean_scored_summary']:
            marked_up = article['mean_scored_summary_marked_up'].replace(s, '<strong>%s</strong>' % (s, ))
            article['mean_scored_summary_marked_up'] = marked_up
        filename = article['filename'] + '.MeanScoredSummary.html'
        f = open(filename, 'w')
        #
        html = HTML_TEMPLATE % (article['filename'], article['mean_scored_summary_marked_up'],)
        f.write(html.encode('utf-8'))
        f.close()
        print "Data written to", f.name
    """
    print "-------------------------------------------------"
    print "                'Top N Summary'"
    print "-------------------------------------------------"
    print " ".join(summary['top_n_summary'])
    print
    print
    print "-------------------------------------------------"
    print "             'Mean Scored' Summary"
    print "-------------------------------------------------"
    print " ".join(summary['mean_scored_summary'])
    """
