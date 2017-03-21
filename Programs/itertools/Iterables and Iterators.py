from itertools import combinations
count=0
k,s,n=int(raw_input()),raw_input().split(),int(raw_input())
for x in list(combinations(sorted(s),int(n))): 
    if 'a' in "".join(x):  count+=1
print float(count)/len(list(combinations(sorted(s),int(n))))
