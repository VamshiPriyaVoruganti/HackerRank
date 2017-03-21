for x in range(2):
    n=int(raw_input())
    a1=(raw_input())
    l=a1.split()
    newlis = list(map(int, l))
    if(x==0): a=set(newlis)
    if(x==1): b=set(newlis)
c= a.difference(b)
c.update(b.difference(a))
c=sorted(c)
for x in c:
    print x
