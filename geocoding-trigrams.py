from itertools import izip, islice, tee

def nwise(iterable, count=2):
    iterables = enumerate(tee(iterable, count))
    return izip(*[islice(iterable, start, None)
                  for start, iterables in iterables])

def trigrams(string):
    string = ''.join(['  ', string, ' ']).lower()
    return nwise(string, 3)
