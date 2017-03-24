for _ in range(int(raw_input())):
    c=0; c1=0
    s = raw_input();l={};l=set()
    if len(s)==10 and s.isalnum():
        for x in s: 
            if x.isupper(): c+=1
            if x.isdigit(): c1+=1
            l.add(x)
        if len(l)==len(s) and c>=2 and c1>=3: print "Valid"
        else: print "Invalid"
    else: print "Invalid"
        
