from operator import itemgetter
from collections import defaultdict

def freeform(string):
    ranks = defaultdict(float)
    searchfuncs = [(phonetic, 0.3),
                   (levenshtein, 0.15),
                   (trigrams, 0.55)]
    for searchfunc, coef in searchfuncs:
        for match, rank in searchfunc(string):
            ranks[match] += rank * coef
    return max(ranks.iteritems(), key=itemgetter(1))
