from itertools import groupby
l = [(len(tuple(g)), k) for k,g in groupby(raw_input(), int)]
print ' '.join(map(str, l))
