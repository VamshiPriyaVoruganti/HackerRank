l=set()
n = int(raw_input())
a = set(map(int,raw_input().split()))
n = int(raw_input())
for x in range(n):
    s=raw_input().split()
    cmd=s[0]
    b = set(map(int, raw_input().split()))
    eval("a."+cmd+'(b)')
print sum(a)
