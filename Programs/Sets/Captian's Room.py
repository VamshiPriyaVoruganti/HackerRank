n = int(raw_input())
l = list(map(int,raw_input().split()))
s = set(l)
print ((sum(s))*n-sum(l))/(n-1)
