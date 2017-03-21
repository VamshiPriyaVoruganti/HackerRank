from itertools import permutations
s,n=raw_input().split()
for x in list(permutations(sorted(s),int(n))): print "".join(x)
