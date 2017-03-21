from itertools import combinations_with_replacement
s,n=raw_input().split()
for x in list(combinations_with_replacement(sorted(s),int(n))): print "".join(x)
