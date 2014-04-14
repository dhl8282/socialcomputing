import json
import matrix
import nltk
import os

DATA_DIR = './C50/C50test'

def getReuter50Data():
    reuter = []
    for authorname in os.listdir(DATA_DIR):
        if authorname.startswith('.'):
            continue
        author_dir = os.path.join(DATA_DIR, authorname)
        for filename in os.listdir(author_dir):
            if not filename.endswith('.txt'):
                continue
            filepath = os.path.join(author_dir, filename)
            file = open(filepath, 'r')
            text = file.read()
            reuter += [{'author':authorname, 'filepath':filepath, 'filename':filename, 'text':text}]
    return reuter

def getReuter50FirstArticle():
    reuter = []
    for authorname in os.listdir(DATA_DIR):
        if authorname.startswith('.'):
            continue
        author_dir = os.path.join(DATA_DIR, authorname)
        for filename in os.listdir(author_dir):
            if not filename.endswith('.txt'):
                continue
            filepath = os.path.join(author_dir, filename)
            file = open(filepath, 'r')
            text = file.read()
            reuter += [{'author':authorname, 'filepath':filepath, 'text':text}]
            break
    return reuter

def searchReuter50(textCorpus, listOfQuery, limit=10):
    print listOfQuery
    activities = [article['text'].lower().split() for article in textCorpus]
    tc = nltk.TextCollection(activities)
    relevant_activities = []
    for idx in range(len(activities)):
        score = 0
        for term in [t.lower() for t in listOfQuery]:
            score += tc.tf_idf(term, activities[idx])
        if score > 0:
            relevant_activities.append({'score': score, 'author': textCorpus[idx]['author'],
                    'filepath': textCorpus[idx]['filepath']})

    relevant_activities = sorted(relevant_activities, key=lambda p:p['score'], reverse=True)
    for activity in relevant_activities[:limit]:
        print activity['author']
        print '\tFile: %s' % (activity['filepath'], )
        print '\tScore: %s' % (activity['score'], )
    print

def getTDMatrix(textCorpus):
    all_articles = [article['text'].lower().split() for article in textCorpus]

    tc = nltk.TextCollection(all_articles)

    # Compute a term-document matrix such that td_matrix[doc_title][term]
    # returns a tf-idf score for the term in the document
    td_matrix = {}
    i = 0
    for idx in range(len(all_articles)):
        i += 1
        print i
        article = all_articles[idx]
        fdist = nltk.FreqDist(article)
        doc_title = textCorpus[idx]['author']
        td_matrix[doc_title] = {}
        # takes long..
        for term in fdist.iterkeys():
            td_matrix[doc_title][term] = tc.tf_idf(term, article)
    return td_matrix

def getDoc(td_matrix, filename='matrix.json'):
    viz_links = []
    viz_nodes = [ {'title' : title} for title in td_matrix.keys() ]
    idnum = 0
    for vn in viz_nodes:
        vn.update({'idx' : idnum})
        idnum += 1
    idx = dict(zip([ node['title'] for node in viz_nodes ], range(len(viz_nodes))))
    distances = {}
    for title1 in td_matrix.keys():
        distances[title1] = {}
        min_dist = 1.0
        most_similar = None
        for title2 in td_matrix.keys():
            if title1 == title2:
                continue
            # Compute similarity amongst documents
            terms1 = td_matrix[title1]
            terms2 = td_matrix[title2]
            distances[title1][title2] = matrix.compute_similarity(terms1, terms2)
            if distances[title1][title2] < min_dist:
                min_dist = distances[title1][title2]
                most_similar = title2
            viz_links.append({'source' : idx[title1], 'target' : idx[most_similar], 'score' : 1 - min_dist})
    f = open(filename, 'w')
    f.write(json.dumps({'nodes' : viz_nodes, 'links' : viz_links}, indent=1))
    f.close()

def readJson(filename):
    return json.load(open(filename))

def sortByScore(filename):
    a = readJson(filename)
    links = a['links']
    sortedLinks = sorted(links, key=lambda p:p['score'], reverse=True)
    print sortedLinks[0]
    print sortedLinks[len(sortedLinks)-1]
