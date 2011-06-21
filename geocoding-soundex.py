from itertools import groupby

def soundex(word):
    table = {}
    yield word[0]
    codes = (table[char]
             for char in word[1:]
             if char in table)
    for code in groupby(codes):
        yield code
