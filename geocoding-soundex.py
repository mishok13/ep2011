from itertools import groupby

def soundex(word):
    table = {'b': 1, 'f': 1, 'p': 1, 'v': 1,
             'c': 2, 'g': 2, 'j': 2, ...}
    yield word[0]
    codes = (table[char]
             for char in word[1:]
             if char in table)
    for code in groupby(codes):
        yield code
