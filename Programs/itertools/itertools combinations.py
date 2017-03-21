from itertools import combinations
s,n=raw_input().split()
for i in range(1,int(n)+1): 
    for x in list(combinations(sorted(s),i)): print "".join(x)
