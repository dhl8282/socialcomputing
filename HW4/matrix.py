import nltk, math, os, json

def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v1)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

def compute_similarity(_terms1, _terms2):
    # Take care not to mutate the original data structures
    # since we're in a loop and need the originals multiple times
    terms1 = _terms1.copy()
    terms2 = _terms2.copy()
    # Fill in "gaps" in each map so vectors of the same length can be computed
    for term1 in terms1:
        if term1 not in terms2:
            terms2[term1] = 0
    for term2 in terms2:
        if term2 not in terms1:
            terms1[term2] = 0
    # Create vectors from term maps
    v1 = [score for (term, score) in sorted(terms1.items())]
    v2 = [score for (term, score) in sorted(terms2.items())]
    # Compute similarity amongst documents
    return cosine_similarity(v1, v2)