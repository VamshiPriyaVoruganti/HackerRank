n = input()
s = set(map(int, raw_input().split()))
n = int(raw_input())
for x in range(n):
    s1=raw_input().split()
    if len(s1)>1:  eval("s."+s1[0]+"("+s1[1]+")")
    else: eval("s."+s1[0]+"("+")")
print sum(s)
