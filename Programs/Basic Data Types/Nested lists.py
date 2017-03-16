l={}
final=[]
l=set()
d={}
i=0
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    d[name]=score
    l.add(score)
l=sorted(l)
for k,v in d.items():
    if v==l[1]:
        final.insert(i,k)
        i+=1
final.sort()
for x in range(len(final)):
    print final[x]
    
     
      

