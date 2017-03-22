from collections import deque
d = deque()
for _ in range(int(raw_input())):
    s=raw_input().split()
    cmd=s[0]
    if len(s)>1: cmd+="("+s[1]+")"
    else: cmd+="("+")"
    eval('d.'+cmd)
for x in d:
    print x,
