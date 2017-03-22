from collections import defaultdict
d = defaultdict(list)
b=[]
n, m = map(int,raw_input().split())
for i in range(0,n): d[raw_input()].append(i+1) 
for i in range(0,m): b=b+[raw_input()]  
for i in b: 
    if i in d: print " ".join(map(str,d[i]))
    else: print -1
