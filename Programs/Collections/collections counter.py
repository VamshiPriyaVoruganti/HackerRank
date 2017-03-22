from collections import Counter
n=raw_input()
l=list(map(int,raw_input().split()))
s=Counter(l).keys()
count=Counter(l).values()
money=0
n=int(raw_input())
for x in range(n):
    size,price=raw_input().split()
    if int(size) in s and count[s.index(int(size))]>0: 
        money+=int(price)
        value = count[s.index(int(size))]
        count[s.index(int(size))]=value-1
print money   
