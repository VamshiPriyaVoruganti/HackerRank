"""from itertools import product
n,k = raw_input().split()
l1=[]; i=-1 
total=0
arrayN = []
for _i_ in range(int(n)):
    arrayN.append([int(x) for x in raw_input().split()][0:])
l=list(product(*arrayN))
for x in l:
    for i in x: 
        total+=i*i
        total=total%int(k)
        l1.append(total)
    total=0
print max(l1)"""


from itertools import *
K, M = map(int, raw_input().split())
N = []
for _ in xrange(K):
     N.append(map(int, raw_input().split())[1:])        
MAX = -1
for i in product(*N):
    MAX = max(sum(map(lambda x: x**2, i))%M, MAX)
print MAX 
